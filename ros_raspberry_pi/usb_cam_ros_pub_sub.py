#!/usr/bin/env python

import cv2
import numpy as np 
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
import rospy

bridge = CvBridge()

def image_callback(ros_img):
    print('got an Image')
    global bridge

    try:
        cv_img = bridge.imgmsg_to_cv2(ros_img, 'bgr8')
    except CvBridgeError as e:
        print(e)
    
    #(r,c, ch) = cv_img.shape

    #if c >200 and r >200:
       # cv2.circle(cv_img, (100,100), 90, 255)
    edges = cv2.Canny(cv_img,100,200)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(cv_img, 'Webcam Activated with ROS & OpenCV!',(10, 350), font,1,
    (0,255,0),2, cv2.LINE_AA)
    cv2.imshow("Image", cv_img)
    cv2.imshow("canny", edges)
    cv2.waitKey(3) 

def main(a):

    rospy.init_node('usb_cam_ros_pub_sub', anonymous=True)
    img_subcriber = rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Shutting down')
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
