import cv2

def transform(keypress, frame):
    for i in range(n_transformations(keypress)):
        frame = transformations[i](frame)
    return frame

def n_transformations(keypress):
    max = len(transformations)
    if keypress < ord("0") or keypress > ord("9"):
        return max
    digit = keypress - ord("0")
    return digit if digit < max else max

transformations = [
    lambda frame: cv2.flip(frame, 1),
    lambda frame: cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
]