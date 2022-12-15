import pyrebase

config = {
    "apiKey": "AIzaSyBn6kPFPP9u9Ut5pDQlHbQwTl4ciOUbhUk",
    "authDomain": "pill-9a57d.firebaseapp.com",
    "databaseURL": "https://pill-9a57d-default-rtdb.firebaseio.com",
    "projectId": "pill-9a57d",
    "storageBucket": "pill-9a57d.appspot.com",
    "messagingSenderId": "544548433520",
    "appId": "1:544548433520:web:139e3264cc624b11cfceb5",
    "measurementId": "G-ZPGQ2GX8Y6",
    "serviceAccount": "firebase_key.json"
}

firebase_storage = pyrebase.initialize_app(config)
storage = firebase_storage.storage()

all_files = storage.list_files()

count = 1
for file in all_files:
    if "PRS" in file.name:
        print(file.name)
        download_name = file.name
        download_name = download_name[14:]
        download_name = download_name[:-4]
        download_name = str("Prescriptions/" + download_name + "_IoT_" + str(count) + ".jpg")
        print(download_name)
        storage.child(file.name).download(download_name)