# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first ine of the code has been defined as below:

def hello_name(user_name):
    """Prints hello_username!"""
    print("hello_" + user_name.lower() + "!")

hello_name("ryehsu")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing:

def first_odds():
    """Prints odd numbers from 1-100."""
    for number in range(1, 101):
        if number % 2 == 0:
            continue
        else:
            print(number)
            number + 1
        
first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below:

def max_num_in_list(a_list):
    """Returns the max number in a list."""
    max_num = max(a_list)
    return max_num

list_of_numbers = [23, 19, 99, -56, 33]
print(max_num_in_list(list_of_numbers))


# Question 4 
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (True/False):

def is_leap_year(a_year):
    """Checks if given year is a leap year."""
    leap_year = False

    if a_year % 4 == 0:
        leap_year = True
    if a_year % 100 == 0 and a_year % 400 != 0:
        leap_year = False
    return leap_year

print(is_leap_year())


# Question 5 
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2, 3, 4, 5, 6, 7] are consecutive numbers, but [1, 2, 4, 5] are not consecutive numbers. The return should be boolean Type:

def is_consecutive(a_list):
    """Checks if numbers in a list are consecutive."""
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))

num_list = [1, 2, 3, 4, 5, 6]
print(is_consecutive(num_list))