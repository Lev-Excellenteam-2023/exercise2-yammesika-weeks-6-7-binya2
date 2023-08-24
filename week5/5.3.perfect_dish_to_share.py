def is_perfect_number(value):
    """
    Returns True if value is a perfect number, the sum of the proper divisors of n is equal to value.
    """
    divisors = [num  for num  in range(1, value ) if n % num  == 0 and i != value ]
    return sum(divisors) == value


if __name__ == '__main__':
    i = 1
    while True:
        if is_perfect_number(i):
            print(i)
        i += 1
