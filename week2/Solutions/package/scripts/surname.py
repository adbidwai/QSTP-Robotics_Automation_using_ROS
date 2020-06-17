#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('surname')
pub = rospy.Publisher('/surname', String, queue_size=1)

rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish('Swamy')
    rate.sleep()