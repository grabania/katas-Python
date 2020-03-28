# Difference of Volumes of Cuboids.
# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

# For example, if the parameters passed are([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

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
