import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
# img=cv2.imread("----.JPG")
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,1.1,5)
    for (fx,fy,fw,fh) in face:
        cv2.rectangle(frame,(fx,fy),(fx+fw,fy+fh),(0,0,255),2)
        eye_gray=gray[fy:fy+fh, fx:fx+fw]
        eye_color=frame[fy:fy+fh, fx:fx+fw]
        eye=eye_cascade.detectMultiScale(eye_gray,1.1,4)
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(eye_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    if cv2.waitKey(10)==ord("q"):
        break
    cv2.imshow("frame",frame)
