#Day 4 - Digits, integers

"""
Ex1: Function finds if int "val" is contained by List "digits".
Ex2: User enters integer between 101 and 99999, returns reversed int.
"""

from typing import List
from random import randint
import time
from bisect import bisect_left

class OutOfRangeError(Exception):
    pass

start_time = time.time()
n = 100 # number of digits
digits_example = [randint(-1000, 1000) for _ in range(n)]

#in operator approach - 6.45s with 1M digits: O(n) time complexity
def isinlist(val: int, digits: List[int]) -> bool:
    return val in digits

#sort approach - 6.5s with 1M digits
def isinlist_list_sorting(val: int, digits: List[int]) -> bool:
    digits.sort()
    x = bisect_left(digits, val)
    if type(x) == int:
        return True

def reverseint() -> int:
    while True:
        try:
            number = input("Enter number to reverse (between 101 and 99999): ")
            if int(number)<101 or int(number)>99999:
                raise OutOfRangeError
            reversed_number_str = number[::-1]
            return int(reversed_number_str)
        except OutOfRangeError:
            print("Your entered number is out of range, try again!\n")
        except:
            print("Enter correct value, try again.")


print(isinlist(2, digits_example))
print("--- %s seconds ---" % (time.time() - start_time))
print(f'With {n} digits\n')

print(reverseint())