#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point

rospy.init_node('path',anonymous=True)
pub = rospy.Publisher('/path',Point,queue_size=10)
r = rospy.Rate(10)
while not rospy.is_shutdown():
	G = Point()
	G.x = 2
	G.y = 2
	pub.publish(G)
	r.sleep()
