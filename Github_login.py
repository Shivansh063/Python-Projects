#!/usr/bin/python3

# importing libraries 

from selenium import webdriver 
from time import sleep 
from getpass import getpass
 
# Storing E-mail and Password in variable usr and pwd
 
usr=input('Enter Email Id:')  
pwd=getpass('Enter Password:')  
  
# Using Firefox 
driver = webdriver.Firefox() 
driver.get("https://github.com/login") 
print ("Opened facebook") 
sleep(1) 
  
#Finding element through id 
username_box = driver.find_element_by_id('login_field') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_id('password') 
password_box.send_keys(pwd) 
print ("Password entered") 
  
login_box = driver.find_element_by_name('commit') 
login_box.click() 
  
print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished") 

