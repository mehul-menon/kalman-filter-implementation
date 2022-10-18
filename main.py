from kalmanfilter import KalmanFilter
import cv2
from orange_detector import OrangeDetector
#KalmanFilter
kf = KalmanFilter()
od = OrangeDetector()
cap = cv2.VideoCapture('orange.mp4')
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    orange_box = od.detect(frame)
    x1, y1, x2, y2 = orange_box
    cx = int((x1+x2)/2)
    cy = int((y1+y2)/2)
    predict_pos = kf.predict(cx, cy)
    cv2.circle(frame, (cx,cy), 15, (0,0,255), 4)
    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 4)
    cv2.circle(frame, (predict_pos[0],predict_pos[1]), 15, (255,0,0),4)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(50)
    if k==27:
        break