# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    for index, num in enumerate(nums):
        if index != len(nums)-1 and num == 3 and nums[index+1] == 3:
            return True
        else:
            pass
    return False


# Check
print(has_33([1, 3, 3]))

# Check
print(has_33([1, 3, 1, 3]))

# Check
print(has_33([3, 1, 3]))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    return "".join([let*3 for let in text])


# Check
print(paper_doll('Hello'))

# Check
print(paper_doll('Mississippi'))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif (a == 11 or b == 11 or c == 11) and sum((a, b, c, -10)) <= 21:
        return sum((a, b, c, -10))
    else:
        return 'BUST'


# Check
print(blackjack(5,6,7))

# Check
print(blackjack(9,9,9))

# Check
print(blackjack(9,9,11))

# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer_69(arr):
    start_pop = -1
    stop_pop = -1

    if 6 in arr and 9 in arr:
        for index, num in enumerate(arr):
            if index != len(arr)-1 and num == 6 and 9 in arr[index+1:]:
                start_pop = index
            elif start_pop >= 0 and num == 9:
                stop_pop = index + 1
        return sum(arr[:start_pop]) + sum(arr[stop_pop:])
    return sum(arr)


# Check
print(summer_69([1, 3, 5]))

# Check
print(summer_69([4, 5, 6, 7, 8, 9]))

# Check
print(summer_69([2, 1, 6, 9, 11]))
