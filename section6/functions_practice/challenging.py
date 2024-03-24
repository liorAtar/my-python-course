# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1, 2, 4, 0, 0, 7, 5]) --> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) --> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) --> False

def spy_game(nums):
    zero_count = 0

    if 0 in nums and 7 in nums:
        for num in nums:
            if zero_count == 2 and num == 7:
                return True
            elif zero_count != 2 and num == 0:
                zero_count += 1
    return False


# Check
print(spy_game([1, 2, 4, 0, 0, 7, 5]))

# Check
print(spy_game([1, 0, 2, 4, 0, 5, 7]))

# Check
print(spy_game([1, 7, 2, 0, 4, 5, 0]))


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and
# including a given number count_primes(100) --> 25 By convention, 0 and 1 are not prime.

def is_prime(num):
    is_num_prime = True

    if num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_num_prime = False
                break
    return is_num_prime


def count_primes(num):
    count = 0
    for i in range(2, num+1):
        if is_prime(i):
            count += 1
    return count


# Check
print(count_primes(100))


# Just for fun:
# PRINT BIG: Write a function that takes in a single letter, and returns a 5 x5 representation of that letter


# print_big('a')
#
# out:  *
#      * *
#     *****
#     *   *
#     *   *

# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to
# specific 5 - line combinations of patterns. For purposes of this exercise, it's ok if your dictionary stops at "E".

# ****
# *   *
# ****
# *   *
# ****

# *****
# *
# *
# *
# *****

def print_big(letter):
    let_start_list = {
        'a': {
            0: [0, 0, 1, 0, 0],
            1: [0, 1, 0, 1, 0],
            2: [1, 1, 1, 1, 1],
            3: [1, 0, 0, 0, 1],
            4: [1, 0, 0, 0, 1],
        },
        'b': {
            0: [1, 1, 1, 1, 0],
            1: [1, 0, 0, 0, 1],
            2: [1, 1, 1, 1, 0],
            3: [1, 0, 0, 0, 1],
            4: [1, 1, 1, 1, 0],
        },
        'c': {
            0: [0, 1, 1, 1, 1],
            1: [1, 0, 0, 0, 0],
            2: [1, 0, 0, 0, 0],
            3: [1, 0, 0, 0, 0],
            4: [0, 1, 1, 1, 1]
        }
    }

    curr_row = 0
    while curr_row < 5:
        row_str = ""
        for column in let_start_list[letter][curr_row]:
            if column == 0:
                row_str += " "
            elif column == 1:
                row_str += "*"
        print(row_str)
        curr_row += 1
    print('\n')


print_big('a')
print_big('b')
print_big('c')
