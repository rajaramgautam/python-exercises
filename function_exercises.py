#!/usr/bin/env python
# coding: utf-8

# # Exercises
# 
# - Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.
# 

# # 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[9]:


def is_two(x):
    if isinstance(x, str):
        return True
    elif isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    
    else:
        return False


# In[24]:


is_two(True)


# In[17]:


def is_two2(var):
    if type(var) == str:
        return True
    elif type(var) == int:
        return True
    elif type(var) == float:
        return True
    
    else:
        return False


# In[23]:


is_two2([1, 2, 3, 4]) 


# # 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[25]:


def is_vowel(para):
    if para in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' }:
        return True
    else:
        return False
    


# In[31]:


is_vowel("B")


# # 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[32]:


def is_consonant(para):
    if is_vowel(para) == True:
        return False
    else:
        return True
    


# In[35]:


is_consonant('b')


# # 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[41]:


def string_word(s):
    if is_consonant(s[0]) == True:
        return s.capitalize()
    


# In[62]:


string_word('nepal')


# # 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
# 

# In[61]:


def calculate_tip(tip_percentage, bill_total):
    tip_amount = tip_percentage * bill_total
    return tip_amount
    


# In[57]:


calculate_tip(0.1, 200)


# # 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[63]:


def apply_discount(original_price, discount_percentage):
    price_after_discount = original_price * (100-discount_percentage)/100
    return price_after_discount


# In[64]:


apply_discount(200, 20)


# # 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[65]:


def handle_commas(p):
    return p.replace(',', '')


# In[67]:


handle_commas('apple, Orange and Grapes')


# # 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[110]:


def get_letter_grade(number):
    number = float(number)
    if number >100:
        return 'Invalid Input'
    if number >= 90:
        return 'A'
    elif number >= 80:
        return 'B'
    elif number >= 70:
        return 'C'
    elif number >= 60:
        return 'D'
    elif number >= 50:
        return 'E'
    else:
        return 'F'


# In[112]:


get_letter_grade(99.9)


# # 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[139]:


def remove_vowels(f):
    newstr = f
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in f.lower():
        if x in vowels:
            newstr = newstr.replace(x, '')
    return newstr


# In[140]:


remove_vowels('apple')


# # 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#     - Name will become name
#     - First Name will become first_name
#     - % Completed will become completed

# In[144]:


def normalize_name(r):
    r = r.strip()
    r = r.lower()
    r = r.replace(' ', '_')
    return r
    


# In[145]:


normalize_name("  Rajaram Gautam   ")


# # 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#     - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#     - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[148]:


def cumulative_sum(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]
    


# In[150]:


cumulative_sum([1, 2, 3])


# In[ ]:




