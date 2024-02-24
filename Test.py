import cv2
import face_recognition

# Open the default camera (usually the first camera)
cap = cv2.VideoCapture(0)

while True:
    # Read frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame from the camera")
        break
    
    # Convert the frame from BGR color (OpenCV) to RGB color (face_recognition)
    rgb_frame = frame[:, :, ::-1]

    # Find all face locations in the frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Draw rectangles around the faces
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
