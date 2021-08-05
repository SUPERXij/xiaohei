import cv2
# 调用人脸识别库
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# 调用摄像头，具体参数看电脑摄像头参数
cap = cv2.VideoCapture(0)
# 摄像头宽度跟高度
cap.set(3, 640)
cap.set(4, 480)
# 亮度
cap.set(10, 100)
while True:
    success, img = cap.read()
    # 镜像
    imgMirror = cv2.flip(img, 1)
    imgResult = imgMirror.copy()
    imgGray = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    # 人脸框架
    for (x, y, w, h) in faces:
        cv2.rectangle(imgResult, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("faceid", imgResult)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break