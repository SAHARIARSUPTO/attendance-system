import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
from datetime import datetime
from openpyxl import Workbook

# Check if the encoding file exists
encode_file_path = 'local_data.pkl'
if not os.path.exists(encode_file_path):
    print(f"Error: Encoding file '{encode_file_path}' not found.")
    exit()

# Load the encoding file
print("Loading Encode File ...")
with open(encode_file_path, 'rb') as file:
    encodeDict = pickle.load(file)
print("Encode File Loaded")

# Check if the background image exists
background_image_path = 'Resources/background.png'
if not os.path.exists(background_image_path):
    print(f"Error: Background image '{background_image_path}' not found.")
    exit()

# Initialize VideoCapture
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Failed to open camera.")
    exit()

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
if not os.path.exists(folderModePath):
    print(f"Error: Mode images folder '{folderModePath}' not found.")
    exit()

modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    img_path = os.path.join(folderModePath, path)
    if os.path.isfile(img_path):
        imgModeList.append(cv2.imread(img_path))
    else:
        print(f"Warning: '{img_path}' is not a valid file.")

# Initialize variables
imgBackground = cv2.imread(background_image_path)
modeType = 0
counter = 0
id = -1
imgStudent = []
studentInfo = None  # Initialize studentInfo

# Create a new Excel workbook and select the active worksheet
workbook = Workbook()
worksheet = workbook.active
worksheet.append(["Time", "ID"])

while True:
    try:
        # Read frame from the camera
        success, img = cap.read()

        if not success:
            print("Failed to read frame from the camera")
            break

        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faceCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

        imgBackground[162:162 + 480, 55:55 + 640] = img

        match_found = False  # Flag to track if a match is found

        if faceCurFrame:
            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                matches = face_recognition.compare_faces(list(encodeDict.values()), encodeFace)
                faceDis = face_recognition.face_distance(list(encodeDict.values()), encodeFace)

                matchIndex = np.argmin(faceDis)

                if 0 <= matchIndex < len(matches) and matches[matchIndex]:
                    match_found = True  # Set the flag to True
                    id = list(encodeDict.keys())[matchIndex]

                    # Load image corresponding to the detected ID
                    img_path = f'images/{id}.png'  # Assuming images are named after IDs
                    if os.path.exists(img_path):
                        img_student = cv2.imread(img_path)
                        img_student = cv2.resize(img_student, (414, 633))  # Resize to match the display area

                        # Set the loaded image to appear on the background
                        imgBackground[44:44 + 633, 808:808 + 414] = img_student

                    studentInfo = encodeDict.get(id)
                    if studentInfo is not None:
                        print(f"Match found for student ID: {id}")
                        # Display the student ID or name here
                        # Log the time and ID into the Excel spreadsheet
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        worksheet.append([current_time, id])
                        workbook.save(filename="face_detection_log.xlsx")
                    else:
                        print("Student information not found for matched face.")

                else:
                    print("No match found for the detected face.")

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - x1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)

                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1

            if counter != 0 and match_found:
                if counter == 1:
                    pass
                pass

        else:
            modeType = 0
            counter = 0

        cv2.imshow("Face Attendance", imgBackground)
        cv2.waitKey(1)

    except Exception as e:
        print("Error:", e)
        break

cap.release()
cv2.destroyAllWindows()
