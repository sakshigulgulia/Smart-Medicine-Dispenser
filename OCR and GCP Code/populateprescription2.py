import easyocr, sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("key.json", scopes = scope)

file = gspread.authorize(creds)
workbook = file.open("IoT_Write")
sheet = workbook.sheet1

#print(patient_two_populate[0])
def sheet_update_patient_two(patient_two_populate):
    sheet.update_cell(1,7, patient_two_populate[0])
    sheet.update_cell(1,8, patient_two_populate[1])
    sheet.update_cell(2,7, patient_two_populate[2])
    sheet.update_cell(2,8, patient_two_populate[3])
    sheet.update_cell(4,7, patient_two_populate[4])
    sheet.update_cell(4,8, patient_two_populate[5])
    sheet.update_cell(5,7, patient_two_populate[6])
    sheet.update_cell(5,8, patient_two_populate[7])
    sheet.update_cell(6,7, patient_two_populate[8])
    sheet.update_cell(6,8, patient_two_populate[9])

    sheet.update_cell(10,8, patient_two_populate[11])
    sheet.update_cell(10,9, patient_two_populate[12])
    sheet.update_cell(10,10, patient_two_populate[13])
    sheet.update_cell(10,11, patient_two_populate[14])

    sheet.update_cell(11,7, patient_two_populate[15])
    sheet.update_cell(11,8, patient_two_populate[16])
    sheet.update_cell(11,9, patient_two_populate[17])
    sheet.update_cell(11,10, patient_two_populate[18])
    sheet.update_cell(11,11, patient_two_populate[19])

    sheet.update_cell(12,7, patient_two_populate[20])
    sheet.update_cell(12,8, patient_two_populate[21])

    sheet.update_cell(13,7, patient_two_populate[22])
    sheet.update_cell(13,8, patient_two_populate[23])
    sheet.update_cell(13,9, patient_two_populate[24])
    sheet.update_cell(13,10, patient_two_populate[25])
    sheet.update_cell(13,11, patient_two_populate[26])

    sheet.update_cell(14,7, patient_two_populate[27])
    sheet.update_cell(14,8, patient_two_populate[28])

