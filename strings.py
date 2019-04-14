#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # PSEUDO BRAINSTORM
    # Iterate through letters in text and pattern, comparing patterns
    # Ex: in "banana" looking for "an". Would look at first letter of text - "b"
    # and then seeing if it matches with the first letter of pattern "a". In first
    # loop through it does not so it goes to next letter. Finds "a" in text, which matches
    # with "a" in pattern. Then checks for next letter "n" vs "n". Returns index

    # if pattern in text:
    #     return True
    # else:
    #     return False    

    if len(pattern) == 0:
        return True

    counter = 0 # counts pattern
    goal = len(pattern) # Once counter == goal, return True

    # Logic: Compare text with first letter in pattern. If matches, then counter + 1. 
    # If counter reaches same number as goal then return True
    for letter in text:
        if letter == pattern[counter]:
            counter += 1
            if counter == goal:
                return True
        else:
            counter = 0
            if letter == pattern[counter]:
                counter += 1
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    # PSEUDO BRAINSTORM
    # Iterate through letters in text and pattern, comparing patterns
    # Ex: in "banana" looking for "an". Would look at first letter of text - "b"
    # and then seeing if it matches with the first letter of pattern "a". In first
    # loop through it does not so it goes to next letter. Finds "a" in text, which matches
    # with "a" in pattern. Then checks for next letter "n" vs "n". Returns index

    if len(pattern) == 0:
        return 0

    counter = 0
    goal = len(pattern)

    for i, letter in enumerate(text):
        if letter == pattern[counter]:
            counter += 1
            if counter == goal:
                return i
        else:
            counter = 0
            if letter == pattern[counter]:
                counter += 1

    


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    if len(pattern) == 0:
        return 0

    # Used to keep track of when pattern is matched (GOAL!!!) as well as when that first pattern match is
    counter = 0
    goal = len(pattern)
    goal_index_list = []

    index_dict = {}

    # Logic: enumerate allows for keeping track of the letters that match the pattern as well as the index.
    # When a letter in text matches the first letter of the pattern, append both to index_dict and +1 to counter
    # When counter reaches the goal (# of letters in pattern) then append the index of the first pattern
    # matching letter to goal_index_list
    for i, letter in enumerate(text):
        if letter == pattern[counter]:
            counter += 1
            index_dict[i] = letter
            if counter == goal:
                # return index_dict
                goal_index_list.append(index_dict[pattern[0]])
                print("goal_index_list reached:", goal_index_list)
        else:
            # Resets the dictionary and counter after a letter has been found that doesn't match the pattern
            counter = 0
            index_dict = {}
            if letter == pattern[counter]:
                index_dict[i] = letter
                counter += 1
    return goal_index_list
    
def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    # indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()