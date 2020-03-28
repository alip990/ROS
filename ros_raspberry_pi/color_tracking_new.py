#!/usr/bin/env python

import cv2
import numpy as np 
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Pose
import imutils
import sys
import rospy
from collections import deque
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,help="max buffer size")
args = vars(ap.parse_args())

bridge = CvBridge()

pts = deque(maxlen=args["buffer"])

def image_callback(ros_img):
    print('got an Image')
    global bridge, pts
    try:
        img = bridge.imgmsg_to_cv2(ros_img, 'bgr8')
    except CvBridgeError as e:
        print(e)

    #img = cv2.resize(img, (720,720), interpolation = cv2.INTER_AREA)
    blurred = cv2.GaussianBlur(img, (11, 11), 0)
    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    blue_lower=np.array([92,95,0],np.uint8)
    blue_upper=np.array([144,255,122],np.uint8)
    mask=cv2.inRange(hsv,blue_lower,blue_upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    (_,contours,hierarchy)=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = contours[0]
    center = None
    if len(cnts)>0:
        c = max(cnts, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
	if radius > 10:
	    cv2.circle(img, (int(x), int(y)), int(radius),(0, 255, 255), 2)
	    cv2.circle(img, center, 5, (0, 0, 255), -1)
	pts.appendleft(center)
	for i in range(1, len(pts)):
	    if pts[i - 1] is None or pts[i] is None:
		continue
		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(img, pts[i - 1], pts[i], (0, 0, 255), thickness)

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

