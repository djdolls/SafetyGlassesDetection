import numpy as np
import cv2


face_casade = cv2.CascadeClassifier('C:\\Users\\dhananjay_hedaoo1\\PycharmProjects\\Haarcascade\\trained_classifier\\haarcascade_frontalface_default.xml')

# eye_casade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')


# watch_cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(0)
count = 0;
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_casade.detectMultiScale(gray, 1.3, 5)

    is_face_detected = False
    is_eye_detected = False
    is_image_capture = True
    height, width = img.shape[:2]
    for (x,y,w,h) in faces:
        x1 = 0 if x - w < 0 else x - w
        y1 = 0 if y - h < 0 else y - h
        x2 = width if x + 2 * w > width else x + 2 * w
        y2 = height if y + 3 * h > height else y + 3 * h

        cv2.rectangle(img, (x1,y1), (x2 , y2), (255,0,0), 2)
        # img[y1:y2, x1:x2, 0] = cv2.equalizeHist(img[y1:y2, x1:x2, 0])
        # cv2.imwrite('C:\\Users\\dhananjay_hedaoo1\\PycharmProjects\\Haarcascade\\CameraCropper\\ '  +  str(count) + '.jpg', img[y1:y2, x1:x2])
        count = count + 1





    cv2.imshow('img',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
