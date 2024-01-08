from .numbers.simp import add_numbers, subtract_numbers
from .numbers.comp import sum_of_digits, is_palindrome
from .col import myzip


def main():
    result_add = add_numbers(5, 3)
    result_subtract = subtract_numbers(10, 4)

    print("Addition result:", result_add)
    print("Subtraction result:", result_subtract)

    number = 12321
    print("Sum of digits:", sum_of_digits(number))
    print("Is palindrome?", is_palindrome(number))

    # Example usage of myzip function
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    zipped = myzip(list1, list2)
    print("Zipped result:", list(zipped))

if __name__ == "__main__":
    main()







def main():
    result_add = add_numbers(5, 3)
    result_subtract = subtract_numbers(10, 4)

    print("Addition result:", result_add)
    print("Subtraction result:", result_subtract)

    number = 12321
    print("Sum of digits:", sum_of_digits(number))
    print("Is palindrome?", is_palindrome(number))

if __name__ == "__main__":
    main()
