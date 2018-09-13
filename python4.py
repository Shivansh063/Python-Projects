#!/usr/bin/env python2

import platform
import commands
import os

   
choice='''
Press  1  to  check your current MAC  address  : 
Press  2  to  check total amount to RAM and  CPU   :   
Press  3  to  check your current OS type and OS name  :
Press  4  to check your internet connection   :  
Press  5  to  close your internet connection if it is running  : 
Press  6  to  check your current date and time  :
Press  7  to  logout your system   :  
Press  8  to  Turn off everyone's internet in your current network  : 
'''

print choice 
x=raw_input("Enter your Choice : ")
y=int(x)

if  y == 1 : 
	data = commands.getoutput("ifconfig | grep ether")
	print data

if y == 2 :
	print ("Details for Memory Management ...")
	print commands.getoutput("free")
	print ("Total No. of CPU ... ")
	print commands.getoutput("nproc")

if y == 3 :
	print ("Type of Operating System ")
	print commands.getoutput('platform.system()')
	print ("Name of Operating System ")
	print commands.getoutput('platform.uname()')


