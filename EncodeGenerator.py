import cv2
import face_recognition
import pickle
import os

# Define the path for local storage
local_data_path = "local_data.pkl"

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
encodeDict = {}  # Initialize an empty dictionary to store encodings
for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    student_id = os.path.splitext(path)[0]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(img)  # Detect face locations
    if len(face_locations) > 0:  # Check if at least one face is detected
        encode = face_recognition.face_encodings(img)[0]  # Get encoding of the first detected face
        encodeDict[student_id] = encode  # Store encoding with student ID as key
    else:
        print(f"No face detected in {path}")

print("Encoding Started ...")

# Save the encodings locally
with open(local_data_path, 'wb') as f:
    pickle.dump(encodeDict, f)

print("Encodings saved locally.")
