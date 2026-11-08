"""
Problem 03 - Sum of digits
--------------------------
Given a non-negative whole number, return the sum of its digits.

    4096 -> 19   (4 + 0 + 9 + 6)
    7    -> 7

Rule: use a loop. Do NOT use sum().
Challenge: solve it TWICE. Once by turning the number into a string,
and once using only math (hint for later: think about % and //).
"""

# ---- Step 1: In my own words (input / output) ----
# We need to sum all the digits in the input number
#
# ---- Step 2: Examples I worked out by hand ----
# Empty input, 0 , 1 digit
#
# ---- Step 3 + 4: My plan / pseudocode ----
# Converting input to str
# Input to seperated digits using for loop
# Sum them
#
# Pseudocode 1: 
# 
# string input = str(n)
# Counter = 0
# for i in string input : add i to counter
# Return result
#
# Pseudocode 2:
# 
# result = 0
# While loop to run on all digits
# Extracting last digit from input
# Adding it to result
# Remove last digit and repeat




def sum_of_digits(n):

    # str_input = str(n)
    result = 0

    # for i in str_input:
    #     result += int(i)

    # return result

    while n > 0:

        last_digit = (n%10)

        result += last_digit

        n = (n//10)

    return result


# ---- Step 6: Tests (don't edit below this line) ----
if __name__ == "__main__":
    tests = [
        (4096, 19),
        (7, 7),
        (0, 0),
        (1000, 1),
        (99999, 45),
    ]
    for given, expected in tests:
        got = sum_of_digits(given)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}  sum_of_digits({given}) -> {got}   (expected {expected})")
