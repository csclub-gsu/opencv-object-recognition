import cv2
import numpy as np

def render(model):
    rect_color = (0, 255, 255)
    rect_thickness = 2
    windowName = 'bruh'

    cam_object = cv2.VideoCapture(0)

    while True:
        ret, frame = cam_object.read()

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