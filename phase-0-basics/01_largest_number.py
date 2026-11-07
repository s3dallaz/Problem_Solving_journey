"""
Problem 01 - Largest number
---------------------------
Given a list of numbers, return the largest one.

    [3, 9, 2, 7]  -> 9
    [-5, -1, -8]  -> -1

Rule: do NOT use max() or sorted(). Use a loop.
You can assume the list has at least one number.
"""

# ---- Step 1: In my own words (input / output) ----
#
# The problem asks me to return the largest number from a list without using pre-built functions 
#
# ---- Step 2: Examples I worked out by hand ----
# The input is a list of numbers: many numbers, or just 1 number. The problem says there is always at least one number.
#
# ---- Step 3 + 4: My plan / pseudocode ----
# My plan: keep a variable called biggest, check each number, and replace biggest when a bigger number shows up. #
# pseudocode: start with the first number, for loop over the list, if a number is bigger, replace biggest, return biggest


def largest(numbers):
    biggest = numbers[0]


    for i in numbers:
        if i > biggest:
            biggest = i

    return biggest


# ---- Step 6: Tests (don't edit below this line) ----
if __name__ == "__main__":
    tests = [
        ([3, 9, 2, 7], 9),
        ([-5, -1, -8], -1),
        ([42], 42),
        ([1, 1, 1], 1),
        ([0, -2, 10, 10, 3], 10),
    ]
    for given, expected in tests:
        got = largest(given)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}  largest({given}) -> {got}   (expected {expected})")
