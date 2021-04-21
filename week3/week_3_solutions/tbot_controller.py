#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Point
import math
from tf.transformations import euler_from_quaternion, quaternion_from_euler

roll = pitch = yaw = 0.0
x = y = z = 0.0
xf = yf = 0.0

#This function is used get the yaw angle of the turtlbot by subscribing it from /odom
def get_rotation(msg):
	global yaw
	global x, y 
	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y

	orientation_initial = msg.pose.pose.orientation 
	orientation_list = [orientation_initial.x, orientation_initial.y, orientation_initial.z, orientation_initial.w]
	(roll,pitch,yaw) = euler_from_quaternion(orientation_list)

def callback(msg):
	global xf, yf
	xf = msg.x
	yf = msg.y

theta = math.atan2(yf,xf)
distance = math.sqrt(math.pow(xf,2)+math.pow(yf,2))
kP_angular = 0.5
kP_linear = 0.22



rospy.init_node('rotate_robot')
sub = rospy.Subscriber('/odom',Odometry,get_rotation)
sub1 = rospy.Subscriber('/path',Point,callback)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
r = rospy.Rate(10)
a = Twist()

#Function to rotate a robot
def rotating_robot():
	while not rospy.is_shutdown():
		inc_x = xf - x
		inc_y = yf- y
		angle_to_goal = math.atan2(inc_y,inc_x)
		#angle_to_goal = math.atan2(yf,xf) - yaw
		dist_to_goal = math.sqrt(math.pow(inc_x,2)+math.pow(inc_y,2))

		if abs(angle_to_goal - yaw) > 0.1:
			a.linear.x = 0.0
			a.angular.z = kP_angular*abs(angle_to_goal - yaw)
			print('Angle error: {}'.format(angle_to_goal))
		else:
			a.angular.z = 0.0
			if dist_to_goal > 0.1:
				a.linear.x = kP_linear*dist_to_goal
				print('distance error:{}'.format(dist_to_goal))
			else:
				a.linear.x = 0.0
		pub.publish(a)
		r.sleep()


if __name__ == '__main__':
	try:
		rotating_robot()
	except rospy.ROSInterruptException():
		pass
