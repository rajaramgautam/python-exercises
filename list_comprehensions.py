#!/usr/bin/env python
# coding: utf-8

# # 17 list comprehension problems in python

# In[22]:


fruits = ['mango', 'kiwi', 'strawberry',
          'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# # Example for loop solution to add 1 to each number in the list

# In[19]:


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number+1)

print(numbers_plus_one)


# # Example of using a list comprehension to create a list of the numbers plus one.

# In[3]:


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
numbers_plus_one = [number + 1 for number in numbers]

print(numbers_plus_one)


# # Example code that creates a list of all of the list of strings in fruits and uppercases every string

# In[4]:


fruits = ['mango', 'kiwi', 'strawberry',
          'guava', 'pineapple', 'mandarin orange']
output = []
for fruit in fruits:
    output.append(fruit.upper())
print(output)


# # Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
# 
# 
# 

# In[43]:


fruits = ['mango', 'kiwi', 'strawberry',
          'guava', 'pineapple', 'mandarin orange']
uppercased_fruits = []
for item in fruits:
    uppercased_fruits.append(item.upper())
uppercased_fruits


# # Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

# In[44]:


fruits = ['mango', 'kiwi', 'strawberry',
          'guava', 'pineapple', 'mandarin orange']
capitalized_fruits = []
for item in fruits:
    capitalized_fruits.append(item.capitalize())
capitalized_fruits


# # Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

# In[45]:



fruits_with_more_than_two_vowels = []

for fruit in fruits:
    if len([letter for letter in fruit if letter.lower() in 'aeiou']) > 2:
        fruits_with_more_than_two_vowels.append(fruit)
        
fruits_with_more_than_two_vowels
        


# # Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# In[47]:


fruits_with_only_two_vowels = []

for fruit in fruits:
    if len([letter for letter in fruit if letter.lower() in 'aeiou']) == 2:
        fruits_with_only_two_vowels.append(fruit)
        
fruits_with_only_two_vowels


# # Exercise 5 - make a list that contains each fruit with more than 5 characters

# In[8]:


fruits = ['mango', 'kiwi', 'strawberry',
          'guava', 'pineapple', 'mandarin orange']
fruits_more_than_5_char = []
for item in fruits:
    if len(item) > 5:
        fruits_more_than_5_char.append(item)

print(fruits_more_than_5_char)


# # Exercise 6 - make a list that contains each fruit with exactly 5 characters

# In[9]:


fruits = ['mango', 'kiwi', 'strawberry',
          'guava', 'pineapple', 'mandarin orange']
fruits_equal_5_char = []
for item in fruits:
    if len(item) == 5:
        fruits_equal_5_char.append(item)
print(fruits_equal_5_char)


# # Exercise 7 - Make a list that contains fruits that have less than 5 characters

# In[10]:


fruits = ['mango', 'kiwi', 'strawberry',
          'guava', 'pineapple', 'mandarin orange']
fruits_less_than_5_char = []
for item in fruits:
    if len(item) < 5:
        fruits_less_than_5_char.append(item)

print(fruits_less_than_5_char)


# # Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# In[11]:


fruits = ['mango', 'kiwi', 'strawberry',
          'guava', 'pineapple', 'mandarin orange']
number_characters_fruits = []
for item in fruits:
    number_characters_fruits.append(len(item))
print(number_characters_fruits)


# # Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# In[12]:


fruits = ['mango', 'kiwi', 'strawberry',
          'guava', 'pineapple', 'mandarin orange']
fruits_with_letter_a = []
for item in fruits:
    if 'a' in item:
        fruits_with_letter_a.append(item)
print(fruits_with_letter_a)


# # Exercise 10 - Make a variable named even_numbers that holds only the even numbers

# In[42]:


even_numbers = []
for number in numbers:
    if number%2 == 0:
        even_numbers.append(number)
even_numbers


# # Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

# In[15]:


numList = []
odd_numbers = []
for number in numList:
    if number/2 != 0:
        odd_numbers.append(number)
print(odd_numbers)


# # Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

# In[40]:


positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)
positive_numbers


# # Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

# In[36]:



negative_numbers = []
for number in numbers:
    if number < 0:
        negative_numbers.append(number)
negative_numbers


# # Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

# In[39]:


two_numeraled_numbers = []
for number in numbers:
    if len(str(abs(number))) >= 2:
        two_numeraled_numbers.append(number)
        
two_numeraled_numbers
        


# # Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# In[33]:


numbers_squared = [(number)**2 for number in numbers ]
numbers_squared


# # Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# In[26]:


odd_negative_numbers = [number for number in numbers if (number%2 != 0) and (number < 0)]
odd_negative_numbers


# # Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.

# In[25]:


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
           13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
numbers_plus_5 = [number+5 for number in numbers ]

numbers_plus_one


# In[ ]:




