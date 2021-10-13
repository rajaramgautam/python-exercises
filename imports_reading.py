#!/usr/bin/env python
# coding: utf-8

# # Example 1: Importing a module from the python standard library

# In[1]:


import math

x = 4
math.sqrt(x)


# In[2]:


# module as an alias

import math as m

x = 16
m.sqrt(x)


# In[4]:


x = 4.3
m.ceil(4.3) # return the ceiling of x, i.e. round UP!


# In[5]:


from math import sqrt

sqrt(4)


# # To be asked with instructor

# In[6]:




from math import sqrt, pow

print('The square root of 2 is ≅ %.3f' % sqrt(2))
print('pi squared is about %.2f' % pow(3.14, 2))


# # Example 2: A Third Party Library

# In[7]:


import pandas as pd

pd.Series(["a", 1, True])


# # Example 3: A local file that contains imports

# In[8]:


import math

def rounded_sqrt(x):
    return math.ceil(math.sqrt(x))


# In[9]:


rounded_sqrt(10)


# In[ ]:




