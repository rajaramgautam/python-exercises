
""" 
/**
Create a Python script file named data_types_and_variables.py. Inside it, write some Python code, that is, variables and operators, to describe the 
following scenarios. Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions
 can be represented with code.

You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet 
if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. 
Google pays 400 dollars per hour, 
Amazon 380, and Facebook 350. How much will you receive in payment for this week? 
You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
A student can be enrolled to a class only if the class is not full and the class schedule 
does not conflict with her current schedule.
A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
Premium members do not need to buy a specific amount of products.


Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'
Create a variable that holds a boolean value for each of the following conditions:

the password must be at least 5 characters
the username must be no more than 20 characters
the password must not be the same as the username
bonus neither the username or password can start or end with whitespace
For practicing with list comprehensions, work through 17 List Comprehension Exercises. Add your solutions to a new file named list_comprehensions.py

BONUS

For even more practice with all your Python tools together, work through 20 Python Data Structure Manipulation Exercises. 
Name this file python_data_structure_manipulation_exercises.py.

**/ """

# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet
# if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

the_little_mermaid_days = 3
brother_bear_day = 5
hercules_days = 1

total_days = the_little_mermaid_days + brother_bear_day + hercules_days
cost_per_day = 3


total_cost = cost_per_day * total_days
print(total_cost)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour.
# Google pays 400 dollars per hour,
# Amazon 380, and Facebook 350. How much will you receive in payment for this week?
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
google_pay_hourly = 400
amazon_pay_hourly = 380
facebook_pay_hourly = 350
google_work_hour = 6
amazon_work_hour = 4
facebook_work_hour = 10

google_pay_weekly = google_pay_hourly * google_work_hour
amazon_pay_weekly = amazon_pay_hourly * amazon_work_hour
facebook_pay_weekly = facebook_pay_hourly * facebook_work_hour

total_pay_weekly = google_pay_weekly + amazon_pay_weekly + facebook_pay_weekly

print(total_pay_weekly)

# A student can be enrolled to a class only if the class is not full and the class schedule
# does not conflict with her current schedule.

is_class_full = False
class_schedule_conflict = False
can_enroll_class = not (is_class_full or class_schedule_conflict)

print(can_enroll_class)

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired.
# Premium members do not need to buy a specific amount of products.

premiun_members = True
order_more_than_2 = True
order_less_than_or_equal2 = False
product_offer = (not order_less_than_or_equal2)

print(product_offer)

# Use the following code to follow the instructions below:

# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'
len(password) >= 5
len(username) <= 20
password == username
