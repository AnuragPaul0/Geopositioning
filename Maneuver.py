import airsim
import sys
import time
from Drone_Auto import image_proc_algorithm
import keyboard  # using module keyboard

#connect and take off drone
client = airsim.MultirotorClient()# for car use CarClient() 
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)
client.takeoffAsync()

# z of -20 is 20 meters above the original launch point.
z = -20

# Fly given velocity vector for 1 seconds
duration = 1
speed = 2

vx = speed
vy = 0

client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 0))

print("choose: 4 5 6 = Turn left back right ,8 straight, 0 get position,"+
          " any key to quit: ")
while True:
    if keyboard.is_pressed('4'):  # if key '4' is pressed
        vx = 0
        vy = -speed
        client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                                airsim.YawMode(False, 270))
    elif keyboard.is_pressed('5'):
        vx = -speed
        vy = 0
        client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                                airsim.YawMode(False, 180))
    elif keyboard.is_pressed('6'): 
        vx = 0
        vy = speed
        client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                                airsim.YawMode(False, 90))
    elif keyboard.is_pressed('8'):
        print('You Pressed 8!')
        vx = speed
        vy = 0
        client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                         airsim.YawMode(False, 0))
    elif keyboard.is_pressed('0'):
        print(client.getMultirotorState().kinematics_estimated.position)
    elif keyboard.is_pressed('n'):
        break
    else:
        continue#break

airsim.wait_key('Press any key to reset to original state')
client.armDisarm(False)
client.reset()

# let's quit cleanly
client.enableApiControl(False)