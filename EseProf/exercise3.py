from __future__ import print_function

import time
from sr.robot import *

"""
Exercise 3 python script

We start from the solution of the exercise 2
Put the main code after the definition of the functions. The code should make the robot:
	- 1) find and grab the closest silver marker (token)
	- 2) move the marker on the right
	- 3) find and grab the closest golden marker (token)
	- 4) move the marker on the right
	- 5) start again from 1

The method see() of the class Robot returns an object whose attribute info.marker_type may be MARKER_TOKEN_GOLD or MARKER_TOKEN_SILVER,
depending of the type of marker (golden or silver). 
Modify the code of the exercise2 to make the robot:

1- retrieve the distance and the angle of the closest silver marker. If no silver marker is detected, the robot should rotate in order to find a marker.
2- drive the robot towards the marker and grab it
3- move the marker forward and on the right (when done, you can use the method release() of the class Robot in order to release the marker)
4- retrieve the distance and the angle of the closest golden marker. If no golden marker is detected, the robot should rotate in order to find a marker.
5- drive the robot towards the marker and grab it
6- move the marker forward and on the right (when done, you can use the method release() of the class Robot in order to release the marker)
7- start again from 1

	When done, run with:
	$ python run.py exercise3.py

"""



        
        
        
        
        
        
        
        
        
        
        
        
a_th = 2.0
""" float: Threshold for the control of the linear distance"""

d_th = 0.4
""" float: Threshold for the control of the orientation"""

silver = True
""" boolean: variable for letting the robot know if it has to look for a silver or for a golden marker"""

R = Robot()
""" instance of the class Robot"""


def drive(speed, seconds):
    """
    Function for setting a linear velocity

    Args: speed (int): the speed of the wheels
          seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0


def turn(speed, seconds):
    """
    Function for setting an angular velocity

    Args: speed (int): the speed of the wheels
          seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0


def find_silver_token():
    """
    Function to find the closest silver token

    Returns:
        dist (float): distance of the closest silver token (-1 if no silver token is detected)
        rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
    """
    dist = 100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            dist = token.dist
            rot_y = token.rot_y
    if dist == 100:
        return -1, -1
    else:
        return dist, rot_y


def find_golden_token():
    """
    Function to find the closest golden token

    Returns:
        dist (float): distance of the closest golden token (-1 if no golden token is detected)
        rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
    """
    dist = 100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist = token.dist
            rot_y = token.rot_y
    if dist == 100:
        return -1, -1
    else:
        return dist, rot_y


while 1:
	q=135
	t=0
	if silver == True:  
		dist, rot_y = find_silver_token()
		print ("Dist=",dist,"Rot=",rot_y)
		if dist == -1:  
			print("I don't see any token!!")
			turn(+10, 1)
			q=q+10
			t=t+1
		elif dist < d_th:  
			print("Found it!")
			if R.grab():  
				print("Gotcha!")
				turn(20, 2)
				drive(20, 2)
				R.release()
				drive(-20, 2)
				turn(-20, 2)
				silver= not silver
			else:
				print("Aww, I'm not close enough.")
		elif -a_th <= rot_y <= a_th:  
			print("Ah, that'll do.")
			drive(100, 0.1)
		elif rot_y < -a_th:  		
			print("Left a bit...")
			turn(-2, 0.5)
			q=q-2
			t=t+0.5
		elif rot_y > a_th:
			turn(+2, 0.5)
			q=q+2
			t=t+0.5
		dist, rot_y = find_silver_token()
		if dist == -1:  
			print("I don't see any token!!")
			turn(+10, 1)
			q=q+10
			t=t+1
	elif silver == False:	
		dist, rot_y = find_silver_token()
		print ("Dist=",dist,"Rot=",rot_y)
		if dist == -1:  
			print("I don't see any token!!")
			turn(+10, 1)
			q=q+10
			t=t+1
		elif dist < d_th:  
			print("Found it!")
			if R.grab():  
				print("Gotcha!")
				turn(20, 2)
				drive(20, 2)
				R.release()
				drive(-20, 2)
				turn(-20, 2)
				silver= not silver
			else:
				print("Aww, I'm not close enough.")
		elif -a_th <= rot_y <= a_th:  
			print("Ah, that'll do.")
			drive(50, 0.1)
		elif rot_y < -a_th:  		
			print("Left a bit...")
			turn(-2, 0.5)
			q=q-2
			t=t+0.5
		elif rot_y > a_th:
			turn(+2, 0.5)
			q=q+2
			t=t+0.5
		dist, rot_y = find_silver_token()
		if dist == -1:  
			print("I don't see any token!!")
			turn(+10, 1)
			q=q+10
			t=t+1
