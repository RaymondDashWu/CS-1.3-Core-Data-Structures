# PSEUDO BRAINSTORM
# use sets to create word bank 1 & 2
# find out which set is smaller
# iterate through smaller word bank and see if word is banned. If it is, remove it from the bigger list
# return big list


def redact_words(words, banned_words):
    """Time Complexity: O(n + m)
    Space Complexity: O(n)"""    
    if words > banned_words:
        smaller_set = banned_words
        larger_set = words
    else:
        smaller_set = words
        larger_set = banned_words
    print("larger_set", larger_set)
    print("smaller_set", smaller_set)

    return larger_set - smaller_set

print(redact_words(set(['A', 'B', 'C']), set(['B', 'C'])))