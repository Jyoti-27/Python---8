#!/usr/bin/env python
# coding: utf-8

# ## Functions in Python
# - Predefined
# - Userdefined

# In[1]:


list1 = [2, 3, 4, 5]
list1.append(6)
list1


# In[4]:


a = 5 
b = 6
# Create a function to find the sum of a and b
def addition(a,b):
    return a + b
addition(a,b)


# In[2]:


a = 5 
b = 2
# Create a function to find the subtraction of a and b
def subtraction(a,b):
    return a - b
subtraction(a,b)


# #### Write program to find the sum of numbers starting from 1 to 25, 50 to 75 and 90 to 100 using three different for loops

# In[6]:


sum = 0
for i in range(1,26):
    sum = sum + i
print("Sum of integers from 1 to 25 is = ", sum)

    
sum = 0    
for i in range(50,76):
    sum = sum + i
print("Sum of integers from 50 to 75 is = ", sum)

    
sum = 0
for i in range(9,101):
    sum = sum + i
print("Sum of integers from 90 to 100 is = ", sum)
    
    


# - Python Program to check given number is Prime number.

# In[2]:


num = int(input("Enter a number: "))
# Convert string to int 
isDivisible = False;
i = 2;
while i < num:
    if num % i == 0:
        isDivisible = True;
        print("{} is divisible by {}".format(num,i))
    i += 1;
if isDivisible:
    print("{} is not a Prime Number".format(num))
else:
     print("{} is a Prime Number".format(num))
        


# In[10]:


def sum(x,y):
    sum = 0
    for i in range(x,y + 1):
        sum = sum + i
    print('Sum of integers from {} to {} is {}'.format(x,y,sum))
sum(1,25)
sum(50,75)
sum(90,100)
sum(10,45)


# In[12]:


# Write a program to find the square of the function
def square(a):
    return a ** 2
square(5)


# In[19]:


def square(a):
    square = a ** 2
    print("The square of {} is {}".format(a,square))
square(5)


# In[21]:


def squareroot(a):
    squareroot = a ** (1/2)
    print("The squareroot of {} is {}".format(a,squareroot))
squareroot(100)
squareroot(88)


# In[22]:


# Create a function to find square and cube of number.
sq = 1
def sqr(x):
    a = x * x
    b = x * x * x
    return "Square is"+str(a)+"and cube is "+str(b);


# In[30]:


# Create a function to find square and cube of number.
def square_cube(x):
        square = x ** 2
        cube = x ** 3
        return square,cube
square_cube(3)


# In[37]:


# Create a function to find square and cube of number.
def Square_Cube(a):
    Square = a ** 2
    Cube = a ** 3
    print("The Square of {} is {}, Cube is {}".format(a,Square,Cube))
Square_Cube(100)


# In[ ]:




