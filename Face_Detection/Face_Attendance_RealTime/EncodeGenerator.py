import os
import pickle

import cv2
import face_recognition
import firebase_admin
from firebase_admin import credentials, db, storage

# Check if the Firebase app is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://faceattendance-48f10-default-rtdb.firebaseio.com/",
        'storageBucket': "faceattendance-48f10.appspot.com"
    })

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []

for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    
    # Check if the image is read successfully
    if img is None:
        print(f"Image {path} is not valid or could not be loaded.")
        continue
    
    imgList.append(img)
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        
        # Check if a face encoding was found
        if len(encode) == 0:
            print("No face found in image")
            continue
        
        encodeList.append(encode[0])

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
