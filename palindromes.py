#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

# Note: By filtering out text and then comparing I ruin my best case scenario time complexity
# in the instance of a scenario where the first and last letter are different. If my algorithm just compared
# the letters I'd have an O(1) operation whereas the code here has to filter and lowercase everything first,
# making it O(N) best case. 

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    
    text = text.lower()
    
    # This filters out all characters except letters and numbers. 
    import re
    text = re.sub(r"[^a-z\d]+", '', text)

    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # PSEUDO BRAINSTORM
    # Resource - 
    # https://www.willpeavy.com/palindrome/ for understanding palindrome edge cases
    # 
    # Prework - 
    # [X] change all words to lowercase
    # [X] filter out all non-letters using regex
    # 
    # Iterate through letters in half the text by
    # floor dividing to range. I think it works with odd or even numbered text?
    # have second pointer that checks if last letter

    # Logic: This checks two letters at a time: first and last to see if they're equal.
    # If not, return False
    backwards_counter = -1
    for letter in range(0, (len(text) // 2)):
        if text[letter] == text[backwards_counter]:
            backwards_counter -= 1
        else:
            return False
    return True

def is_palindrome_recursive(text, left=0, right=-1):
    # PSEUDO BRAINSTORM
    # Resource - 
    # https://www.willpeavy.com/palindrome/ for understanding palindrome edge cases
    # 
    # Prework - 
    # [X] change all words to lowercase
    # [X] filter out all non-letters using regex
    # 
    # Iterate through letters in half the text by
    # floor dividing to range. I think it works with odd or even numbered text?
    # have second pointer that checks if last letter

    # Edge case of nothing in string
    if len(text) == 0:
        return True

    # Logic: This checks two letters at a time: first and last to see if they're equal.
    # If not, return False
    if text[left] != text[right]:
        return False
    # Counter that checks when True by checking if left equals length of text divided by 2 rounded down
    elif left == (len(text) // 2):
        return True
    else:
        return is_palindrome_recursive(text, left + 1, right - 1)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()