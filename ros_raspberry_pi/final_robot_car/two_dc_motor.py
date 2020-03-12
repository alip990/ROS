#!/usr/bin/env python
import RPi.GPIO as gpio
import time
from time import sleep
import sys
import signal
import rospy
from std_msgs.msg import Float32
import RPi.GPIO as GPIO
from time import sleep


class Motion_vector():
    def __init__(self):
        
        GPIO.setmode(GPIO.BOARD)

        self.Motor1A = 10
        self.Motor1B = 12
        self.Motor1E = 8

        self.Motor2A = 24
        self.Motor2B = 26
        self.Motor2E = 22

        GPIO.setup(self.Motor1A,GPIO.OUT)
        GPIO.setup(self.Motor1B,GPIO.OUT)
        GPIO.setup(self.Motor1E,GPIO.OUT)

        GPIO.setup(self.Motor2A,GPIO.OUT)
        GPIO.setup(self.Motor2B,GPIO.OUT)
        GPIO.setup(self.Motor2E,GPIO.OUT)
    def forword(self):
        print("Going forword")
        GPIO.output(self.Motor1A,GPIO.HIGH)
        GPIO.output(self.Motor1B,GPIO.LOW)
        GPIO.output(self.Motor1E,GPIO.HIGH)

        GPIO.output(self.Motor2A,GPIO.HIGH)
        GPIO.output(self.Motor2B,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.HIGH)
        
    def backword(self):
        GPIO.output(self.Motor1A,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.HIGH)
        GPIO.output(self.Motor1E,GPIO.HIGH)

        GPIO.output(self.Motor2A,GPIO.LOW)
        GPIO.output(self.Motor2B,GPIO.HIGH)
        GPIO.output(self.Motor2E,GPIO.HIGH)
    def left(self):
        print("Going forword")
        GPIO.output(self.Motor1A,GPIO.HIGH)
        GPIO.output(self.Motor1B,GPIO.LOW)
        GPIO.output(self.Motor1E,GPIO.HIGH)
        
        GPIO.output(self.Motor2A,GPIO.LOW)
        GPIO.output(self.Motor2B,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.LOW)
        
    def right(self):
        print("Going forword")
        GPIO.output(self.Motor1A,GPIO.LOW)
        GPIO.output(self.Motor1B,GPIO.LOW)
        GPIO.output(self.Motor1E,GPIO.LOW)

        GPIO.output(self.Motor2A,GPIO.HIGH)
        GPIO.output(self.Motor2B,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.HIGH)
    def all_stop(self):
        print("All stop")
        GPIO.output(self.Motor1E,GPIO.LOW)
        GPIO.output(self.Motor2E,GPIO.LOW)

m_v = Motion_vector()

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Sonar data %s", data.data)
    if data.data > 18.2:
        m_v.forword()
    if data.data < 18.2:
        m_v.all_stop()
       
        
def sonar_motor():
    rospy.init_node('two_dc_motor', anonymous=True)
    p = rospy.Subscriber('/sonar_dist', Float32, callback)
    
    rospy.spin()
if __name__ == '__main__':
    sonar_motor()


