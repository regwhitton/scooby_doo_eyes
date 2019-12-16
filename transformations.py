import cv2
import dlib
from imutils import face_utils, resize

SHAPE_PREDICTOR = './shape_predictor_68_face_landmarks.dat'

face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor(SHAPE_PREDICTOR)
(left_eye_start, left_eye_end) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(right_eye_start, right_eye_end) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

def transform(keypress, frame):
    transformations = transformation_lists[to_list_index(keypress)]
    for t in transformations:
        frame = t(frame)
    return frame

def to_list_index(keypress):
    max = len(transformation_lists) - 1
    if keypress < ord("0") or keypress > ord("9"):
        return max
    digit = keypress - ord("0")
    return digit if digit < max else max


def tx_mirror_flip(frame):
    return cv2.flip(frame, 1)

def tx_grey_scale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def tx_scale(frame):
    return resize(frame, width=450)

def detect_faces(frame):
    return face_detector(frame, 0)

def outline_rect(frame, rect):
    tl = rect.tl_corner()
    br = rect.br_corner()
    cv2.rectangle(frame, (tl.x, tl.y), (br.x, br.y), (0, 255, 0), 1)
    
def tx_outline_faces(frame):
    for face in detect_faces(frame):
        outline_rect(frame, face)
    return frame

def find_eyes_in_rect(frame, rect):
    shapes = shape_predictor(frame, rect)
    shapes = face_utils.shape_to_np(shapes)
    left_eye = shapes[left_eye_start:left_eye_end]
    right_eye = shapes[right_eye_start:right_eye_end]
    return (left_eye, right_eye)

def outline_shape(frame, shape):
    cv2.drawContours(frame, [shape], -1, (0, 255, 0), 1)

def tx_outline_eyes(frame):
    for face in detect_faces(frame):
        (left_eye, right_eye) = find_eyes_in_rect(frame, face)
        outline_shape(frame, left_eye)
        outline_shape(frame, right_eye)
    return frame

transformation_lists = [
    [],
    # [tx_mirror_flip],
    # [tx_mirror_flip, tx_grey_scale],
    # [tx_mirror_flip, tx_grey_scale, tx_outline_faces],
    # [tx_mirror_flip, tx_grey_scale, tx_outline_eyes]
    [tx_mirror_flip],
    [tx_scale, tx_grey_scale],
    [tx_scale, tx_grey_scale, tx_outline_faces],
    [tx_outline_eyes]
]
