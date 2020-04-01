# Difference of Volumes of Cuboids.
# In this simple exercise, you will create a program that will take
# two lists of integers, a and b. Each list will consist of 3 positive
# integers above 0, representing the dimensions of cuboids a and b.
# You must find the difference of the cuboids' volumes regardless of which is bigger.
# For example, if the parameters passed are([2, 2, 3], [5, 4, 1]),
# the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.
# Your function will be tested with pre-made examples as well as random ones.
# If you can, try writing it in one line of code.


def find_difference(a, b):
    return abs((a[1]*a[2]*a[0])-b[1]*b[2]*b[0])


print(find_difference([3, 2, 5], [1, 4, 4]))


# Is it even?
# In this Kata we are passing a number(n) into a function.
# Your code will determine if the number passed is even(or not).
# The function needs to return either a true or false.
# Numbers may be positive or negative, integers or floats.
# Floats are considered UNeven for this kata.


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


print(is_even(0))
print(is_even(0.5))


# Will you make it?
# You were camping with your friends far away from home,
# but when it's time to go back, you realize that you fuel
# is running out and the nearest pump is 50 miles away!
# You know that on average, your car runs on about 25 miles per gallon.
# There are 2 gallons left. Considering these factors, write
#  a function that tells you if it is possible to get to the pump or not.
#  Function should return true(1 in Prolog) if it is possible and
#   false(0 in Prolog) if not. The input values are always positive.


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))


# Removing Elements
# Take an array and remove every second element out of that array.
# Always keep the first element and start removing with the next element.
# Example:
# my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    return my_list[::2]


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# Number toString
# The code gives an error!
# a = 123.toString()
# Fix it!

a = str(123)

print(a, '123', 'Wrong!')


# Even or Odd
# Create a function(or write a script in Shell) that takes
# an integer as an argument and returns "Even" for even
# numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(2))
print(even_or_odd(7))
print(even_or_odd(1))
print(even_or_odd(-1))


# Opposite number
# Very simple, given a number, find its opposite.
# Examples:
# 1: -1
# 14: -14
# -34: 34

def opposite(number):
    return number * (-1)


print(opposite(1))


# Sum of positive
# You get an array of numbers, return the sum of all of the positives ones.
# Example[1, -4, 7, 12] = > 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    s = 0
    for x in arr:
        if x > 0:
            s = s + x
    return s


print(positive_sum([1, 2, 3, 4, 5]))
print(positive_sum([1, -2, 3, 4, 5]))
print(positive_sum([-1, 2, 3, 4, -5]))
print(positive_sum([]))
print(positive_sum([-1, -2, -3, -4, -5]))


# Return Negative
# In this simple assignment you are given a number
# and have to make it negative. But maybe the number is already negative?
# Example:
# make_negative(1)  # return -1
# make_negative(-5)  # return -5
# make_negative(0)  # return 0
# Notes:
# The number can be negative already, in which case
# no change is required.
# Zero(0) is not checked for any specific sign.
# Negative zeros make no mathematical sense.

def make_negative(number):
    if number <= 0:
        return number
    else:
        return number * (-1)


print(make_negative(42))


# Convert boolean values to strings 'Yes' or 'No'.
# Complete the method that takes a boolean value and
# return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'


print(bool_to_word(True))
print(bool_to_word(False))


# Remove String Spaces
# Simple, remove the spaces from the string, then return the resultant string.


def no_space(x):
    return x.replace(" ", "")


print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
print(no_space(
    '8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
print(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
print(no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8')
print(no_space('8j aam'), '8jaam')


# Reversed Strings
# Complete the solution so that it reverses the string value passed into it.
# solution('world')

def solution(string):
    return string[::-1]


print(solution('world') == 'dlrow')
print(solution('hello') == 'olleh')
print(solution('') == '')
print(solution('h') == 'h')


# Convert a String to a Number!
# We need a function that can transform a string into a number.
# What ways of achieving this do you know?
# Note: Don't worry, all inputs will be strings,
# and every string is a perfectly valid representation of an integral number.
# Examples
# stringToNumber("1234") == 1234
# stringToNumber("605") == 605
# stringToNumber("1405") == 1405
# stringToNumber("-7") == -7

def string_to_number(s):
    return int(s)


print(string_to_number("1234"))
print(string_to_number("605"))
print(string_to_number("1405"))
print(string_to_number("1234"))


# Convert a Number to a String!
# We need a function that can transform a number into a string.
# What ways of achieving this do you know?
# Examples:
# number_to_string(123) / * returns '123' * /
# number_to_string(999) / * returns '999' * /

def number_to_string(num):
    return str(num)


print(number_to_string(67))


# Vowel Count
# Return the number(count) of vowels in the given string.
# We will consider a, e, i, o, and u as vowels for this Kata.
# The input string will only consist of lower case letters and/or spaces.


def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
            num_vowels += 1
    return num_vowels


print(getCount("abracadabra"))
