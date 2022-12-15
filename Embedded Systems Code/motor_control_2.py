import RPi.GPIO as GPIO
from time import sleep

A_2=4
B_2=17
C_2=27
D_2=22
time = 0.001

GPIO.setmode(GPIO.BCM)
#Motor 1
GPIO.setup(A_2,GPIO.OUT)
GPIO.setup(B_2,GPIO.OUT)
GPIO.setup(C_2,GPIO.OUT)
GPIO.setup(D_2,GPIO.OUT)
GPIO.output(A_2, False)
GPIO.output(B_2, False)
GPIO.output(C_2, False)
GPIO.output(D_2, False)

# driving the motor 1
def Step1():
    GPIO.output(D_2, True)
    sleep (time)
    GPIO.output(D_2, False)
 
def Step2():
    GPIO.output(D_2, True)
    GPIO.output(C_2, True)
    sleep (time)
    GPIO.output(D_2, False)
    GPIO.output(C_2, False)

def Step3():
    GPIO.output(C_2, True)
    sleep (time)
    GPIO.output(C_2, False)
 
def Step4():
    GPIO.output(B_2, True)
    GPIO.output(C_2, True)
    sleep (time)
    GPIO.output(B_2, False)
    GPIO.output(C_2, False)

def Step5():
    GPIO.output(B_2, True)
    sleep (time)
    GPIO.output(B_2, False)

def Step6():
    GPIO.output(A_2, True)
    GPIO.output(B_2, True)
    sleep (time)
    GPIO.output(A_2, False)
    GPIO.output(B_2, False)

def Step7():
    GPIO.output(A_2, True)
    sleep (time)
    GPIO.output(A_2, False)

def Step8():
    GPIO.output(D_2, True)
    GPIO.output(A_2, True)
    sleep (time)
    GPIO.output(D_2, False)
    GPIO.output(A_2, False)
 
def motor_control_two():
# start one complete turn
    global count
    for i in range (64):
         Step1()
         Step2()
         Step3()
         Step4()
         Step5()
         Step6()
         Step7()
         Step8()
