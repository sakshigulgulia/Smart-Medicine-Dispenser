import RPi.GPIO as GPIO
from time import sleep

A_4=7
B_4=1
C_4=12
D_4=0
time = 0.001

GPIO.setmode(GPIO.BCM)
#Motor 1
GPIO.setup(A_4,GPIO.OUT)
GPIO.setup(B_4,GPIO.OUT)
GPIO.setup(C_4,GPIO.OUT)
GPIO.setup(D_4,GPIO.OUT)
GPIO.output(A_4, False)
GPIO.output(B_4, False)
GPIO.output(C_4, False)
GPIO.output(D_4, False)

# driving the motor 1
def Step1():
    GPIO.output(D_4, True)
    sleep (time)
    GPIO.output(D_4, False)
 
def Step2():
    GPIO.output(D_4, True)
    GPIO.output(C_4, True)
    sleep (time)
    GPIO.output(D_4, False)
    GPIO.output(C_4, False)

def Step3():
    GPIO.output(C_4, True)
    sleep (time)
    GPIO.output(C_4, False)
 
def Step4():
    GPIO.output(B_4, True)
    GPIO.output(C_4, True)
    sleep (time)
    GPIO.output(B_4, False)
    GPIO.output(C_4, False)

def Step5():
    GPIO.output(B_4, True)
    sleep (time)
    GPIO.output(B_4, False)

def Step6():
    GPIO.output(A_4, True)
    GPIO.output(B_4, True)
    sleep (time)
    GPIO.output(A_4, False)
    GPIO.output(B_4, False)

def Step7():
    GPIO.output(A_4, True)
    sleep (time)
    GPIO.output(A_4, False)

def Step8():
    GPIO.output(D_4, True)
    GPIO.output(A_4, True)
    sleep (time)
    GPIO.output(D_4, False)
    GPIO.output(A_4, False)
 
def motor_control_four():
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
