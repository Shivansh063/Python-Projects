#!/usr/bin/env  python

# Importing required Libraries
import webbrowser
import time
import sys

# Saving data from Command Line in to variable data
data = sys.argv[1:3]

var1= data[0]
var2= data[1]
 
# Swapping the values of two Variables
var1,var2 = var2,var1
print "Please wait until swapping is done" 
time.sleep(2)


print var1
print var2 

# Concating two strings
result = var1+" "+var2

# After Concatination, Particular String will be on google new tab
webbrowser.open_new_tab('http://google.com/search?btnG=1&q=%s'%result)


