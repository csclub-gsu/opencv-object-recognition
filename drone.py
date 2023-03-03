from djitellopy import Tello
import time
import keyboard

tello = Tello()
tello.connect()

# tello.takeoff()
# We have got our drone and it is functional. This is the file for drone-movement-related code.
# tello.land()

def move():
    if keyboard.is_pressed('w'):
        tello.forward(20)
    elif keyboard.is_pressed('s'):
        tello.back(20)
    elif keyboard.is_pressed('a'):
        tello.left(20)
    elif keyboard.is_pressed('d'):
        tello.right(20)
    elif keyboard.is_pressed("space"):
        tello.up(20)
    elif keyboard.is_pressed("shift"):
        tello.down(20)
    elif keyboard.is_pressed(","):
        tello.ccw(1)
    elif keyboard.is_pressed("."):
        tello.cw(1)
    else:
        tello.stop()

while True:
    # senses if keyboard letters are pressed and does tello's takeoff, land, or completely stop all motors
    if keyboard.is_pressed('t'):
        tello.takeoff()
    if keyboard.is_pressed('l'):
        tello.land()
        break
    if keyboard.is_pressed("esc"):
        tello.emergency()
        break


    #maybe test to see if we hold a key, if the drone continues in that direction.
    move()
