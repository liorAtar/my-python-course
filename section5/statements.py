#  for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
# Code here
for word in st.split():
    if word.startswith('s'):
        print(word)

# Use range() to print all the even numbers from 0 to 10.
# Code Here
for num in range(0, 11):
    if num % 2 == 0:
        print(num)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# Code in this cell
print([x for x in range(1, 51) if (x % 3 == 0)])

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
# Code in this cell
for word in st.split():
    if len(word) % 2 == 0:
        print(word)

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# Code in this cell

for num in range(1,101):
    if num % 5 == 0 and num % 3 ==0 :
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
# Code in this cell
print([char[0] for char in st.split()])
