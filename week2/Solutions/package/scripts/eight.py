#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
from math import pi

t = Twist()

def move():
    while True:
        start_time = time.time()
        while(time.time() - start_time < 7.5*pi):
            t.linear.x = 0.2
            t.angular.z = 0.2
            pub.publish(t)
        
        while(time.time() - start_time < 7.5*pi + 10):
            t.linear.x = 0.2
            t.angular.z = 0
            pub.publish(t)

        while(time.time() - start_time < 15*pi + 10):
            t.linear.x = 0.2
            t.angular.z = -0.2
            pub.publish(t)

        while(time.time() - start_time < 15*pi + 20):
            t.linear.x = 0.2
            t.angular.z = 0
            pub.publish(t)

rospy.init_node('eight_mover')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)


r = rospy.Rate(10)

while not rospy.is_shutdown():
    start_time = time.time()
    move()
    r.sleep(2)
       