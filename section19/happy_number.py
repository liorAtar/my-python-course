# Happy Numbers - A happy number is defined by the following process.
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1
# are happy numbers, while those that do not end in 1 are unhappy numbers.
# Display an example of your output here. Find first 8 happy numbers.


def is_happy_number(num: int) -> bool:
    """
    Determines whether a number is a happy number.

    A happy number is defined by the following process: Starting with any positive integer,
    replace the number by the sum of the squares of its digits, and repeat the process until
    the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

    Args:
        num (int): The number to check for happiness.

    Returns:
        bool: True if the number is happy, False otherwise.
    """
    showed = set()
    while num != 1 and num not in showed:
        showed.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1
