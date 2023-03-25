import cv2
import numpy as np
import time
import datetime

def make_normal_frame(t0, frame):
    frame_copy = frame.copy()
    t1 = time.time() - t0
    t1_str = str(round(t1, 2))
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S") + " | " + t1_str
    developer_name = "Sajad Kamali"
    BLACK = (0, 0, 0)
    cv2.putText(frame_copy, developer_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, BLACK, 2)
    cv2.putText(frame_copy, formatted_date , (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, BLACK, 1)
    return frame_copy

def make_red_frame(frame):
    frame_copy = frame.copy()
    frame_copy[:, :, 2] = 255
    return frame_copy

def make_inversed_frame(frame):
    frame_copy = frame.copy()
    frame_copy = 255 - frame_copy
    return frame_copy

def make_gray_frame(frame):
    gray_frame = np.array(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    gray_frame = cv2.merge((gray_frame, gray_frame, gray_frame))
    return gray_frame

t0 = time.time()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cap.read()
    if ret:
        frame =  cv2.flip(frame, 1)

        normal_frame = make_normal_frame(t0, frame)
        red_frame = make_red_frame(frame)
        inversed_frame = make_inversed_frame(frame)
        gray_frame = make_gray_frame(frame)

        top_frames = np.concatenate((normal_frame, red_frame), axis=1)
        bottom_frames = np.concatenate((inversed_frame, gray_frame), axis=1)
        total_frames = np.concatenate((top_frames, bottom_frames))

        cv2.imshow("temp_frame", total_frames)
        q = cv2.waitKey(1)
        if q == ord('q'):
            break

cv2.destroyAllWindows()
cap.release()
