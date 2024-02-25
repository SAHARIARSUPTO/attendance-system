import os
import pickle

# Define the path to save the data locally
local_data_path = "local_data.pkl"

data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1111":
        {
            "name": "Supto",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
            "22331125": {
        "name": "John Doe",
        "major": "Mathematics",
        "starting_year": 2023,
        "total_attendance": 5,
        "standing": "G",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "223311124": {
        "name": "Jane Smith",
        "major": "Computer Science",
        "starting_year": 2022,
        "total_attendance": 8,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "223311156": {
        "name": "Alice Johnson",
        "major": "Biology",
        "starting_year": 2021,
        "total_attendance": 10,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "223311157": {
        "name": "Bob Williams",
        "major": "Chemistry",
        "starting_year": 2020,
        "total_attendance": 9,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "223311158": {
        "name": "Eva Martinez",
        "major": "Psychology",
        "starting_year": 2019,
        "total_attendance": 6,
        "standing": "B",
        "year": 5,
        "last_attendance_time": "2022-12-11 00:54:34"
    }
}

# Save the data to local storage
with open(local_data_path, 'wb') as f:
    pickle.dump(data, f)

print("Data saved locally.")