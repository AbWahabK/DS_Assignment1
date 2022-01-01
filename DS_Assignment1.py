#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Question1

string = """Twinkle, twinkle, little star,
\tHow I wonder what you are!
\t\tUp above the world so high,
\t\tLike a diamond in the sky.
Twinkle, twinkle, little star,
\tHow I wonder what you are"""

print(string)


# In[5]:


#Question2

from platform import python_version

print(python_version())


# In[14]:


#Question3

import datetime
now = datetime.datetime.now()

print ("Current date : ")
print (now.strftime("%d-%m-%Y"))

print ("\nCurrent time : ")
print (now.strftime("%H:%M"))


# In[17]:


#Question4

area = float(input ("Input the radius of circle : "))

print ("The area of circle is: " + str(3.14 * r**2))


# In[19]:


#Question5

fname = input("Input First Name : ")
lname = input("Input Last Name : ")
print ("Name in Reverse is :  " + lname + " " + fname)


# In[26]:


#Question6
 

#Two Integer inputs
a = int(input("enter first number: "))
b = int(input("enter second number: "))
 
sum = a + b
 
print("sum:", sum)


#Two String inputs
a = str(input("\nenter first input: "))
b = str(input("enter second input: "))
 
sum = a + b
 
print("sum:", sum)


# In[ ]:




