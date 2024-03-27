# Problem 1
# Create a generator that generates the squares of numbers up to some number N.


def gen_squares(n: int):
    for num in range(n):
        yield num ** 2


for x in gen_squares(10):
    print(x)
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81


# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
# Note: Use the random library. For example:


import random

random.randint(1, 10)


# 9


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)
# 6
# 1
# 10
# 5
# 8
# 2
# 8
# 5
# 4
# 5
# 1
# 4


# Problem 3
# Use the iter() function to convert the string below into an iterator:

s = 'hello'

# code here
s_iter = iter(s)
print(next(s_iter))

# Problem 4
# Explain a use case for a generator using a yield statement where you would not want to use a normal function
# with a return statement.

# Answer: If the output of the function will take a large amount of memory


# Extra Credit!
# Can you explain what gen_comp is in the code below?
# (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)

my_list = [1, 2, 3, 4, 5]

gen_comp = (item for item in my_list if item > 3)

for item in gen_comp:
    print(item)
# 4
# 5

# Answer: gen_comp contains a generator that yields items from my_list only if they are greater than 3.

