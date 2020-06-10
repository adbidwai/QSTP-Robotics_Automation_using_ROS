''' The following python code helps the user to convert Coordinates from polar system to Cartesian system, or vice-versa'''

import numpy as np				

def pol2cart(r, theta):         #function for converting polar to cartesian coordinates.
	x = r*np.cos(theta)
	y = r*np.sin(theta)
	return (x,y)

def cart2pol(x, y):             #function for converting cartesian to polar coordinates.
	r = np.sqrt( x**2 + y**2 )
	theta = np.arctan2(y, x)
	return (r,theta)


choice = input("Enter 1 for polar to cartesian conversion, or 2 for cartesian to polar conversion: ")

if choice == '1' :
    r, theta = input("Enter polar coordinates r, theta (will be computed in radian) : ").split()
    print ("Cartesian Coordinates are (x,y) = ",pol2cart(float(r), float(theta)))

elif choice == '2':
    x, y = input("Enter cartesian coordinantes x,y: ").split()
    print ("Polar Coordinates are (r,theta) = ",cart2pol(float(x),float(y))) 
# In case a number other than 1 or 2 is entered
else :                 
    print ("INVALID CHOICE, CHOICE MUST BE 1 OR 2")
