#!/usr/bin/env python
import sys
import rospy
from week2.srv import AngularVelocity
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

def callback(msg):
    r = msg.data
    rospy.wait_for_service('compute_ang_vel')
    
    try:
        calc = rospy.ServiceProxy('compute_ang_vel',AngularVelocity)
        res = calc(r)
        print('Received angular velocity as %s'%res.vel)
        ang_vel = res.vel
        rate = rospy.Rate(15)
        while not rospy.is_shutdown():
            t = Twist()
            t.linear.x = 0.2
            t.angular.z = ang_vel
            pub.publish(t)
            rate.sleep()
        

    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def setup():

    sub = rospy.Subscriber('/radius', Float32, callback)
    rospy.spin()
   



if __name__ == "__main__":
    rospy.init_node('subscriber')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    try:
        setup()
    except Exception as e:
        print('%s error was thrown'%e)    