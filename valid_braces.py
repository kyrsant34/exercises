# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should
# return true if the string is valid, and false if it's invalid.
#
# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}.
# Thanks to @arnedag for the idea!
#
# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
#
# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.

def valid_braces(s):
    d = {'(': ')', '{': '}', '[': ']'}
    expected = []
    for ch in s:
        if ch in d:
            expected.append(d[ch])
        elif not expected or ch != expected.pop():
            return False

    return True

if __name__ == '__main__':
    assert valid_braces('(){}[]') is True
    assert valid_braces('([{}])') is True
    assert valid_braces('(}') is False
    assert valid_braces('[(])') is False
    assert valid_braces('[({})](]') is False
    assert valid_braces('))') is False
