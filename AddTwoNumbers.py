#!/usr/bin/python
from nose.tools import assert_equal

def solution(num1,num2):
    return num1+num2

class SolutionTest(object):
    def test(self,sol):
        assert_equal(sol(2,2),4)
        assert_equal(sol(4,4),8)
	
        print("all test cases passed")
	
t=SolutionTest()
t.test(solution)


