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
        tello.move_forward(20)
    elif keyboard.is_pressed('s'):
        tello.move_back(20)
    elif keyboard.is_pressed('a'):
        tello.move_left(20)
    elif keyboard.is_pressed('d'):
        tello.move_right(20)
    elif keyboard.is_pressed("space"):
        tello.move_up(20)
    elif keyboard.is_pressed("shift"):
        tello.move_down(20)
    elif keyboard.is_pressed(","):
        tello.rotate_counter_clockwise(1)
    elif keyboard.is_pressed("."):
        tello.rotate_clockwise(1)
    else:
        #tello.stop()
        pass

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
