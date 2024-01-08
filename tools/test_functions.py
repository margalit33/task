from .numbers.simp import add_numbers, subtract_numbers
from .numbers.comp import sum_of_digits, is_palindrome
from .col import myzip


def test_all_functions():
    # Test functions from simp.py
    result_add = add_numbers(5, 3)
    result_subtract = subtract_numbers(10, 4)
    assert result_add == 8
    assert result_subtract == 6

    # Test functions from comp.py
    assert sum_of_digits(123) == 6
    assert is_palindrome(12321) == True

    # Test myzip function from col.py
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    zipped = myzip(list1, list2)
    assert list(zipped) == [(1, 'a'), (2, 'b'), (3, 'c')]

    print("All functions passed the test.")

if __name__ == "__main__":
    test_all_functions()

