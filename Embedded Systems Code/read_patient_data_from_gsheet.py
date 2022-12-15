import sys
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
