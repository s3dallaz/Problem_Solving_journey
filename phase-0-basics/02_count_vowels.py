"""
Problem 02 - Count vowels
-------------------------
Given a string, return how many vowels (a, e, i, o, u) it has.
Uppercase vowels count too.

    "engineering" -> 5
    "PYTHON"      -> 1

Rule: use a loop. Do NOT use sum() or count().
"""

# ---- Step 1: In my own words (input / output) ----
# The problem is we need to count all the vowels inside a word and return the number of them (Input should be a str, output a number)
#
# ---- Step 2: Examples I worked out by hand ----
# Input could be a (Str, int, float, bool, or an empty str) so we need to handle this  
#
# ---- Step 3 + 4: My plan / pseudocode ----
#
# 1 - Check the input if it's a str or no and reject other inputs
# 2 - Create a tuple contains all vowels
# 3 - For loop to check vowels in words 
# 4 - Return vowels count
# 5 - Counter
#
# Pseudocode : 
# if str text != str reject
# lowercase every word
# vowels = (a, e, i, o, u)
# for i in text: if i in vowels add 1 to counter
# return counter 



def count_vowels(text):

    counter = 0

    vowels = ('a', 'e', 'i', 'o', 'u')

    if not isinstance (text,str):
            return counter
            

    
    text = text.lower()

    for i in text:
        if i in vowels:
            counter += 1

    return counter


# ---- Step 6: Tests (don't edit below this line) ----
if __name__ == "__main__":
    tests = [
        ("engineering", 5),
        ("PYTHON", 1),
        ("", 0),
        ("rhythm", 0),
        ("AeIoU", 5),
        ("Hello, World!", 3),
        (0, 0),
    ]
    for given, expected in tests:
        got = count_vowels(given)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}  count_vowels({given!r}) -> {got}   (expected {expected})")
