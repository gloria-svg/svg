import cv2

face_haar_cascade = cv2.cascadeClassifier (cv2.data.haarcascade + 'haarcascade_frontalface')
image = cv2.imread('mic.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitkey(e)

   faces = face_haar_cascade.detectMultiscale(gray, 1.1, 4)

   for (x,y,w,h) in faces:
       cv2.rectangle(image, (x,y), (x+w, y+h),(0, 255, 0), 5)

    cv2.imshow("Faces", image)
    cv2.waitkey(e)
    cv2.destroyAllWindows()
