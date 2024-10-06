# Face Recognition Attendance System

This project implements a **Face Recognition Attendance System** using Python, OpenCV, Firebase, and a real-time database. The system detects faces using a webcam, matches them against stored encodings, and logs attendance data in Firebase.

## Features

- Real-time face detection and recognition.
- Firebase integration for student data and attendance logging.
- Automatically updates attendance and last-seen time in Firebase.

## Prerequisites

Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Install Required Libraries

You can install the required libraries using pip. Make sure to install them in your virtual environment.

```bash
pip install opencv-python firebase-admin face_recognition cvzone
```

## Install Required Libraries

You can install the required libraries using pip. Make sure to install them in your virtual environment.

```bash
pip install opencv-python
pip install firebase-admin
pip install face_recognition
pip install cvzone
```

## Setup Firebase

-Create a Firebase project at Firebase Console.
-Enable the Realtime Database and Storage.
-Generate a service account key from Project Settings > Service accounts and download the JSON file.
-Place the downloaded JSON file in the project directory and rename it to **serviceAccountKey.json**.

## Project Structure

```bash
Face-Attendance/
│
├── EncodeGenerator.py         # Script to generate and save face encodings
├── AddDataToDataBase.py       # Script to add student data to Firebase
├── main.py                    # Main script for real-time attendance system
├── Resources/                 # Folder containing resources such as images
│   ├── background.png
│   └── Modes/                 # Mode images for UI
│
├── Images/                    # Folder containing student images
│
└── EncodeFile.p               # File containing saved face encodings
```

## Usage
1. First, run EncodeGenerator.py to generate the face encodings from student images and save them in **EncodeFile.p**.

```bash
python EncodeGenerator.py
```
2. Then, run AddDataToDataBase.py to add student information to the Firebase database.

```bash
python AddDataToDataBase.py
```

3. Finally, run the main.py script to start the face attendance system.

```bash
python main.py
```
Ensure your webcam is connected, and the application will open a window for real-time attendance tracking.

## How It Works

1. **Face Encoding**: The system reads student images, generates encodings, and saves them for future comparison.

2. **Real-Time Detection**: The webcam captures video frames, detects faces, and matches them against stored encodings.
   
3. **Attendance Logging**: When a match is found, the system updates the attendance records and last-seen timestamps in Firebase.






