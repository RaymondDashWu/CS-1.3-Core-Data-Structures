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
            

                

    # Recursive - ???


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
    
    # if len(pattern) == 0:
    #     return 0

    # for letter in text:
    #     if letter == pattern:
    #         for pattern_index in range(len(pattern)):
    #             if pattern[pattern_index] == text[]
                # would have to return index - n

    counter = 0
    goal = len(pattern)

    for i, letter in enumerate(text, start = 1):
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

    counter = 0
    goal = len(pattern)
    index_list = []

    for i, letter in enumerate(text):
        print("i:", i)
        print("pattern:", pattern)
        print("text:", text)
        print("index_list:", index_list)
        if letter == pattern[0]:
            counter += 1
            if counter == goal:
                index_list.append(i) # Note: This line broken. Won't append with the proper number?
        else:
            counter = 0
            if letter == pattern[counter]:
                counter += 1
    return index_list

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
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