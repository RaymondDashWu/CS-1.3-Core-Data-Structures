#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # PSEUDO BRAINSTORM
    # map that starts out adding 1, 10, 100, etc. based on binary values
    # map function that takes in the length of digits and generates a map then subtracts from total

    # 	var romanNumeralDict map[int]string = map[int]string{
	# 	1000: "M",
	# 	900:  "CM",
	# 	500:  "D",
	# 	400:  "CD",
	# 	100:  "C",
	# 	90:   "XC",
	# 	50:   "L",
	# 	40:   "XL",
	# 	10:   "X",
	# 	9:    "IX",
	# 	5:    "V",
	# 	4:    "IV",
	# 	1:    "I",
	# }
    
    # test = map(lambda x: 2 ** x)

    # PSEUDO 2
    # for length of digits, becomes 2 to the power of n - 1
    # add total values if value at position = 1
    #  n - 1
    # total = 0
    # for bit in len(digits):
    #     if digits[bit] == 1:
    #         total += digits ** (bit - 1)
    #     else:
    #         continue



    # TODO: Decode digits from binary (base 2)
    # total = 0
    # for bit in range(0, len(digits)):
    #     # if digits in string.digits:
    #     print(digits[bit])
    #     if digits[bit] == '1':
    #         total += base ** int(digits[bit])
    #     else:
    #         continue
    # return total
    # TODO: Decode digits from hexadecimal (base 16)
    
    # PSEUDO BRAINSTORM:
    # 110

    total = 0
    power = len(digits) - 1

    for character in digits:
        print('DID IT WORK?')
        total += string.printable.index(character) * (base ** power)
        power -= 1
    return total




    # TODO: Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # ...
    # TODO: Encode number in hexadecimal (base 16)

    # PSEUDO BRAINSTORM
    # divide the decimal number by 16 repeatedly.
    # write the last remainder you obtained in the hex equivalent column
    # If the remainder is more than nine, remember to change it to its hex letter equivalent. 
    # Return the remainders in reverse order

    result = digits
    # remainder = digits % 16
    tmp_remainder = []
    tmp_hex = []

    while result > 0:
        remainder = digits % base
        tmp_remainder.append(remainder)
        result = int(digits / base)
        tmp_hex.append(string.hexdigits[remainder])
        print('LOOK HERE STUPID', tmp_hex)
        digits = result
    return tmp_hex[::-1]

    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()