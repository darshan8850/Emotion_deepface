from deepface import DeepFace
import cv2

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # crop face region
        face_img = frame[y:y+h, x:x+w]
        emotions = DeepFace.analyze(face_img, actions=['emotion'],enforce_detection=False)
        #print(emotions)
       
        emotion=emotions[0]['dominant_emotion']
        prob=emotions[0]['emotion'][emotion]
        cv2.putText(frame, f"{emotion}={prob}", (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow('Real-time Emotion Detection',frame)

    # exit if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
