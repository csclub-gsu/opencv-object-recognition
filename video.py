import cv2
import numpy as np
import math

def render(model):
    rect_color = (0, 255, 255)
    rect_thickness = 2
    windowName = 'bruh'

    cam_object = cv2.VideoCapture(0)

    while True:
        ret, frame = cam_object.read()

        ### ISSUE 3 START - Use this area to create the camera transformations to match the camera quality of the drone ###
        
         # Either (set the camera's resolution to 720p)
        cam_object.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cam_object.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        # Or (adjust the focal length of the camera | tello's fov = 82.6, tello's width = 1280)
        width = int(cam_object.get(cv2.CAP_PROP_FRAME_WIDTH))
        desired_focal_length = width / (2 * math.tan(math.radians(82.6 * (1280 / width)) / 2))
        cam_object.set(cv2.CAP_PROP_FOCUS, desired_focal_length)

        ### ISSUE 3 END ###

        recognized_objects = model(np.asarray(frame))  # converts image into array

        # drawing rects from recognized_objects
        for x, y, width, height in recognized_objects:
            frame = cv2.rectangle(frame, (x, y), (x + width, y + width), rect_color, rect_thickness)

        # rendering video
        if ret == True:
            cv2.imshow(windowName, frame)

            key = cv2.waitKey(1);

            # terminating conditions, getWindowProperty returns -1 if window is closed
            # throws error after closing i have no idea why
            if key == ord("q") or cv2.getWindowProperty(windowName, 0) == -1:
                break

    cam_object.release()
    cv2.destroyAllWindows()
