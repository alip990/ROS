#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ros_basic_motion_analysis import Motion_vector
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String
from geometry_msgs.msg import Twist
q = Motion_vector()

class ROS_motion:
    def __init__(self):
        rospy.init_node('DC_motor', anonymous=True)
        rospy.Subscriber('/cmd_vel', Twist, self.callback)
    def callback(self,data):
        l = data.linear.x
        a = data.angular.z
        
        if l>0 and a == 0:
            q.forword()
        elif l>0 and a >0:
            q.left()
        elif l > 0 and a < 0:
            q.right()
        elif l < 0 :
            q.backword()
        else:
            q.all_stop()
        
        


# In[ ]:




