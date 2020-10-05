#!/usr/bin/env python
# coding: utf-8

# In[1]:


text = """Data Science is a process of extracting knowledge from the data, 
which has several process like data preparation, analysis and modelling.
Data Preparation takes 70% of data science project rest is all about analysis and modelling."""
print(text)


# In[3]:


text = text.lower
tokens = text.split(text)
print(token)


# In[4]:


# Splitting text into tokens/words by using split function
text = text.lower()
print(text)
tokens = text.split()
print(tokens)


# In[16]:


start_e = []
for words in tokens:
    if words.startwith('e'):
        start_e.append(words)
(start_e)


# In[17]:


starts_with_e=[]
for word in tokens:
    if word[0]=='e':
        starts_with_e.append(word)

starts_with_e  


# In[18]:


ends_with_e = []
for word in tokens:
    if word.endswith('e'):
        ends_with_e.append(word)

ends_with_e output : ['science', 'knowledge', 'the', 'like', 'science']


# In[21]:


start_e =[]
for words in tokens:
    if words.startswith('e'):
        start_e.append(words)
        
(start_e)


# In[25]:


ends_with_e = []
for word in tokens:
    if word.endswith('e'):
        ends_with_e.append(word)

ends_with_e 


# In[ ]:


# First create an empty list with the name startingwith_e
# Then keep a condition that,if the words starts with 'e'
startswith_e = []


# In[ ]:


# For the words in tokens keep printing the words.
# As soon as if finds the word 'process' break the loop


# In[29]:


for words in tokens:
    print(words)
    if words == 'process':
        break


# In[35]:


ends_with_e = []
for word in tokens:
    if word.endswith('e'):
        ends_with_e.append(word)

ends_with_e 


# In[36]:


import random
rand = []
for i in range(100):
    num = random.randint(0,100)
    rand.append(num)
print(rand)
    


# In[41]:


# Find and create an even numbers in rand
even = []
for i in rand:
    if i % 2 == 0:
        even.append(str(i))
        print('Even numbers are :\n',even)
print('='*79)
    


# In[42]:


# Find and create an even numbers in rand
even = []
for i in rand:
    if i % 2 == 0:
        even.append(i)
print(even)
    


# In[45]:


# Find and create a list of numbers divisible by 5 in rand.
Div5 = []
for i in range(100):
    if i % 5 == 0:
        Div5.append(i)
        
print(Div5) 


# In[46]:


count = 0
if count < 5:
    print("Hello, I am an if statement and count is", count,'\n')
    count += 1
    print("Current count is:", count,'\n')
    print('******If loop is over******\n')
    while count < 5:
        print("Hello, I am a while and count is" , count,'\n')
        count +=1 #
        print('******While loop is over******\n')


# In[1]:


# Example of file working with loops
x = 0
# Define a while loop
while(x < 4):
    print(x)
    x = x + 1


# In[2]:


# Define a for loop
for x in range(2,7):
    print(x)


# In[ ]:


# Lets check the difference between if and while


# In[6]:


count = 0
if count < 5:
    print(count)
    count += 1


# In[7]:


count = 0
while count < 5:
    print(count)
    count += 1 # count = count + 1


# In[11]:


count = 0
while True:
    print(count)
    count += 1
    print("Current count is", count, '\n')
    print("-"*50)
    if count >= 10:
        break # Do not remove break


# In[ ]:


count = 0
while True:
    print(count)
    count += 1
    print("Current count is", count, '\n')
    print("-"*50)
    


# In[3]:


# Find the product of all numbers present in a list
lst = [10, 20, 30, 40, 50]
product = 1
index = 0
while index < len(lst):
    print("length of the index is:",len(lst), '\n')
    print("each indexing value are:",lst[index], '\n')
    product *= lst[index]
    print("product value",product, '\n')
    index += 1
    print("current indexing position is", index, '\n')
    print("-"*45)
print("product is: {}".format(product))


# ## While Loop with else
# 
# Same as that of for loop, we can have an optional else block with while loop as well.
# 
# The else part is executed if the condition in the while loop evaluates to False. The while loop can be terminated with a break statement.
# 
# In such case, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false.
# 
# 

# In[5]:


# While loop with else
numbers = [10, 20, 30, 40, 50]
#iterating over the list
index = 0
while index <len(numbers):
    print(numbers[index])
    index += 1
    print("Current indexing:", index)
else:
        print("\n no item left in the list")


# In[ ]:





# In[ ]:




