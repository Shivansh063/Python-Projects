#!usr/bin/pyhton

import sys
import time
import webbrowser



data= sys.argv[1: ]
n1= data[0]
n2= data[1]

print ("please until two name swap")

time.sleep(1)

n1,n2= n2,n1


print n1
print n2


n3 = n1 + " " + n2

webbrowser.open_new_tab('http://www.google.com/search?tbm=isch&q=%s'%n3)
 













