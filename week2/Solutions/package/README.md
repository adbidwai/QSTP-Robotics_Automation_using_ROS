Week2 submission
=================

Folders:
--------
scripts - contains 7 python files
srv - contains service definition file called AngularVelocity.srv
launch - contains a launch file circle.launch which launches server.py, subscriber.py and radius.py . 

Files in scripts:
-----------------
fullname.py, name.py, and surname.py are for the practice question

server.py - the server node of the rosservice
radius.py - publisher node which publishes to the /radius topic
subscriber.py - the node which calls for the service and subscribres to /radius and publishes to /cmd_vel
eight.py - for the bonus question which makes the turtlebot to move in the shape of 8

For running:
------------
For the third question, directly run the launch file circle.launch
For the bonus question, run the python file eight.py

Note:
-----
For the circle question, when I used  linear velocity equal to 1, the bot drifts with each rotation. I have implemented the code with linear velocity equal to 0.2.

Details:
-------
Name: Sushant S
Roll No. 2019AAPS1031G