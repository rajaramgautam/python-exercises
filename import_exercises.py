#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Exercises

You will need to use imports to complete each exercise; in addition, these exercise will strengthen your problem solving and python coding skills.

You will be directed to create specific files in part 1, for the rest you may do your work in either import_exercises.py or import_exercises.ipynb.




# # 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
# 
# - a. Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
# - b. Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.
# - c. Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.
# 
# - Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in.
# 

# In[ ]:


from function_exercises import is_vowel
from function_exercises import is_consonant as cons
from function_exercises import handle_commas, get_letter_grade


# In[ ]:


from function_exercises import is_vowel
is_vowel('e')


# In[ ]:


from function_exercises import calculate_tip
calculate_tip(0.25, 200)


# In[ ]:


from function_exercises import get_letter_grade as grade
grade(99.9)


# # Read about and use the itertools module from the python standard library to help you solve the following problems:
# 
# - How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# - How many different combinations are there of 2 letters from "abcd"?
# - How many different permutations are there of 2 letters from "abcd"?

# In[ ]:


import itertools 
word = 'abc'
p = permutations(word)
for j in list(p):
    print(j)


# In[ ]:


from itertools import combinations
  
letters ="abcd"
  
# size of combination is set to 2
x = combinations(letters, 2) 
y = [' '.join(i) for i in x]
  
print(y)


# In[ ]:


from itertools import permutations
  
letters ="abcd"
  
# size of combination is set to 2
a = permutations(letters, 2) 
y = [' '.join(i) for i in a]
  
print(y)


# # 3. Save this file as profiles.json inside of your exercises directory (right click -> save file as...).
# 
# - Use the load function from the json module to open this file.
# 
# import json
# 
# json.load(open('profiles.json'))
# # Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
# 
# - Total number of users
# - Number of active users
# - Number of inactive users
# - Grand total of balances for all users
# - Average balance per user
# - User with the lowest balance
# - User with the highest balance
# - Most common favorite fruit
# - Least most common favorite fruit
# - Total number of unread messages for all users

# In[24]:


import json
json.load(open('profiles.json.txt'))
data = json.load(open('profiles.json.txt'))


# # Total number of users

# In[25]:


len(data)


# # Number of active users

# In[26]:


active_user = []
for user in data:
    if user['isActive'] == True:
        active_user.append(user)
        
active_user       


# In[27]:


len(active_user)


# # Number of inactive users

# In[28]:


# From common sense = total - active = 19 - 9 = 10


# In[29]:


inactive_user = []
for user in data:
    if user['isActive'] == False:
        inactive_user.append(user)
        
len(inactive_user)  


# # Grand total of balances for all users

# In[33]:


balance_data = []
def get_balance():
    for index in data:
        index = data['index']
        for balance in dictionary:
            balance = data['index']['balance']
            balance_data.append(balance)
        
balance_data           


# In[ ]:





# In[34]:


balance_data


# In[ ]:


bank


# In[59]:


i = -1
while i < (len(data)-1):
    data[i]['balance']
    i = i + 1
    print(data[i]['balance'])


# In[63]:


bank_balance = []
def balance():
    i = -1
    while i < (len(data)-1):
        data[i]['balance']
        i = i + 1
        
    bank_balance.append(data[i]['balance'])
   


# In[61]:


bank_balance


# In[51]:


data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




