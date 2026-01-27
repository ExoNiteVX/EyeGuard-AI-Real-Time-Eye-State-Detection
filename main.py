import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)
print("AI is watching, press 'Q' to quit.")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_image)

    status = "Eyes opened"
    color = (0, 255, 0)


    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            top = face_landmarks.landmark[159].y
            bottom = face_landmarks.landmark[145].y

            eye_detection = bottom - top



            if eye_detection < 0.012:
                status = "Eyes closed"
                color = (0, 0, 255)




        cv2.putText(image, status, (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,1, color, 2)

        cv2.imshow("Eye detector", image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break



cap.release()
cv2.destroyAllWindows()
