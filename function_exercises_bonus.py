#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bonus
Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
col_index('A') returns 1
col_index('B') returns 2
col_index('AA') returns 27


# # 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# In[151]:


def twelveto24(s):
    if s[-2]== 'a':
        message8 = s.replace(':', '')
        message9 = message8.replace('am', '')
        message10 = int(message9)
        if message10 >= 1300:
            print('Invalid Input')
            
    elif s[-2]== 'p':
        message11 = s.replace(':', '')
        message12 = message11.replace('pm', '')
        message13 = int(message12)
        if message13 >= 1300:
            print('Invalid Input')      
    
    elif s[-2]== 'a':
        message = s.replace(':', '')
        message1 = message.replace('am', ' hours')
        return message1    
       
    elif s[-2]== 'p':
        message2 = s.replace(':', '')
        message3 = message2.replace('pm', '')
        message4 = int(message3)
        message5 = message4 + 1200
        message6 = str(message5)
        message7 = message6 + (' hours')
        return message7
   
    else:
        print('Invalid Format')
        


# In[152]:


twelveto24('25:00pm')


# In[ ]:





# In[85]:


def twentyfourto12(p):
    message0 = p.lower()
    message1 = message0.replace('hours', '')
    message2 = int(message1)
    if message2 > 2400:
        message = 'Invalid Input'
        return message
    elif message2 == 2400:
        message11 ='12:00 am' 
        return message11
    elif message2 == 1200:
        message10 ='12:00 pm' 
        return message10
    elif message2 < 1200:
        message3 = str(message2)
        message4 = message3[:1] + ':' + message3[1:]
        message5 = message4 + ' am'
        return message5
    elif message2 > 1200:
        message6 = message2 - 1200
        message7 = str(message6)
        message8 = message7[:2] + ':' + message7[2:]
        message9 = message8 + ' pm'
        return message9
    
    
    
    


# In[86]:


twentyfourto12('2300 Hours')


# In[ ]:




