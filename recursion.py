#!python

def factorial(n):
    """factorial(n) returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n"""
    # check if n is negative or not an integer (invalid input)
    if not isinstance(n, int) or n < 0:
        raise ValueError('factorial is undefined for n = {}'.format(n))
    # implement factorial_iterative and factorial_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return factorial_iterative(n)
    # return factorial_recursive(n)


def factorial_iterative(n):
    # TODO: implement the factorial function iteratively here
    # TODO: Annotate functions with complexity analysis of running time and space (memory)
    # Time - O(n) Space - O(n)
    total = 1
    for num in range(1, n):
        if n > 1:
            print('HERE DUM DUM', num)
            # num + 1 is used to account for range going up to but not hitting n
            total *= (num + 1)
            print('LOOK', total)
    return total

    # once implemented, change factorial (above) to call factorial_iterative
    # to verify that your iterative implementation passes all tests


def factorial_recursive(n):
    # TODO: Annotate functions with complexity analysis of running time and space (memory)
    # Time - O(1) Space - O(n)
    # check if n is one of the base cases
    if n == 0 or n == 1:
        return 1
    # check if n is an integer larger than the base cases
    elif n > 1:
        # call function recursively
        return n * factorial_recursive(n - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()