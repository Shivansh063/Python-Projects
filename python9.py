#!/usr/bin/env  python


import webbrowser
import time
import sys
import requests
import bs4


data = sys.argv[1:3]

n1 = data[0]
n2 = data[1]
 
n1,n2 = n2,n1
print "Please wait until swapping is done" 
time.sleep(2)


print n1
print n2

n3 = n1+" "+n2

res = requests.get('http://google.com/search?btnG=1&q=%s'%n3)

soup = bs4.BeautifulSoup(res.text, 'lxml')

for i in soup.select('.r') :
	print (i.text) 

