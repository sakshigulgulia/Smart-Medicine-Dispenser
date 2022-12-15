import RPi.GPIO as GPIO
from time import sleep

A_3=10
B_3=9
C_3=11
D_3=8
time = 0.001

GPIO.setmode(GPIO.BCM)
#Motor 1
GPIO.setup(A_3,GPIO.OUT)
GPIO.setup(B_3,GPIO.OUT)
GPIO.setup(C_3,GPIO.OUT)
GPIO.setup(D_3,GPIO.OUT)
GPIO.output(A_3, False)
GPIO.output(B_3, False)
GPIO.output(C_3, False)
GPIO.output(D_3, False)

# driving the motor 1
def Step1():
    GPIO.output(D_3, True)
    sleep (time)
    GPIO.output(D_3, False)
 
def Step2():
    GPIO.output(D_3, True)
    GPIO.output(C_3, True)
    sleep (time)
    GPIO.output(D_3, False)
    GPIO.output(C_3, False)

def Step3():
    GPIO.output(C_3, True)
    sleep (time)
    GPIO.output(C_3, False)
 
def Step4():
    GPIO.output(B_3, True)
    GPIO.output(C_3, True)
    sleep (time)
    GPIO.output(B_3, False)
    GPIO.output(C_3, False)

def Step5():
    GPIO.output(B_3, True)
    sleep (time)
    GPIO.output(B_3, False)

def Step6():
    GPIO.output(A_3, True)
    GPIO.output(B_3, True)
    sleep (time)
    GPIO.output(A_3, False)
    GPIO.output(B_3, False)

def Step7():
    GPIO.output(A_3, True)
    sleep (time)
    GPIO.output(A_3, False)

def Step8():
    GPIO.output(D_3, True)
    GPIO.output(A_3, True)
    sleep (time)
    GPIO.output(D_3, False)
    GPIO.output(A_3, False)
 
def motor_control_three():
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
