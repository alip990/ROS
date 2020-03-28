#!/usr/bin/env python

import cv2
import numpy as np 
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Pose

import sys
import rospy

bridge = CvBridge()
pub = rospy.Publisher('/color_detect_pose', Pose, queue_size=10)
target_pose=Pose()

x_d=0.0
y_d=0.0
x_d_p=0.0
y_d_p=0.0

def image_callback(ros_img):
    print('got an Image')
    global bridge
    global x_d,y_d, x_d_p, y_d_p

    try:
        img = bridge.imgmsg_to_cv2(ros_img, 'bgr8')
    except CvBridgeError as e:
        print(e)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    blue_lower=np.array([97,94,0],np.uint8)
    blue_upper=np.array([255,255,153],np.uint8)
    blue=cv2.inRange(hsv,blue_lower,blue_upper)
    kernal = np.ones((5 ,5), "uint8")
    blue=cv2.dilate(blue,kernal)
    (_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours)>0:
        contour= max(contours,key=cv2.contourArea)
	area = cv2.contourArea(contour)
	print("area",area)
        if area>2000:
            x,y,w,h = cv2.boundingRect(contour)
	    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    #img=cv2.circle(img,((2*x+w)/2,(2*y+h)/2),5,(255,0,0),-1)
	    img=cv2.line(img,(260,68),((2*x+w)/2,(2*y+h)/2),(0,255,0),2)
            x_d= (((2*y+h)/2)-68) * 0.06
	    y_d= (((2*x+w)/2)-260) * 0.075
	    s= 'x_d:'+ str(x_d)+ 'y_d:'+str(y_d)
            cv2.putText(img,s,(x-20,y-5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),1,cv2.LINE_AA)
            if (abs(x_d-x_d_p)> 1 or abs(y_d-y_d_p)>1):
                target_pose.position.x=x_d*0.01
		target_pose.position.y=y_d*0.01
		target_pose.position.z=0.0
		pub.publish(target_pose)	
		x_d_p=x_d
		y_d_p=y_d
    cv2.imshow("Mask",blue)
    cv2.imshow("Color Tracking",img)
    cv2.waitKey(3) 

def main(a):
    rospy.init_node('color_obj_track', anonymous=True)
    img_subcriber = rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('Shutting down')
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)

