#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose
import sys
import rospy
import serial
Myserial = serial.Serial('/dev/ttyACM0',9600)
def callback(data):
    global Myserial
    if (data.position.x and data.position.y) > 0:
        Myserial.write(str.encode('F'))
    if (data.position.y) < 0:
        Myserial.write(str.encode('B'))
def listener_cmd_vel():
    rospy.init_node('listener_cmd_vel', anonymous=True)
    rospy.Subscriber('/color_detect_pose',Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    listener_cmd_vel()
