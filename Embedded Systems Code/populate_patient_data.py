#import easyocr
import sys
from Fingerprint_Sensor import enroll_finger
from Fingerprint_Sensor import get_num
#from read_patient_data_from_gsheet import *


#import sys
from Fingerprint_Sensor import enroll_finger
from Fingerprint_Sensor import get_num

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("key.json", scopes = scope)

file = gspread.authorize(creds)
workbook = file.open("IoT")
sheet = workbook.sheet1


def read_patient_one_data(patient_one_populate):
    patient_one_populate[10] = sheet.cell(6,2).value
    patient_one_populate[8] = sheet.cell(5,2).value
    patient_one_populate[2] = sheet.cell(1,2).value
    patient_one_populate[4] = sheet.cell(2,2).value

    if sheet.cell(11,2).value != 'Nil':
        patient_one_populate[17] = 1
    else:
        patient_one_populate[17] = 0

    if sheet.cell(11,3).value != 'Nil':
        patient_one_populate[18] = 1
    else:
        patient_one_populate[18] = 0

    if sheet.cell(11,4).value != 'Nil':
        patient_one_populate[19] = 1
    else:
        patient_one_populate[19] = 0

    if sheet.cell(11,5).value != 'Nil':
        patient_one_populate[20] = 1
    else:
        patient_one_populate[20] = 0

    patient_one_populate[16] = sheet.cell(11,1).value #Pill 1 Name
    patient_one_populate[27] = sheet.cell(12,2).value #Pill 1 Days

    if sheet.cell(13,2).value != 'Nil':
        patient_one_populate[22] = 1
    else:
        patient_one_populate[22] = 0

    if sheet.cell(13,3).value != 'Nil':
        patient_one_populate[23] = 1
    else:
        patient_one_populate[23] = 0

    if sheet.cell(13,4).value != 'Nil':
        patient_one_populate[24] = 1
    else:
        patient_one_populate[24] = 0

    if sheet.cell(13,5).value != 'Nil':
        patient_one_populate[25] = 1
    else:
        patient_one_populate[25] = 0

    patient_one_populate[21] = sheet.cell(13,1).value ##Pill 2 Name
    patient_one_populate[26] = sheet.cell(14,2).value #Pill 2 Days

    print(patient_one_populate)
    return patient_one_populate

#edit this
def read_patient_two_data(patient_two_populate):
    patient_two_populate[10] = sheet.cell(6,8).value
    patient_two_populate[8] = sheet.cell(5,8).value
    patient_two_populate[2] = sheet.cell(1,8).value
    patient_two_populate[4] = sheet.cell(2,8).value

    if sheet.cell(11,8).value != 'Nil':
        patient_two_populate[17] = 1
    else:
        patient_two_populate[17] = 0

    if sheet.cell(11,9).value != 'Nil':
        patient_two_populate[18] = 1
    else:
        patient_two_populate[18] = 0

    if sheet.cell(11,10).value != 'Nil':
        patient_two_populate[19] = 1
    else:
        patient_two_populate[19] = 0

    if sheet.cell(11,11).value != 'Nil':
        patient_two_populate[20] = 1
    else:
        patient_two_populate[20] = 0

    patient_two_populate[16] = sheet.cell(11,7).value #Pill 1 name
    patient_two_populate[26] = sheet.cell(12,8).value #Pill 1 days

    if sheet.cell(13,8).value != 'Nil':
        patient_two_populate[22] = 1
    else:
        patient_two_populate[22] = 0

    if sheet.cell(13,9).value != 'Nil':
        patient_two_populate[23] = 1
    else:
        patient_two_populate[23] = 0

    if sheet.cell(13,10).value != 'Nil':
        patient_two_populate[24] = 1
    else:
        patient_two_populate[24] = 0

    if sheet.cell(13,11).value != 'Nil':
        patient_two_populate[25] = 1
    else:
        patient_two_populate[25] = 0

    patient_two_populate[21] = sheet.cell(13,7).value #Pill 2 name
    patient_two_populate[27] = sheet.cell(14,8).value #Pill 2 days
    print(patient_two_populate)
    return patient_two_populate




class Pill:
    #count = 0
    def __init__(self):
        self.pill_status = 1
        self.pill_name = ""
        self.pill_times = [0, 0, 0, 0]
        self.pill_days = 0
        self.pill_dispense = [0, 0, 0, 0]
        self.pill_count = 0
        self.pill_total = 0
        self.pill_recent_dispense = 0
        self.count = 0
    
    def pill_set(self, pill_name, pill_times, pill_days):
        if pill_name != "Nil":
            self.pill_status = 1
            self.pill_name = pill_name
            self.pill_times = pill_times
            self.pill_days = pill_days
            self.pill_dispense = [0, 0, 0, 0]
            self.pill_count = 7
            for i in range(4):
                if self.pill_times[i] == 1:
                    self.count = self.count + int(self.pill_days)
            self.pill_total = self.count
            print(self.pill_total)

class Patient:

    def __init__(self):
        self.pill_one = Pill()
        self.pill_two = Pill()

    def initialize(self, patient_id, name, hospital_name, doctor_name, patient_finger_id):
        self.status = 1
        self.id = patient_id
        self.finger_id = patient_finger_id
        self.patient_name = name
        self.hospital_name = hospital_name
        self.doctor_name = doctor_name

    def populate(self, pill_number, pill_name, pill_times, pill_days):
        if pill_number == 1:
            self.pill_one.pill_set(pill_name, pill_times, pill_days)
        elif pill_number == 2:
            self.pill_two.pill_set(pill_name, pill_times, pill_days)
        

x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
patient_one_temp = x
patient_two_temp = y

#change this
if (sheet.cell(5,2).value != "" and sheet.cell(5,8).value == ""):
    patient_one = Patient()
    list_of_patients = [patient_one]
    patient_one_populate = read_patient_one_data(patient_one_temp)

elif (sheet.cell(5,2).value != "" and sheet.cell(5,8).value != ""):
    patient_one = Patient()
    patient_two = Patient()
    list_of_patients = [patient_one, patient_two]
    patient_one_populate = read_patient_one_data(patient_one_temp)
    patient_two_populate = read_patient_two_data(patient_two_temp)


if (len(list_of_patients) == 1):
    print("Welcome.....")
    print("Enroll your fingerprint for security")
    patient_finger_id = get_num()
    enroll_finger(patient_finger_id)
    list_of_patients[0].initialize(patient_one_populate[10], patient_one_populate[8], patient_one_populate[2], patient_one_populate[4], 1)#patient_finger_id)
    pill_one_times_list = [patient_one_populate[17], patient_one_populate[18], patient_one_populate[19], patient_one_populate[20]]
    list_of_patients[0].populate(1, patient_one_populate[16], pill_one_times_list, patient_one_populate[26])
    pill_two_times_list = [patient_one_populate[22], patient_one_populate[23], patient_one_populate[24], patient_one_populate[25]]
    list_of_patients[0].populate(2, patient_one_populate[21], pill_two_times_list, patient_one_populate[27])#replace 5 with value from list
    
elif (len(list_of_patients) == 2):
    print("Welcome Patient 1....")
    print("Enroll your fingerprint for security")
    #patient_finger_id = get_num()
    #enroll_finger(patient_finger_id)
    list_of_patients[0].initialize(patient_one_populate[10], patient_one_populate[8], patient_one_populate[2], patient_one_populate[4], 1)#patient_finger_id)
    pill_one_times_list = [patient_one_populate[17], patient_one_populate[18], patient_one_populate[19], patient_one_populate[20]]
    list_of_patients[0].populate(1, patient_one_populate[16], pill_one_times_list, patient_one_populate[26])
    pill_two_times_list = [patient_one_populate[22], patient_one_populate[23], patient_one_populate[24], patient_one_populate[25]]
    list_of_patients[0].populate(2, patient_one_populate[21], pill_two_times_list, patient_one_populate[27])
    print(list_of_patients[0])
    print("Welcome Patient 2....")
    print("Enroll your fingerprint for security")
    #patient_finger_id = get_num()
    #enroll_finger(patient_finger_id)
    list_of_patients[1].initialize(patient_two_populate[10], patient_two_populate[8], patient_two_populate[2], patient_two_populate[4], 2)#patient_finger_id)
    pill_one_times_list = [patient_two_populate[17], patient_two_populate[18], patient_two_populate[19], patient_two_populate[20]]
    list_of_patients[1].populate(1, patient_two_populate[16], pill_one_times_list, patient_two_populate[26])
    pill_two_times_list = [patient_two_populate[22], patient_two_populate[23], patient_two_populate[24], patient_two_populate[25]]
    list_of_patients[1].populate(2, patient_two_populate[21], pill_two_times_list, patient_two_populate[27])
    print(list_of_patients[1])
