# from deepface import DeepFace
# import cv2
# import time

# face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)

# start_time = time.time()
# emotion_list = []

# while True:

#     ret, frame = cap.read()
#     if not ret:
#         break
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_detector.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#         # crop face region
#         face_img = frame[y:y+h, x:x+w]
#         emotions = DeepFace.analyze(face_img, actions=['emotion'],enforce_detection=False)
       
#         emotion=emotions[0]['dominant_emotion']
#         prob=emotions[0]['emotion'][emotion]
#         cv2.putText(frame, f"{emotion}={prob}", (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1, cv2.LINE_AA)

#         # append emotion to list
#         emotion_list.append(emotion)

#     # display frame
#     cv2.imshow('Real-time Emotion Detection',frame)

#     # check if 10 seconds have passed
#     if time.time() - start_time >= 10:
#         # count occurrences of each emotion
#         emotion_counts = {}
#         for emotion in emotion_list:
#             if emotion in emotion_counts:
#                 emotion_counts[emotion] += 1
#             else:
#                 emotion_counts[emotion] = 1
#         # get most occurring emotion
#         most_common_emotion = max(emotion_counts, key=emotion_counts.get)
#         print(f"Most common emotion in the last 10 seconds: {most_common_emotion}")
#         # clear emotion list and reset start time
#         emotion_list.clear()
#         start_time = time.time()

#     # exit if 'ESC' is pressed
#     if cv2.waitKey(1) == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

from deepface import DeepFace
import cv2
import time

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_emotions():
    
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    emotions = []
    while (time.time() - start_time) < 20:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # crop face region
            face_img = frame[y:y+h, x:x+w]
            emotion = DeepFace.analyze(face_img, detector_backend='opencv', 
                                       align = True, enforce_detection=False,
                                       actions=['emotion'])[0]['dominant_emotion']
            emotions.append(emotion)
            cv2.putText(frame, f"{emotion}", (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1, cv2.LINE_AA)

        cv2.imshow('Real-time Emotion Detection', frame)

        # exit if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # count most common emotion in last 20 seconds
    if emotions:
        most_common_emotion = max(set(emotions), key = emotions.count)
        return most_common_emotion
    else:
        return "No emotions detected in last 20 seconds."

print(detect_emotions())