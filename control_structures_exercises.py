#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Exercises

# Do your work for this exercise in a file named control_structures_exercises.py.

# Conditional Basics

# 1 a. prompt the user for a day of the week, print out whether the day is Monday or not
day_of_week = input('What day is today ?')
if day_of_week.lower() == 'monday':
    print('Its Monday.')
else:
    print('It is not Monday.')


# In[3]:


Exercises

Do your work for this exercise in a file named control_structures_exercises.py.

Conditional Basics

prompt the user for a day of the week, print out whether the day is Monday or not

prompt the user for a day of the week, print out whether the day is a weekday or a weekend

create variables and make up values for

the number of hours worked in one week
the hourly rate
how much the week's paycheck will be
write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

Loop Basics

While

Create an integer variable i with a value of 5.
Create a while loop that runs so long as i is less than or equal to 15
Each loop iteration, output the current value of i, then increment i by one.
Your output should look like this:


5
6
7
8
9
10
11
12
13
14
15
Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
Alter your loop to count backwards by 5's from 100 to -10.
Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

 2
 4
 16
 256
 65536
Write a loop that uses print to create the output shown below.


100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
For Loops

Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

For example, if the user enters 7, your program should output:


7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
Create a for loop that uses print to create the output shown below.


1
22
333
4444
55555
666666
7777777
88888888
999999999

break and continue

Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

Your output should look like this:


Number to skip is: 27

Here is an odd number: 1
Here is an odd number: 3
Here is an odd number: 5
Here is an odd number: 7
Here is an odd number: 9
Here is an odd number: 11
Here is an odd number: 13
Here is an odd number: 15
Here is an odd number: 17
Here is an odd number: 19
Here is an odd number: 21
Here is an odd number: 23
Here is an odd number: 25
Yikes! Skipping number: 27
Here is an odd number: 29
Here is an odd number: 31
Here is an odd number: 33
Here is an odd number: 35
Here is an odd number: 37
Here is an odd number: 39
Here is an odd number: 41
Here is an odd number: 43
Here is an odd number: 45
Here is an odd number: 47
Here is an odd number: 49
The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

Fizzbuzz

One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
Display a table of powers.

Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.
Example Output

What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125
Bonus: Research python's format string specifiers to align the table

Convert given number grades into letter grades.

Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0
Bonus

Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.


# In[5]:


# 1 b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day_of_week = input('What day is today?')
if day_of_week.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    print('Its a weekday')
elif day_of_week.lower() in ['saturday', 'sunday']:
    print('Its weekend')
else:
    print('Its invalid input.')


# In[11]:


# 1 c. the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

number_of_hours_worked_weekly = 40
hourly_rate = 45

if number_of_hours_worked_weekly <= 40:
    weekly_pay_check = number_of_hours_worked_weekly * hourly_rate
    print('The weelky pay is $' + str(weekly_pay_check) )
if number_of_hours_worked_weekly > 40:
    weekly_pay_check = number_of_hours_worked_weekly * 40 + (1.5*hourly_rate* (number_of_hours_worked_weekly - 40))
    print('The weelky pay is $' +  str(weekly_pay_check) )


# In[21]:


# 2. Loop Basics

# While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
# Your output should look like this:

i = 5
while i <= 15:
    print(i)
    i += 1


# In[32]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

 
i = 0
while i <= 100:
    print(i)
    i = i + 2


# In[33]:


# Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i = i-5


# In[39]:


# Create a while loop that starts at 2, and displays the number squared on each line while
# the number is less than 1,000,000. Output should equal:

i = 2
while i < 1000000:
    print(i)
    i =i**2


# In[41]:


# Write a loop that uses print to create the output shown below
i = 100
while i > 0:
   print(i)
   i = i-5
   


# In[66]:


# b. For Loops

# i. Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.

# For example, if the user enters 7, your program should output:

multiplication_chart = int(input('Which number multiplication chart do you like? '))

for i in range(1, 11):
    product = multiplication_chart * i
    print(f'{multiplication_chart} x {i} = {product}')

   
    


# In[64]:


# 2 b. ii Create a for loop that uses print to create the output shown below.
for i in range(1, 10):
    print(str(i)*i)


# In[114]:


# # 2 c. Break and Continue
#  i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting
#the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). 
#Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.

# Your output should look like this:


# Number to skip is: 27

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49

num = input('Please enter an odd number between 1 and 50: ')

while True:
    if (num.isdigit() == False 
        or int(num) >50 
        or int(num) <= 0 
        or int(num) % 2 == 0):
            print('Invalid input')
            num = input('Please enter an odd number between 1 and 50: ')
    else:
        break
        
num = int(num)

print(f'The num to skip : {num}')

for i in range(1, 50):
    if i%2 == 0:
        
        continue
   
    elif i ==  num:
        print(f'Yikes! Skipping number : {i}')
    else:
        print(f'Here is an odd number: {i}')
        

        
    


# # 2. d. The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
# 

# In[118]:


num = input('Please enter a positive: ')
while True:
    if (num.isdigit() == False 
        
        or int(num) <= 0):
            print('Invalid input')
            num = input('Please enter a positive: ')
    else:
        break
        
num = int(num)

for i in range(0, num+1):
    print(i)



# # 2. e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1. 

# In[120]:


num = input('Please enter a positive: ')
while True:
    if (num.isdigit() == False 
        
        or int(num) <= 0):
            print('Invalid input')
            num = input('Please enter a positive: ')
    else:
        break
        
num = int(num)

for i in reversed(range(1, num+1)):
    print(i)
    i = i-1


# In[ ]:


# 3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

    
    


# In[83]:


# Write a program that prints the numbers from 1 to 100.
for number in range(1, 101):
    print(number)


# In[87]:


# For multiples of three print "Fizz" instead of the number
for number in range(1, 101):
    if number%3 == 0:
        print('Fizz')
    else :
        print(number)


# In[88]:


# For the multiples of five print "Buzz".
for number in range(1, 101):
    if number%5 == 0:
        print('Buzz')
    else :
        print(number)


# In[89]:


# For numbers which are multiples of both three and five print "FizzBuzz".
for number in range(1, 101):
    if number%3 == 0 and number%5 == 0:
        print('FizzBuzz')
    else :
        print(number)


# In[96]:


for number in range(1, 101):
    if number%3 == 0 and number%5 == 0:
        print('FizzBuzz')
        continue
    elif number%3 == 0:
        print('Fizz')
        # continue
    elif number%5 == 0:
        print('Buzz')
        continue
    else:
        print(number)


# # 4 Display a table of powers.
# 
# - Prompt the user to enter an integer.
# - Display a table of squares and cubes from 1 to the value entered.
# - Ask if the user wants to continue.
# - Assume that the user will enter valid data.
# - Only continue if the user agrees to.
# - Example Output
# 
# What number would you like to go up to? 5
# 
# Here is your table!
# 
# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125
# 

# In[165]:


while True:   
    num = input('What number would you like to go up to? ')

    print('Here is your table!')
    print('number | squared | cubed ')
    print('------ | ------- | ----- ')

    num = int(num)
    for i in range (1 , num+1):
        print(f'{i}      | {i**2}       | {i**3}')



    user_input = input('Do you want to continue? Please enter yes or y to continue:')
    if user_input.lower() in ['yes', 'y']:
        continue
    else:
        break
    
    


# In[ ]:





# ## 5 Convert given number grades into letter grades.
# 
# - Prompt the user for a numerical grade from 0 to 100.
# - Display the corresponding letter grade.
# - Prompt the user to continue.
# - Assume that the user will enter valid integers for the grades.
# - The application should only continue if the user agrees to.
# - Grade Ranges:
# 
# - A : 100 - 88
# - B : 87 - 80
# - C : 79 - 67
# - D : 66 - 60
# - F : 59 - 0
# - Bonus
# 
# - Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

# In[166]:


while True:
    num_grade = input('Enter numerical grade from 0 to 100: ')
    num_grade = int(num_grade)

    if num_grade in range(88, 101):
        print('The corresponding letter grade: A')
    
    elif num_grade in range(80, 88):
        print('The corresponding letter grade: B')
    
    elif num_grade in range(67, 80):
        print('The corresponding letter grade: C')
    
    elif num_grade in range(60, 67):
        print('The corresponding letter grade: D')
    
    else:
        print('The corresponding letter grade: F')
    


    user_input = input('Do you want to continue? Please enter yes or y to continue:')
    if user_input.lower() in ['yes', 'y']:
        continue
    else:
        break
    


# # Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
# 
# - a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[ ]:


books = [
    {
        'title':'title1',
        'author': 'author1',
        'genre': 'genre1'
    },
    {
        'title':'title2',
        'author': 'author1',
        'genre': 'genre2'
    },
    {
        'title':'title3',
        'author': 'author2',
        'genre': 'genre2'
    },
    {
        'title':'title4',
        'author': 'author3',
        'genre': 'genre2'
    }
]
for book in books:
    print(f" The book {book['title']} by author {book['author']} belongs to {book['genre']}")
    
    user_input = input('Please choose a genre: ')
for book in books:
    if user_input == book['genre']:
        print(book['title'])


# In[ ]:




