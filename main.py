#!/bin/python

from PIL import Image
import pyvirtualcam
import numpy as np
import cv2


vid = cv2.VideoCapture(0)


with pyvirtualcam.Camera(width=1280, height=720, fps=5) as cam:
    while True:
        ret, frame = vid.read()
        frame = cv2.resize(frame, (420, 240), interpolation=cv2.BORDER_DEFAULT)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        framePIL = Image.fromarray(frame)
        framePIL.save("./frame.jpeg", "jpeg", optimize=True, quality=11)
        framePIL = Image.open("./frame.jpeg")

        newFrame = np.array(framePIL)
        newFrame = cv2.resize(newFrame, (1280, 720), interpolation=cv2.BORDER_DEFAULT)
        
        #cam.send(newFrame)
        cam.send(newFrame)
        cam.sleep_until_next_frame()
        
        if cv2.waitKey(1) == 17: break
    

    vid.release()
    cv2.destroyAllWindows()

