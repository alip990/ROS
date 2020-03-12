#!/usr/bin/env python
import RPi.GPIO as gpio
import time
import sys
import signal
import rospy
from std_msgs.msg import Float32
from ros_basic_motion_analysis import Motion_vector

q = Motion_vector()

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Sonar data %s", data.data)


def sonar_motor():
    rospy.init_node('two_dc_motor', anonymous=True)
    rospy.Subscriber('/sonar_dist', Float32, callback)
    rospy.spin()
if __name__ == '__main__':
    sonar_motor()


