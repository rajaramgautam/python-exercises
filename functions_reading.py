#!/usr/bin/env python
# coding: utf-8

# In[1]:


max


# In[3]:


max([4, 3, 2, 1])


# In[5]:


maximum_number = max([4, 3, 2, 1])
print(maximum_number)


# In[6]:


type(maximum_number)


# In[7]:


print('The max is: ' + str(maximum_number))


# In[23]:


def increment(n):
    return n+1
return_value1= increment(3)


# In[24]:


return_value1 = increment(3)


# In[25]:


return_value1


# In[22]:


type(c)


# In[10]:


type(increment(3))


# In[11]:


def add (a, b):
    result = a+b
    return result


# In[13]:


add(6, 1)


# In[16]:


x=4
add (x, 3)


# In[17]:


def shout(message):
    print(message.upper() + '!!!')
return_value = shout('hey there')


# In[18]:


type(return_value)


# In[31]:


return_value


# In[27]:


shout('hey there')


# In[28]:


def increment(n):
    return n+1
return_value1= increment(3)


# In[29]:


type(return_value1)


# In[30]:


return_value1


# In[32]:


def sayhello():
    print('Hey there!')
    
sayhello()


# # Default Values
# 

# In[33]:


def sayhello(name = 'World', greeting = 'Hello'):
    return '{}, {}'.format(greeting, name)
sayhello()


# In[34]:


sayhello('Codeup')


# In[35]:


sayhello('Ranjana')


# In[36]:


sayhello('Morning')


# In[37]:


sayhello('Codeup', 'Salutation')


# In[39]:


sayhello('Rajaram')


# In[40]:


sayhello(name = 'Aarvik')


# In[44]:


sayhello(name = "a", greeting = "b")


# # Keyword Arguments

# In[46]:


sayhello(greeting = 'Salutations', name = 'Codeup')


# In[47]:


sayhello('Codeup', greeting = 'Salutations')


# # The only restriction is that keyword arguments must come after the postional arguments.

# In[48]:


sayhello(greeting = 'Salutations', 'Codeup')


# # Calling Functions

# In[49]:


args = ['Codeup', 'Salutations']
sayhello(*args)


# In[50]:


kwargs = {'greeting': 'salutations', 'name': 'Codeup'}
sayhello(**kwargs)


# # Function Scope

# In[57]:


a_global_variable = 42

def somefunction():
    print('Inside the function: %s' % a_global_variable)

somefunction()
print('Outside the function: %s' % a_global_variable)


# In[58]:


def somefunction():
    a_local_variable = 'pizza'
    print('Inside the function: %s' % a_local_variable)

somefunction()
print('Outside the function: %s' % a_local_variable)


# # Lamda Functions

# In[52]:


add_one = lambda n: n+1
add_one(8)


# In[53]:


cube = lambda n: n**3
cube(3)


# In[54]:


print(' %s')


# In[ ]:




