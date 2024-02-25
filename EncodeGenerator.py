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
    encode = face_recognition.face_encodings(img)[0]
    encodeDict[student_id] = encode  # Store encoding with student ID as key

print("Encoding Started ...")

# Save the encodings locally
with open(local_data_path, 'wb') as f:
    pickle.dump(encodeDict, f)

print("Encodings saved locally.")
