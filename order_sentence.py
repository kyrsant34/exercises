# Your task is to sort a given string. Each word in the string will contain a single number.
# This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input String will only contain valid
# consecutive numbers.

def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda word: int(''.join(filter(str.isdigit, word)))))

if __name__ == '__main__':
    assert order("is2 Thi12s T4est 3a") == "is2 3a T4est Thi12s"
    assert order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
    assert order("") == ""
