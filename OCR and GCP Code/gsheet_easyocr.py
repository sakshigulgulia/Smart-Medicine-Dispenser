import easyocr, sys, os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from populateprescription1 import *
from populateprescription2 import *

reader = easyocr.Reader(['en']) # this needs to run only once to load the model into$
print("Load Library Done...")

dir = sys.argv[1]
print(dir)
f = os.listdir(dir)
print(f)
file = ["0","0"]
for i in range(len(f)):
    print(i)
    file[i] = dir+"/"+f[i]
    print(file[i])

try:
    patient_one_populate = reader.readtext(file[0], detail=0)
    print(patient_one_populate)
    sheet_update_patient_one(patient_one_populate)

    patient_two_populate = reader.readtext(file[1], detail=0)
    print(patient_two_populate)
    sheet_update_patient_two(patient_two_populate)

except IndexError:
    print("IndexError")
    pass
except ValueError:
    print("ValueError: Incorrect Image Format")
    pass