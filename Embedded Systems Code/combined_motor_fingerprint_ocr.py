from time import sleep
import signal, sys
import RPi.GPIO as GPIO
import pytz, datetime
from motor_control_1 import motor_control_one
from motor_control_2 import motor_control_two
from motor_control_3 import motor_control_three
from motor_control_4 import motor_control_four
from Fingerprint_Sensor import *
from easy_ocr import *


global pill_one_count, pill_two_count, pill_three_count, pill_four_count
#patient 1
pill_one_count = 7
pill_two_count = 7

#patient 2
pill_three_count = 7
pill_four_count = 7

global pill_one_dispense, pill_two_dispense, pill_three_dispense, pill_four_dispense
#dispense_time = [8-11, 12-15, 16-19, 20-23]
buzzer_flag = 0
#Time Variables
time_zone = pytz.timezone("US/Eastern")



# Non-Motor Pins PIN-Assignment
button = 16
piezo = 13
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(piezo,GPIO.OUT)
piezo_pwm = GPIO.PWM(piezo, 1000)
piezo_pwm.start(0)#Initilize duty as 0

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
    

def dispense_pill(button):
    piezo_pwm.ChangeDutyCycle(0)
    global buzzer_flag
    if buzzer_flag:
        buzzer_flag = 0
    global pill_one_count, pill_two_count, pill_three_count, pill_four_count
    
    if len(list_of_patients) == 2:
        if (list_of_patients[0].pill_one_dispense or list_of_patients[0].pill_two_dispense) and (list_of_patients[1].pill_one_dispense or list_of_patients[1].pill_two_dispense):
            count = 0
            while (count < 2):
                while get_fingerprint():
                    if finger.finger_id == list_of_patients[0].finger_id:
                        i = 0
                    elif finger.finger_id == list_of_patients[1].finger_id:
                        i = 1
                    else:
                        print("You are not authorized!")
                        break
                    print("Welcome ", list_of_patients[i].patient_name)
                    if list_of_patients[i].pill_one_dispense:
                        print("Take your pill, ", list_of_patients[i].patient_name)
                        motor_control_one()
                        list_of_patients[i].pill_one_dispense = 0
                        pill_one_count-=1
                        print("Remaining Count of %s is %d", list_of_patients[i].pill_one_name, pill_one_count)
                    if list_of_patients[i].pill_two_dispense:
                        print("Take your pill, ", list_of_patients[i].patient_name)
                        motor_control_one()
                        list_of_patients[i].pill_two_dispense = 0
                        pill_two_count-=1
                        print("Remaining Count of %s is %d", list_of_patients[i].pill_two_name, pill_two_count)
                    if (not list_of_patients[i].pill_one_dispense or not list_of_patients[i].pill_two_dispense):
                        break
                count += 1

    for n in range(len(list_of_patients)):
        if list_of_patients[n].pill_one_dispense or list_of_patients[n].pill_two_dispense:
            while get_fingerprint():
                if finger.finger_id == list_of_patients[n].finger_id:
                    print("Welcome ", list_of_patients[n].patient_name)
                    if list_of_patients[n].pill_one_dispense:
                        print("Take your pill, ", list_of_patients[n].patient_name)
                        motor_control_one()
                        list_of_patients[n].pill_one_dispense = 0
                        pill_one_count-=1
                        print("Remaining Count of %s is %d", list_of_patients[n].pill_one_name, pill_one_count)
                    if list_of_patients[n].pill_two_dispense:
                        print("Take your pill, ", list_of_patients[n].patient_name)
                        motor_control_one()
                        list_of_patients[n].pill_two_dispense = 0
                        pill_two_count-=1
                        print("Remaining Count of %s is %d", list_of_patients[n].pill_two_name, pill_two_count)
                    if (not list_of_patients[n].pill_one_dispense or not list_of_patients[n].pill_two_dispense):
                        break
                else:
                    print("You are not authorized!")
                    break


    
def buzzer(piezo_pwm):
    global buzzer_flag
    print("Time to take the Pill!")
    piezo_pwm.ChangeDutyCycle(50)
    buzzer_flag = 1
    
    
GPIO.add_event_detect(button, GPIO.FALLING, callback=dispense_pill, bouncetime=100)
while True:
    try:
        t_time = datetime.datetime.now(tz=time_zone)
        current_time = list(t_time.timetuple())
        #print(list(t_time.timetuple()))
        #for n in len(list_of_patients):
        n = 0
        if(any(list_of_patients[n].pill_one_times) and not list_of_patients[n].recent_dispense):
            for i in range(len(list_of_patients[n].pill_one_times)):
                print(i)
                if i == 0 and list_of_patients[n].pill_one_times[i] == 1:
                    if current_time[3] >= 8 and current_time[3] < 11:
                        list_of_patients[n].pill_one_dispense = 1
                if i == 1 and list_of_patients[n].pill_one_times[i] == 1:
                    if current_time[3] >= 12 and current_time[3] < 15:
                        list_of_patients[n].pill_one_dispense = 1
                if i == 2 and list_of_patients[n].pill_one_times[i] == 1:
                    if current_time[3] >= 16 and current_time[3] < 19:
                        list_of_patients[n].pill_one_dispense = 1
                if i == 3 and list_of_patients[n].pill_one_times[i] == 1:
                    if current_time[3] > 20 and current_time[3] < 23:
                        list_of_patients[n].pill_one_dispense = 1
                #else:
                 #   print("Something went wrong!")
        
        if(any(list_of_patients[n].pill_two_times) and not list_of_patients[n].recent_dispense):
            for i in range(len(list_of_patients[n].pill_two_times)):              
                if i == 0 and list_of_patients[n].pill_two_times[i] == 1:
                    if current_time[3] >= 2 and current_time[3] < 11:
                        list_of_patients[n].pill_two_dispense = 1
                if i == 1 and list_of_patients[n].pill_two_times[i] == 1:
                    if current_time[3] >= 12 and current_time[3] < 15:
                        list_of_patients[n].pill_two_dispense = 1
                if i == 2 and list_of_patients[n].pill_two_times[i] == 1:
                    if current_time[3] >= 16 and current_time[3] < 19:
                        list_of_patients[n].pill_two_dispense = 1
                if i == 3 and list_of_patients[n].pill_two_times[i] == 1:
                    if current_time[3] > 20 and current_time[3] < 23:
                        list_of_patients[n].pill_two_dispense = 1
                #else:
                 #   print("Something went wrong!")
    
        if(list_of_patients[n].pill_one_dispense or list_of_patients[n].pill_two_dispense):
            buzzer(piezo_pwm)
        if not buzzer_flag:
            piezo_pwm.ChangeDutyCycle(0)    
            print("hello")
        
        sleep(1)

    except IndexError:
        continue
    except OSError:
        break
            
GPIO.cleanup()
    
