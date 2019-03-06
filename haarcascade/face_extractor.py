import cv2
import numpy as np
import os

#Required File location
filename = 'C:\\Users\\dhananjay_hedaoo1\\PycharmProjects\\Haarcascade\\trained_classifier\\haarcascade_frontalface_default.xml'

# Load the face cascade file
cascade = cv2.CascadeClassifier(filename)
count = 0;
for face in os.listdir('Face'):
    detected_face = False

    try:
        scaling_factor = 1
        image = cv2.imread('Face/' + str(face))
        height, width = image.shape[:2]
        print height, width

        flag = True
        if (width > 2000 or height > 2000) and flag:
            scaling_factor = 0.2
            flag = False

        if (width > 1500 or height > 1500) and flag:
            scaling_factor = 0.3
            flag = False

        if (width > 1000 or height > 1000) and flag:
            scaling_factor = 0.4
            flag = False
        flag = True
        frame = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor,
                           interpolation=cv2.INTER_AREA)
        rects = cascade.detectMultiScale(frame)

        for (x, y, w, h) in rects:
            x1 = 0 if x - w < 0 else x - w
            y1 = 0 if y - h < 0 else y - h
            x2 = width if x + 2 * w > width else x + 2 * w
            y2 = height if y + 3 * h > height else y + 3 * h
            # cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
            detected_face = True
            cv2.imwrite('C:\\Users\\dhananjay_hedaoo1\\PycharmProjects\\Haarcascade\\Crop\\crop' + str(count) + '.jpg',
                        frame[y1:y2, x1:x2])

        if (detected_face!=True):
            print ("Not object detected")
            cv2.imwrite('C:\\Users\\dhananjay_hedaoo1\\PycharmProjects\\Haarcascade\\NotDetected\\nocrop' + str(count) + '.jpg',
                        frame)

        count = count + 1
    except:
        print "Bad exception"

