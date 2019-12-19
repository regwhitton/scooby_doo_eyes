#!./env/python

from imutils.video import VideoStream, WebcamVideoStream
import cv2, sys
import pyautogui
from transformations import transform
import numpy as np

ESCAPE_KEY = ord("\x1B")

def main():
    keyboard = Keyboard()
    window = Window()
    camera = Camera()
    while keyboard.get_last_key() != ESCAPE_KEY:
        frame = camera.grab_frame()
        new_frame = transform(keyboard.get_last_key(), frame)
        window.display(new_frame)

class Window:
    NAME = 'Scooby Doo Eyes'
    def __init__(self):
        pyautogui.FAILSAFE = False
        cv2.namedWindow(Window.NAME, cv2.WINDOW_GUI_EXPANDED)
        cv2.setWindowProperty(Window.NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty(Window.NAME, cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_FREERATIO)
        (_,_,width,height) = cv2.getWindowImageRect(Window.NAME)
        print("Screen size: %d x %d" % (width, height))
        pyautogui.moveTo(width, height)

    def __del__(self):
        cv2.destroyWindow(Window.NAME)
        
    def display(self, image):
        cv2.imshow(Window.NAME, image)

class Camera:
    def __init__(self):
        vs = VideoStream(src=0, usePiCamera=False)
        # if isinstance(vs.stream, WebcamVideoStream):
        #     # Setting camera size is ignored or stops camera if camera doesn't support size.
        #     vs.stream.stream.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        #     vs.stream.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        vs.start()
        if isinstance(vs.stream, WebcamVideoStream):
            width = vs.stream.stream.get(cv2.CAP_PROP_FRAME_WIDTH)
            height = vs.stream.stream.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print("Video frame size: %d x %d" % (width, height))
        self.vs = vs

    def __del__(self):
        if self.vs != None:
            self.vs.stop()

    def grab_frame(self):
        return self.vs.read()

class Keyboard:
    def __init__(self):
        self.last_key = -1

    def get_last_key(self):
        key = cv2.waitKey(1)
        if key > -1:
            self.last_key = key
        return self.last_key

if __name__ == '__main__' :
    main()
