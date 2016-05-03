#!/usr/bin/python
import sys
from nose.tools import assert_equal

class Anagram():

    def __init__(self,strone,strtwo):
        #print('am here')
        self.str1 = strone
        self.str2 = strtwo

    def _isAnagram(self):
        self.lettersCount = dict()
        
        if len(self.str1) != len(self.str2):
            return False

        for x in self.str1:
            if x == ' ':
                continue
            if x in self.lettersCount:
                self.lettersCount[x] += 1
            else:
                self.lettersCount[x] = 1

        for y in self.str2:
            if y == ' ':
                continue
            if y in self.lettersCount:
                self.lettersCount[y] -= 1
            else:
                self.lettersCount[y] = 1

        for x in self.lettersCount:
            if self.lettersCount[x] != 0:
                return False
            #print("{} : {} ".format(x,self.lettersCount[x]))
        return True

    def testCode(self):
        assert_equal(self._isAnagram(),True)
        print('Successfully passed')

#ana = Anagram('clint eastwood','old west action')
ana = Anagram(sys.argv[1].lower(),sys.argv[2].lower())
ana.testCode()

