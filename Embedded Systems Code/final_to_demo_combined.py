import sys
from Fingerprint_Sensor import enroll_finger
from Fingerprint_Sensor import get_num

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from time import sleep
import signal
import RPi.GPIO as GPIO
import pytz, datetime

from motor_control_1 import motor_control_one
from motor_control_2 import motor_control_two
from motor_control_3 import motor_control_three
from motor_control_4 import motor_control_four
#from Fingerprint_Sensor import get_fingerprint

import board
from digitalio import DigitalInOut, Direction
import adafruit_fingerprint
import serial
from twilio.rest import Client
import requests
#Twilio Account Cred
account_sid = "ACd178e541067c698f6980aea9e6e5539c"
auth_token = "9a8e4c5573bd87ec1cf3c50250ece5cd"

client = Client(account_sid, auth_token)

#Google Sheets
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name("/home/raspi/Desktop/RasPi/iot01-371004-6f1d2fc1f270.json", scopes = scope)

file = gspread.authorize(creds)
workbook = file.open("IoT_Write")
sheet = workbook.sheet1




class Pill:
    #count = 0
    def __init__(self):
        self.pill_status = 1
        self.pill_name = ""
        self.pill_times = [0, 0, 0, 0]
        self.pill_days = 0
        self.pill_dispense = ['0', '0', '0', '0']
        self.pill_count = 0
        self.pill_total = 0
        self.pill_recent_dispense = '0'
        self.count = 0
    
    def pill_set(self, pill_name, pill_times, pill_days):
        if pill_name != "Nil":
            self.pill_status = 1
            self.pill_name = pill_name
            self.pill_times = pill_times
            self.pill_days = pill_days
            self.pill_dispense = ['0', '0', '0', '0']
            self.pill_count = 7
            for i in range(4):
                if self.pill_times[i] == '1':
                    self.count = self.count + int(self.pill_days)
            self.pill_total = self.count
            print(self.pill_total)
            
            

class Patient:

    def __init__(self):
        self.pill_one = Pill()
        self.pill_two = Pill()

    def initialize(self, patient_id, name, hospital_name, doctor_name, patient_finger_id):
        self.status = '1'
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
            

def read_patient_one_data(patient_one_populate):
    patient_one_populate[10] = sheet.cell(6,2).value
    patient_one_populate[8] = sheet.cell(5,2).value
    patient_one_populate[2] = sheet.cell(1,2).value
    patient_one_populate[4] = sheet.cell(2,2).value

    if sheet.cell(11,2).value != 'Nil':
        patient_one_populate[17] = '1'
    else:
        patient_one_populate[17] = '0'

    if sheet.cell(11,3).value != 'Nil':
        patient_one_populate[18] = '1'
    else:
        patient_one_populate[18] = '0'

    if sheet.cell(11,4).value != 'Nil':
        patient_one_populate[19] = '1'
    else:
        patient_one_populate[19] = '0'

    if sheet.cell(11,5).value != 'Nil':
        patient_one_populate[20] = '1'
    else:
        patient_one_populate[20] = '0'

    patient_one_populate[16] = sheet.cell(11,1).value #Pill 1 Name
    patient_one_populate[27] = sheet.cell(12,2).value #Pill 1 Days

    if sheet.cell(13,2).value != 'Nil':
        patient_one_populate[22] = '1'
    else:
        patient_one_populate[22] = '0'

    if sheet.cell(13,3).value != 'Nil':
        patient_one_populate[23] = '1'
    else:
        patient_one_populate[23] = '0'

    if sheet.cell(13,4).value != 'Nil':
        patient_one_populate[24] = '1'
    else:
        patient_one_populate[24] = '0'

    if sheet.cell(13,5).value != 'Nil':
        patient_one_populate[25] = '1'
    else:
        patient_one_populate[25] = '0'

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
        patient_two_populate[17] = '1'
    else:
        patient_two_populate[17] = '0'

    if sheet.cell(11,9).value != 'Nil':
        patient_two_populate[18] = '1'
    else:
        patient_two_populate[18] = '0'

    if sheet.cell(11,10).value != 'Nil':
        patient_two_populate[19] = '1'
    else:
        patient_two_populate[19] = '0'

    if sheet.cell(11,11).value != 'Nil':
        patient_two_populate[20] = '1'
    else:
        patient_two_populate[20] = '0'

    patient_two_populate[16] = sheet.cell(11,7).value #Pill 1 name
    patient_two_populate[26] = sheet.cell(12,8).value #Pill 1 days

    if sheet.cell(13,8).value != 'Nil':
        patient_two_populate[22] = '1'
    else:
        patient_two_populate[22] = '0'

    if sheet.cell(13,9).value != 'Nil':
        patient_two_populate[23] = '1'
    else:
        patient_two_populate[23] = '0'

    if sheet.cell(13,10).value != 'Nil':
        patient_two_populate[24] = '1'
    else:
        patient_two_populate[24] = '0'

    if sheet.cell(13,11).value != 'Nil':
        patient_two_populate[25] = '1'
    else:
        patient_two_populate[25] = '0'

    patient_two_populate[21] = sheet.cell(13,7).value #Pill 2 name
    patient_two_populate[27] = sheet.cell(14,8).value #Pill 2 days
    print(patient_two_populate)
    return patient_two_populate



x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
patient_one_temp = x
patient_two_temp = y


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
    patient_finger_id = get_num()
    enroll_finger(patient_finger_id)
    list_of_patients[0].initialize(patient_one_populate[10], patient_one_populate[8], patient_one_populate[2], patient_one_populate[4], patient_finger_id)
    pill_one_times_list = [patient_one_populate[17], patient_one_populate[18], patient_one_populate[19], patient_one_populate[20]]
    list_of_patients[0].populate(1, patient_one_populate[16], pill_one_times_list, patient_one_populate[26])
    pill_two_times_list = [patient_one_populate[22], patient_one_populate[23], patient_one_populate[24], patient_one_populate[25]]
    list_of_patients[0].populate(2, patient_one_populate[21], pill_two_times_list, patient_one_populate[27])
    print(list_of_patients[0])
    print("Welcome Patient 2....")
    print("Enroll your fingerprint for security")
    patient_finger_id = get_num()
    enroll_finger(patient_finger_id)
    list_of_patients[1].initialize(patient_two_populate[10], patient_two_populate[8], patient_two_populate[2], patient_two_populate[4], patient_finger_id)
    pill_one_times_list = [patient_two_populate[17], patient_two_populate[18], patient_two_populate[19], patient_two_populate[20]]
    list_of_patients[1].populate(1, patient_two_populate[16], pill_one_times_list, patient_two_populate[26])
    pill_two_times_list = [patient_two_populate[22], patient_two_populate[23], patient_two_populate[24], patient_two_populate[25]]
    list_of_patients[1].populate(2, patient_two_populate[21], pill_two_times_list, patient_two_populate[27])
    print(list_of_patients[1])



GPIO.setwarnings(False)
uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)
#dispense_time = [8-11, 12-15, 16-19, 20-23]



#Pill Dispense Tracking
#Time Variables
time_zone = pytz.timezone("US/Eastern")
t = datetime.datetime.now(tz=time_zone)
dispense_track_time = list(t.timetuple())


# Non-Motor Pins PIN-Assignment
button = 16
piezo = 13
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(piezo,GPIO.OUT)
piezo_pwm = GPIO.PWM(piezo, 5000)
piezo_pwm.start(0)#Initilize duty as 0



def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
    

def get_fingerprint():
    """Get a finger print image, template it, and see if it matches!"""
    print("Waiting for image...")
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    print("Templating...")
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        
        return False
    print("Searching...")
    if finger.finger_search() != adafruit_fingerprint.OK:
        print("Finger Not Found!")
        return False
    return True

def dispense_pill(list_of_patients):
    print("Button pressed - interrupt")
    #piezo_pwm.ChangeFrequency(1)
    piezo_pwm.ChangeDutyCycle(0)
    
    global finger

    
    if len(list_of_patients) == 2:
        print("line 48")
        if (any(list_of_patients[0].pill_one.pill_dispense) or any(list_of_patients[0].pill_two.pill_dispense)) and (any(list_of_patients[1].pill_one.pill_dispense) or any(list_of_patients[1].pill_two.pill_dispense)):
            count = 0
            print("both patients pills")
            while (count < 2):
                print("line72")
                while True:
                    if get_fingerprint():
                        print("Reading Fingerprint...")
                        if finger.finger_id == list_of_patients[0].finger_id:
                            i = 0
                        elif finger.finger_id == list_of_patients[1].finger_id:
                            i = 1
                        print("Welcome ", list_of_patients[i].patient_name)
                        for index in range(len(list_of_patients[i].pill_one.pill_dispense)):
                            if list_of_patients[i].pill_one.pill_recent_dispense == '0':
                                if list_of_patients[i].pill_one.pill_dispense[index] == '1':
                                    print("line85")
                                    print("Take your pill, ", list_of_patients[i].patient_name)
                                    if i == 0:
                                        motor_control_one()
                                    elif i == 1:
                                        motor_control_three()
                                    list_of_patients[i].pill_one.pill_dispense[index] = '0'
                                    list_of_patients[i].pill_one.pill_count -= 1
                                    list_of_patients[i].pill_one.pill_total -= 1
                                    list_of_patients[i].pill_one.pill_recent_dispense = '1'
                                    print("Remaining Count of " + str(list_of_patients[i].pill_one.pill_name) +" in dispenser is " + str(list_of_patients[i].pill_one.pill_count))
                                    break
                            else:
                                print("You have already received the Pill ", list_of_patients[i].patient_name)
                        for index in range(len(list_of_patients[i].pill_two.pill_dispense)):
                            if list_of_patients[i].pill_two.pill_recent_dispense == '0':
                                if list_of_patients[i].pill_two.pill_dispense[index] == '1':
                                    print("line97")
                                    print("Take your pill, ", list_of_patients[i].patient_name)
                                    if i == 0:
                                        motor_control_two()
                                    elif i == 1:
                                        motor_control_four()
                                    list_of_patients[i].pill_two.pill_dispense[index] = '0'
                                    list_of_patients[i].pill_two.pill_count -= 1
                                    list_of_patients[i].pill_two.pill_total -= 1
                                    list_of_patients[i].pill_two.pill_recent_dispense = '1'
                                    print("Remaining Count of " + str(list_of_patients[i].pill_two.pill_name) + " in dispenser is " + str(list_of_patients[i].pill_two.pill_count))
                                    break
                            else:
                                print("You have already received the Pill ", list_of_patients[i].patient_name)
                        #count_1 = 0
                        #count_2 = 0
                        if ((not any(list_of_patients[i].pill_one.pill_dispense) == '1') and (not any(list_of_patients[i].pill_two.pill_dispense) == '1')):
                            print("while true")
                            break
                count += 1

    elif (len(list_of_patients) >= 1) :
        for n in range(len(list_of_patients)):
            print("line91")
            for index in range(4):
                if ((list_of_patients[n].pill_one.pill_dispense[index]) == '1' or (list_of_patients[n].pill_two.pill_dispense[index] == '1')):
                    if get_fingerprint():
                        if finger.finger_id == list_of_patients[n].finger_id:
                            print("Welcome ", list_of_patients[n].patient_name)

                            if list_of_patients[n].pill_one.pill_dispense[index] == '1':
                                print("Take your pill, ", list_of_patients[n].patient_name)
                                if n == 0:
                                    motor_control_one()
                                elif n == 1:
                                    motor_control_three()
                                list_of_patients[n].pill_one.pill_dispense[index] = '0'
                                list_of_patients[n].pill_one.pill_count -= 1
                                list_of_patients[n].pill_one.pill_total -= 1
                                list_of_patients[n].pill_one.pill_recent_dispense = '1'
                                print("Remaining Count of %s is %d", list_of_patients[n].pill_two.pill_name, list_of_patients[n].pill_two.pill_count)
                            
                            if list_of_patients[n].pill_two.pill_dispense[index] == '1':
                                print("Take your pill, ", list_of_patients[n].patient_name)
                                if n == 0:
                                    motor_control_two()
                                elif n == 1:
                                    motor_control_four()
                                list_of_patients[n].pill_two.pill_dispense[index] = '0'
                                list_of_patients[n].pill_two.pill_count -= 1
                                list_of_patients[n].pill_two.pill_total -= 1
                                list_of_patients[n].pill_two.pill_recent_dispense = '1'
                                print("Remaining Count of %s is %d", list_of_patients[n].pill_two.pill_name, list_of_patients[n].pill_two.pill_count)
                            
                            if (not list_of_patients[n].pill_one.pill_dispense[index] or not list_of_patients[n].pill_two.pill_dispense[index]):
                                break
                        else:
                            print("You are not authorized!")
                            break
    queries = {"api_key": "0KKK3VB4GKNVPQQF",
               "field1": list_of_patients[0].pill_one.pill_total,
               "field2": list_of_patients[0].pill_two.pill_total,
               "field3": list_of_patients[1].pill_two.pill_total,
               "field4": list_of_patients[1].pill_two.pill_total}
    r = requests.get('https://api.thingspeak.com/update', params=queries)
    if r.status_code == requests.codes.ok:
        print("Data Received!")
    else:
        print("Error Code: " + str(r.status_code))

    return list_of_patients
    
def buzzer():
    print("buzzerrrrrr")
    global piezo_pwm
    piezo_pwm.ChangeDutyCycle(50)
    for i in range(100000000):
        pass
    piezo_pwm.ChangeDutyCycle(0)
    
    
if __name__ == "__main__":
    while True:
        try:
            t_time = datetime.datetime.now(tz=time_zone)
            current_time = list(t_time.timetuple())
            #print(list(t_time.timetuple()))
            for n in range(len(list_of_patients)):
                #n = 0
                if(any(list_of_patients[n].pill_one.pill_times) and (list_of_patients[n].pill_one.pill_recent_dispense == '0')):
                    print("recent one flag reset")
                    print(list_of_patients[n].pill_one.pill_recent_dispense)
                    for i in range(len(list_of_patients[n].pill_one.pill_times)):
                        #print(i)
                        if i == 0 and list_of_patients[n].pill_one.pill_times[i] == '1':
                            if current_time[3] == 14: #and current_time[4] == 0 and current_time[5] == 0:
                                list_of_patients[n].pill_one.pill_dispense[i] = '1'
                                index = i
                        if i == 1 and list_of_patients[n].pill_one.pill_times[i] == '1':
                            if current_time[3] == 13 and current_time[4] == 0 and current_time[5] == 0:
                                list_of_patients[n].pill_one.pill_dispense[i] = '1'
                                index = i
                        if i == 2 and list_of_patients[n].pill_one.pill_times[i] == '1':
                            if current_time[3] == 17 and current_time[4] == 0 and current_time[5] == 0:
                                list_of_patients[n].pill_one.pill_dispense[i] = '1'
                                index = i
                        if i == 3 and list_of_patients[n].pill_one.pill_times[i] == '1':
                            if current_time[3] == 21 and current_time[4] == 0 and current_time[5] == 0:
                                list_of_patients[n].pill_one.pill_dispense[i] = '1'
                                index = i
                        else:
                            pass
                            #print("Something went wrong 0")
                
                if(any(list_of_patients[n].pill_two.pill_times) and (list_of_patients[n].pill_two.pill_recent_dispense == '0')):
                    print("recent two flag reset")
                    print(list_of_patients[n].pill_two.pill_recent_dispense)
                    for i in range(len(list_of_patients[n].pill_two.pill_times)):              
                        if i == 0 and list_of_patients[n].pill_two.pill_times[i] == '1':
                            if current_time[3] == 14: #and current_time[4] == 0 and current_time[5] == 0:
                                list_of_patients[n].pill_two.pill_dispense[i] = '1'
                        if i == 1 and list_of_patients[n].pill_two.pill_times[i] == '1':
                            if current_time[3] == 13 and current_time[4] == 0 and current_time[5] == 0:
                                list_of_patients[n].pill_two.pill_dispense[i] = '1'
                        if i == 2 and list_of_patients[n].pill_two.pill_times[i] == '1':
                            if current_time[3] == 17 and current_time[4] == 0 and current_time[5] == 0:
                                list_of_patients[n].pill_two.pill_dispense[i] = '1'
                        if i == 3 and list_of_patients[n].pill_two.pill_times[i] == '1':
                            if current_time[3] == 21 and current_time[4] == 0 and current_time[5] == 0:
                                list_of_patients[n].pill_two.pill_dispense[i] = '1'
                        else:
                            pass
                            #print("Something went wrong 1")
            
            if('1' in list_of_patients[0].pill_one.pill_dispense or '1' in list_of_patients[0].pill_two.pill_dispense or '1' in list_of_patients[1].pill_one.pill_dispense or '1' in list_of_patients[1].pill_two.pill_dispense):
                buzzer()
                print("buzzer done - waiting")
                if('1' in list_of_patients[0].pill_one.pill_dispense or '1' in list_of_patients[0].pill_two.pill_dispense):
                    msg_body = "Time to take your Pill " + str(list_of_patients[0].patient_name)
                    message = client.api.account.messages.create(
                        to="+16462151374",
                        from_="+12075219831",
                        body = msg_body)
                if('1' in list_of_patients[1].pill_one.pill_dispense or '1' in list_of_patients[1].pill_two.pill_dispense):
                    msg_body = "Time to take your Pill " + str(list_of_patients[1].patient_name)
                    message = client.api.account.messages.create(
                        to="+16462151374",
                        from_="+12075219831",
                        body = msg_body)
                GPIO.wait_for_edge(button, GPIO.BOTH)
                if not GPIO.input(button):
                    print("ButtonPressed......")
                    list_of_patients = dispense_pill(list_of_patients)
                    print(list_of_patients[0].pill_one.pill_dispense)
                    print(list_of_patients[0].pill_two.pill_dispense)
                    print(list_of_patients[1].pill_one.pill_dispense)
                    print(list_of_patients[1].pill_two.pill_dispense)

            
            sleep(1)

        except IndexError:
            continue
        except OSError:
            break
                
    GPIO.cleanup()

