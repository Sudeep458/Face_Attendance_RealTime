import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendance-48f10-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Sudeep Suresh",
            "major": "Computer  Science",
            "starting_year": 2021,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-05-11 00:23:34"
        },
    "852741":
        {
            "name": "Sandeepa Suresh",
            "major": "Economics",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2024-06-11 00:53:21"
        },
    "963852":
        {
            "name": "Renuka Suresh",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-04-11 00:44:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)