import re
import unittest

def sumNums(fileName):
    file = open(fileName, 'r')
    lst = []
    for line in file:
        line = line.rstrip()
        x = re.findall('[0-9]+', line)
        if len(x) > 0:
            lst = lst + x
    total = 0
    for num in lst:
        total = total + int(num)
    file.close()
    return total

def countWord(fileName, word):
    file = open(fileName, 'r')
    lst = []
    str1 = r"\b" + word + r"\b"
    for line in file:
        x = re.findall(str1, line.lower())
        if len(x) > 0:
            lst = lst + x
    return len(lst)

def listURLs(fileName):
    file = open(fileName, 'r')
    lst = []
    str1 = "\S+w[.]\S+[.]\S+"
    for line in file:
        x = re.findall(str1, line)
        if len(x) > 0:
            lst = lst + x
    return lst


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
