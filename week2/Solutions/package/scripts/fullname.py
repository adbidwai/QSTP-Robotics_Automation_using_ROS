#!/usr/bin/env python
import rospy
from std_msgs.msg import String
name = None
surname = None


class Name:
    def __init__(self):
        self.pub = rospy.Publisher('/fullname', String, queue_size=1)
        self.sub1 = rospy.Subscriber('/name', String, self.callback1)
        self.sub2 = rospy.Subscriber('/surname', String, self.callback2)
        self.str = String()
        self.name = None
        self.surname = None
    
    def callback1(self,msg):
        self.name = msg.data
        self.str = str(self.name) + ' ' + str(self.surname)
        self.pub.publish(self.str)

    def callback2(self,msg):
        self.surname = msg.data
        self.str = str(self.name) + ' ' + str(self.surname)
        self.pub.publish(self.str)
        

if __name__ == "__main__":
    rospy.init_node('fullname')
    name = Name()
    rospy.spin()