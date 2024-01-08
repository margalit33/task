simp_called = False

def sum_of_digits(n):
    global simp_called
    if not simp_called:
        raise ValueError("Please call a function from 'simp' module before using 'comp'")
    return sum(int(digit) for digit in str(n) if digit.isdigit())

def is_palindrome(n):
    global simp_called
    if not simp_called:
        raise ValueError("Please call a function from 'simp' module before using 'comp'")
    return str(n) == str(n)[::-1]




# def sum_of_digits(number):
#     return sum(int(digit) for digit in str(number) if digit.isdigit())

# def is_palindrome(number):
#     return str(number) == str(number)[::-1]
