#!/usr/bin/env  python


import webbrowser
import time
import sys
import requests
import bs4

# Storing two arguments from command line 
data = sys.argv[1:3]

var1= data[0]
var2 = data[1]

# Swapping Values of Variables var1, var2
 
var1,var2 = var2,var1
print "Please wait until swapping is done" 
time.sleep(2)


print var1
print var2
# Concating two strings into a Variable
new_var = var1+" "+var2
# Created a requests object by providing a URL
res = requests.get('http://google.com/search?btnG=1&q=%s'%new_var)
# Now BeautifulSoup object is created with two parameters (requests object, type)
soup = bs4.BeautifulSoup(res.text, 'lxml')
#now selecting only data having class='r' and printing into text form
for i in soup.select('.r') :
	print (i.text) 

