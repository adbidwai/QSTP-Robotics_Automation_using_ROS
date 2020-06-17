#!/usr/bin/env python
import rospy
from week2.srv import AngularVelocity, AngularVelocityResponse




def handle_ang_vel(req):
    r = req.radius
    ang_vel = 0.2/r
    print('Sending angular velocity equal to %s for radius %s'%(ang_vel,r))
    try:
        return AngularVelocityResponse(ang_vel)
    
    except Exception as e:
        print('%s exception was thrown'%e)





def start_server():
    service = rospy.Service('compute_ang_vel', AngularVelocity, handle_ang_vel)
    print('Initializing server.......Done!')
    rospy.spin()


if __name__ == "__main__":
    rospy.init_node('server_node')
    try:
        start_server()
    except Exception as e:
        print('%s exception was thrown'%e)