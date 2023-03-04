from djitellopy import Tello
import time
import keyboard

tello = Tello()
tello.connect()

speed = 100 #speed in cm/s

# test of how the send rc control works
# need to test out if the drone moves with these commands, or completely fails.

while True:
    # senses if keyboard letters are pressed and does tello's takeoff, land, or completely stop all motors
    if keyboard.is_pressed('t'):
        tello.takeoff()
    if keyboard.is_pressed('l'):
        tello.land()
    if keyboard.is_pressed('esc'):
        tello.emergency()
        break

    #sets values for tello rc command all to 0
    lrVal=0
    fbVal=0
    udVal=0
    yVal=0

    #list of if seeing if the keys are pressed and then changing the value 
    
    #Forwards
    if keyboard.is_pressed('w'):
        fbVal = speed
    
    #Left
    if keyboard.is_pressed('a'):
        lrVal = -(speed)

    #Backwards
    if keyboard.is_pressed('s'):
        fbVal = -(speed)

    #Right
    if keyboard.is_pressed('d'):
        lrVal = speed

    #Up
    if keyboard.is_pressed('space'):
        udVal = speed
    
    #Down
    if keyboard.is_pressed('shift'):
        udVal = -(speed)

    #Yaw: counterclockwise
    if keyboard.is_pressed(','):
        yVal = -(speed)

    #Yaw: clockwise
    if keyboard.is_pressed('.'):
        yVal = speed

    #sending the rc command to tello drone
    tello.send_rc_control(lrVal, fbVal, udVal, yVal)
    #honestly I dont know what the function does..., so we need to test and see
