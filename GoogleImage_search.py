#!usr/bin/pyhton
# Importing Required Libraries

import sys
import time
import webbrowser

# Storing information into variable data through command line

data= sys.argv[1: ]
var_1= data[0]
var_2= data[1]

print ("please until two variable swap")

time.sleep(1)
# Swappiing Two Variables
var_1,var_2= var_2,var_1


print var_1
print var_2

# Concating two Strings
result = var_1 + " " + var_2

# google images will open in new tab on topic stored in variable result 
webbrowser.open_new_tab('http://www.google.com/search?tbm=isch&q=%s'%result)
  













