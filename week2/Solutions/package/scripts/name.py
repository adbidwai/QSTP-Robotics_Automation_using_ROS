#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('name')
pub = rospy.Publisher('/name', String, queue_size=1)

rate = rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish('Sushant')
    rate.sleep()