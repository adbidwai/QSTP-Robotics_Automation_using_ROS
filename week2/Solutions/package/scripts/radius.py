#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32

rospy.init_node('radius_publisher')
pub = rospy.Publisher('/radius', Float32, queue_size=1)

rate = rospy.Rate(2)
radius = 1.0

while not rospy.is_shutdown():
    pub.publish(radius)
    rate.sleep()