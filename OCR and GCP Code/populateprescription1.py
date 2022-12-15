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

#print(patient_one_populate[0])
def sheet_update_patient_one(patient_one_populate):
    sheet.update_cell(1,1, patient_one_populate[0])
    sheet.update_cell(1,2, patient_one_populate[1])
    sheet.update_cell(2,1, patient_one_populate[2])
    sheet.update_cell(2,2, patient_one_populate[3])
    sheet.update_cell(4,1, patient_one_populate[4])
    sheet.update_cell(4,2, patient_one_populate[5])
    sheet.update_cell(5,1, patient_one_populate[6])
    sheet.update_cell(5,2, patient_one_populate[7])
    sheet.update_cell(6,1, patient_one_populate[8])
    sheet.update_cell(6,2, patient_one_populate[9])

    sheet.update_cell(10,2, patient_one_populate[11])
    sheet.update_cell(10,3, patient_one_populate[12])
    sheet.update_cell(10,4, patient_one_populate[13])
    sheet.update_cell(10,5, patient_one_populate[14])

    sheet.update_cell(11,1, patient_one_populate[15])
    sheet.update_cell(11,2, patient_one_populate[16])
    sheet.update_cell(11,3, patient_one_populate[17])
    sheet.update_cell(11,4, patient_one_populate[18])
    sheet.update_cell(11,5, patient_one_populate[19])

    sheet.update_cell(12,1, patient_one_populate[20])
    sheet.update_cell(12,2, patient_one_populate[21])

    sheet.update_cell(13,1, patient_one_populate[22])
    sheet.update_cell(13,2, patient_one_populate[23])
    sheet.update_cell(13,3, patient_one_populate[24])
    sheet.update_cell(13,4, patient_one_populate[25])
    sheet.update_cell(13,5, patient_one_populate[26])

    sheet.update_cell(14,1, patient_one_populate[27])
    sheet.update_cell(14,2, patient_one_populate[28])




