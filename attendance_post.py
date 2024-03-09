import requests

def post_attendance_to_server(class_name, date, student_id):
    url = "https://vu-server.vercel.app/attendance"  # Corrected endpoint for posting attendance
    payload = {
        "class_name": class_name,
        "date": date,
        "student_id": student_id
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Attendance data posted successfully!")
        else:
            print(f"Failed to post attendance data. Status code: {response.status_code}")
    except Exception as e:
        print("Error while posting attendance data:", e)
