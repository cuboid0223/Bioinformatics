import cv2
# https://kknews.cc/zh-tw/code/zeoyqka.html
# Load this cascade << 
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# haarcascade_frontalface_default.xml 是OpenCV中已經經過訓練的人臉識別模型文件。
# read the input image  路徑要寫對（我是用相對路徑）
img = cv2.imread('faceDetection/IMG_9940.JPG')
# convert into grayscale ()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)
# draw rectangle around the face
for (x,y,w,h)  in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (225, 0, 0), 2)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
