# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given
# numbers differs from the others. Bob observed that one number usually differs from the others in evenness.
# Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different
# in evenness, and return a position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start
# from 1 (not 0)

# https://www.codewars.com/kata/iq-test/train/python
from collections import defaultdict

def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


if __name__ == '__main__':
    assert iq_test("2 4 7 8 10") == 3
    assert iq_test("1 2 2") == 1
    assert iq_test("1 2 1 1") == 2
