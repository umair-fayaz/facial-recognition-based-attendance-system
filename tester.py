import cv2
import os
import numpy as np
from pathlib import Path

directory = r'data/images/test_raw/test/'

def faceDetection(testImg):
    grayImg = cv2.cvtColor(testImg, cv2.COLOR_BGR2GRAY)
    faceHaar = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    faces = faceHaar.detectMultiScale(grayImg, scaleFactor=1.3, minNeighbors=5)
    return faces, grayImg

def mainFunction(path):
    path_n = path + '.jpg'
    print(path_n)
    testImg = cv2.imread(path)
    # cv2.imshow("Face Detection", testImg)
    # cv2.waitKey(0)
    facesDetected, grayImg = faceDetection(testImg)
    print("Faces Detected: ", facesDetected)
    os.chdir(directory)

    for (x,y,w,h) in facesDetected:
        roi_color = testImg[y:y + h, x:x + w]
        print("[INFO] Object found. Saving locally.")
        status = cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)
        print("[INFO] Image faces_detected.jpg written to filesystem: ", status)

    print("----- DONE DETECTION -----")
cv2.destroyAllWindows()
