# Write a function that computes the volume of a sphere given its radius.
# The volume of a sphere is given as
# (4/3)πr**3
import math
import operator
from functools import reduce


def vol(rad):
    print((4 / 3) * 3.14 * (rad ** 3))


# Check
vol(2)
# 33.49333333333333


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):
    print(f"{num} is {'in' if low < num < high else 'not in'} the range between {low} and {high}")


# Check
ran_check(5, 2, 7)
# 5 is in the range between 2 and 7


# If you only wanted to return a boolean:
def ran_bool(num, low, high):
    print(low < num < high)


ran_bool(3, 1, 10)
# True


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33
# HINT: Two string methods that might prove useful: .isupper() and .islower()

# If you feel ambitious, explore the Collections module to solve this problem!


from collections import Counter


def up_low(s):
    print(f"No. of Upper case characters : {sum(Counter(filter(lambda let: let.isupper(), s)).values())}")
    print(f"No. of Lower case characters : {sum(Counter(filter(lambda let: let.islower(), s)).values())}")

    print(f"No. of Upper case characters : {len(list(filter(lambda let: let.isupper(), s)))}")
    print(f"No. of Lower case Characters : {len(list(filter(lambda let: let.islower(), s)))}")


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
# Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
# No. of Upper case characters :  4
# No. of Lower case Characters :  33


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(lst):
    print(Counter(lst).keys())


unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


# [1, 2, 3, 4, 5]


# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):
    print(math.prod(numbers))
    print(reduce(lambda x, y: x * y, numbers))


multiply([1, 2, 3, -4])
# -24


# Write a Python function that checks whether a word or phrase is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g.,
# madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace()
# method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python,
# there are some clever ways to do it with slicing notation.


def palindrome(s):
    s.replace(' ', '')
    print(s == s[::-1])


palindrome('heleh')
# True


# Hard:
# Write a Python function to check whether a string is pangram or not.
# (Assume the string passed in does not have any punctuation)

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: You may want to use .replace() method to get rid of spaces.
# Hint: Look at the string module
# Hint: In case you want to use set comparisons

import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    str_set = set(map(lambda let: let.lower(), {*str1.replace(" ", "")}))
    print(str_set == set(alphabet))


ispangram("The quick brown fox jumps over the lazy dog")
# True

# string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
