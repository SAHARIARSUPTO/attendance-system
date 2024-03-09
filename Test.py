import requests

# Define the URL of the backend server
backend_url = "http://localhost:3000/login"

# Check if there are any existing students in the database
response = requests.get(backend_url)

if response.status_code == 200:
    existing_students = response.json()
    if existing_students:
        print("Existing students found in the database.")
    else:
        print("No existing students found in the database. Proceeding with registration.")

        # Define the student data to be registered
        student_data = {
            "studentID": "4544",
            "password": "4545"
        }

        # Send a POST request to register the student
        registration_response = requests.post(backend_url, json=student_data)

        # Check the registration response
        if registration_response.status_code == 200:
            print("Student registered successfully!")
            print(registration_response.json())  # Print the response message
        else:
            print("Failed to register student.")
            print(registration_response.json())  # Print the error message if available
else:
    print("Failed to fetch existing students from the database.")
    print(response.json())  # Print the error message if available
