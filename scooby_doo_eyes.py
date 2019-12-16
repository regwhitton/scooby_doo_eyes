#!./env/python

from imutils.video import VideoStream
import cv2
import pyautogui
from transformations import transform

ESCAPE_KEY = ord("\x1B")

def main():
    try:
        keyboard = Keyboard()
        camera = Camera()
        window = Window()
        while keyboard.get_last_key() != ESCAPE_KEY:
            frame = camera.grab_frame()
            new_frame = transform(keyboard.get_last_key(), frame)
            window.display(new_frame)
    finally:
        camera.close()
        window.close()

class Window:
    NAME = 'Scooby Doo Eyes'
    def __init__(self):
        pyautogui.FAILSAFE = False
        cv2.namedWindow(Window.NAME, cv2.WINDOW_GUI_EXPANDED)
        cv2.setWindowProperty(Window.NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        pyautogui.moveTo(3000, 3000)
    def close(self):
        cv2.destroyWindow(Window.NAME)
    def display(self, image):
        cv2.imshow(Window.NAME, image)

class Camera:
    def __init__(self):
        vs = VideoStream(src=0, usePiCamera=False)
        vs.start()
        self.vs = vs
    def close(self):
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
