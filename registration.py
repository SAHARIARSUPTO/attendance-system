import os
import requests

def insert_student(student_id, backend_url):
    try:
        payload = {"studentID": student_id, "password": student_id}  # Assuming password is the same as student ID
        response = requests.post(backend_url, json=payload)
        
        if response.status_code == 200:
            print(f"Student with ID {student_id} registered successfully")
        else:
            print(f"Failed to register student with ID {student_id}. Status code: {response.status_code}")
    except Exception as e:
        print("Error occurred during registration:", e)

def extract_student_ids_and_post(folder_path, backend_url):
    try:
        for filename in os.listdir(folder_path):
            student_id, _ = os.path.splitext(filename)
            insert_student(student_id, backend_url)
    except Exception as e:
        print("Error occurred during login:", e)

if __name__ == "__main__":
    images_folder = "Images"  # Update this to the path where your student images are stored
    backend_url = "https://vu-server.vercel.app/login"

    extract_student_ids_and_post(images_folder, backend_url)
