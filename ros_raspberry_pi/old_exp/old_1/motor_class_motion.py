#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
 

class Motion_vector:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.Motor1A = 10
        self.Motor1B = 12
        self.Motor1E = 8
         
        self.Motor2A = 24
        self.Motor2B = 26
        self.Motor2E = 22
