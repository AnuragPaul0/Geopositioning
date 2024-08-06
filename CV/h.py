# import setup_path
import airsim

import numpy as np
import os
import tempfile
import pprint
import cv2
import keyboard  # using module keyboard
from time import sleep# importing pygame module
# from pyquaternion import Quaternion
# import pygame
 
# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
# client.enableApiControl(False)
client.enableApiControl(True)
# quick snap
state = client.getMultirotorState()
s = pprint.pformat(state)
# print("state: %s" % s)
'''
imu_data = client.getImuData()
s = pprint.pformat(imu_data)
# print("imu_data: %s" % s)

barometer_data = client.getBarometerData()
s = pprint.pformat(barometer_data)
# print("barometer_data: %s" % s)

magnetometer_data = client.getMagnetometerData()
s = pprint.pformat(magnetometer_data)
# print("magnetometer_data: %s" % s)

gps_data = client.getGpsData()
s = pprint.pformat(gps_data)
# print("gps_data: %s" % s)

# client.reset()
'''
print('Press 7 to takeoff')
'''
# def ml(): return -client.simGetVehiclePose().position.x_val
# def mf(): return -client.simGetVehiclePose().position.y_val
# def mu(): return -client.simGetVehiclePose().position.z_val
'''
def ml(): # fname, lname l=
    return -client.simGetVehiclePose().position.x_val
def mf(): # fname, lname f=
    return -client.simGetVehiclePose().position.y_val
def mu(): # fname, lname u=
    return -client.simGetVehiclePose().position.z_val
s=1; d = 1
# client.moveToPositionAsync(b, f, -u, s).join() # -10, 10, -10, 5
# client.moveToPositionAsync(f, l-4, u, s).join() # -10, 10, -10, 5
print(np.round([ml(),mf(),mu()], 3))
# print(client.simGetCameraInfo(0).pose.orientation)
'''
q = client.getCameraInfo(0).pose.orientation #this is different from the getOrientation, taking the latter can create problem due to the fact that the drone move slower than the cam?
my_quaternion = Quaternion(w_val=q.w_val,x_val=q.x_val,y_val= q.y_val,z_val=q.z_val)
mvm = my_quaternion.rotate(action)
donre_vel_rota = [client.getVelocity().x_val , client.getVelocity().y_val , client.getVelocity().z_val]
client.moveByVelocity(vx = donre_vel_rota[0] + mvm[0], #the already existing speed + the one the agent wants to add, smoother drive?
                          vy = donre_vel_rota[1] + mvm[1],
                          vz = donre_vel_rota[2] + mvm[2],
                          duration = duration , #will last x secondes or will be stoped by a new command (put a time.sleep(0.5) next to it)
                          drivetrain =  drivetrain, #the camera is indepedant of the movement, but the movement is w.r.t the cam orientation
                          yaw_mode = YawMode(is_rate = True, yaw_or_rate = actions[3]) ) # True means that yaw_or_rate is seen as a degrees/sec
'''
"""
# initialising pygame
pygame.init()
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
        if event.mod == pygame.KMOD_NONE:
            print('No modifier keys were in a pressed state when this '
                  'event occurred.')
        else:
            if event.mod & pygame.KMOD_LSHIFT:
                print('Left shift was in a pressed state when this event '
                      'occurred.')
            if event.mod & pygame.KMOD_RSHIFT:
                print('Right shift was in a pressed state when this event '
                      'occurred.')
            if event.mod & pygame.KMOD_SHIFT:
                print('Left shift or right shift or both were in a '
                      'pressed state when this event occurred.')
"""
# vx, vy, vz, duration drivetrain , yaw_mode = YawMode(), vehicle_name = '' , DrivetrainType.MaxDegreeOfFreedom
while True:

    if keyboard.is_pressed('7'):  # if key '4' is pressed
        # airsim.wait_key('Press any 8 to takeoff')
        print("Taking off...")
        client.armDisarm(True)#b
        # client.takeoffAsync().join()
        # late snap
        state = client.getMultirotorState()
        # print("state: %s" % pprint.pformat(state))

        # airsim.wait_key('Press any key to move vehicle to (-10, 10, -10) at 5 m/s')
        # client.moveToPositionAsync(b, f, -u, s).join() # -10, 10, -10, 5
        break
    sleep(0.05)# .05=50 milliseconds
        
# client.moveToPositionAsync(f, l-4, u, s).join() # -10, 10, -10, 5
print(np.round([ml(),mf(),mu()], 3))
# client.moveByVelocityBodyFrameAsync(1, 0, 0, 1)
r=.05;a=0;w=0;q=0 #x
# w+=r;print(w)
while True:
    '''
    l=0;u=0;f=0 # v
    if keyboard.is_pressed('4'):
        l-=1; print('l-1')
    if keyboard.is_pressed('8'):
        f+=1; print('f+1')
    if keyboard.is_pressed('6'):
        l+=1; print('l+1')
    if keyboard.is_pressed('5'):
        f-=1; print('f-1')
    if keyboard.is_pressed('7'):
        u-=1; print('u-1')
    if keyboard.is_pressed('9'):
        u+=1; print('u+1')# if key '4' is pressed
    client.moveByVelocityBodyFrameAsync(f, l, u, d)
    '''
    if keyboard.is_pressed('s'):
        w-=r; print(w)# if key '4' is pressed
    if keyboard.is_pressed('a'):
        a-=r; print(a)# if key '4' is pressed
    if keyboard.is_pressed('w'):
        w+=r; print(w)# if keya'4' is pressed
    if keyboard.is_pressed('d'):
        a+=r; print(a)# if key '4' is pressed
    if keyboard.is_pressed('q'):
        q+=r; print(q)# if key '4' is pressed
    if keyboard.is_pressed('e'):
        q-=r; print(q)# if key '4' is pressed
    if keyboard.is_pressed('r'):
        while q!=0 or a!=0 or w!=0:
            if q>0:q-=r
            elif q<0: q+=r
            if abs(q)<r: q=0
            if a>0:a-=r 
            elif a<0: a+=r
            if abs(a)<r: a=0
            if w>0:w-=r
            elif w<0: w+=r
            if abs(w)<r: w=0
            sleep(0.2)
            client.simSetCameraPose(0, airsim.Pose(airsim.Vector3r(0, 0, 0), airsim.to_quaternion(w, q, a)))  #PRY in radians
            # l-=2#b camera_pose = 
    # print(np.round([ml(),mf(),mu()], 3))
    client.simSetCameraPose(0, airsim.Pose(airsim.Vector3r(0, 0, 0), airsim.to_quaternion(w, q, a)))  #PRY in radians
    # client.moveToPositionAsync(0, 0, 0, s).join() # -10, 10, -10, 5
    #mf(), ml()-2, mu()
    # print(np.round([ml(),mf(),mu()], 3))
    sleep(0.3)# .5=50 milliseconds
    # break
 #[:2]self, vehicle_name = ''
client.moveToPositionAsync(0, 10, -20, 5).join() # -10, 10, -10, 5
#+f-b,+r-l,+d-u
# my_function("Emil", "Refsnes")
# client.hoverAsync().join()
client.moveToPositionAsync(-10, 0, -20, 5).join() # -10, 10, -10, 5

# client.hoverAsync().join()

state = client.getMultirotorState()
# print("state: %s" % pprint.pformat(state))

airsim.wait_key('Press any key to take images')
# get camera images from the car
responses = client.simGetImages([
    airsim.ImageRequest("0", airsim.ImageType.DepthVis),  #depth visualization image
    airsim.ImageRequest("1", airsim.ImageType.DepthPerspective, True), #depth in perspective projection
    airsim.ImageRequest("1", airsim.ImageType.Scene), #scene vision image in png format
    airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)])  #scene vision image in uncompressed RGBA array
print('Retrieved images: %d' % len(responses))

tmp_dir = os.path.join(tempfile.gettempdir(), "airsim_drone")
print ("Saving images to %s" % tmp_dir)
try:
    os.makedirs(tmp_dir)
except OSError:
    if not os.path.isdir(tmp_dir):
        raise

for idx, response in enumerate(responses):

    filename = os.path.join(tmp_dir, str(idx))

    if response.pixels_as_float:
        print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
        airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
    elif response.compress: #png format
        print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
        airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
    else: #uncompressed array
        print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
        img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) # get numpy array
        img_rgb = img1d.reshape(response.height, response.width, 3) # reshape array to 4 channel image array H X W X 3
        cv2.imwrite(os.path.normpath(filename + '.png'), img_rgb) # write to png

airsim.wait_key('Press any key to reset to original state')

client.reset()
client.armDisarm(False)

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False)