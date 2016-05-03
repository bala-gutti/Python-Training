#!/usr/bin/python

import collections

# this method is not advisable for large integers (overflow)
def finder(list1,list2):

    sumV = 0
    for x in list1:
        sumV += x
    for y in list2:
        sumV -= y

    print('missing element is : ',sumV)


def finder2(list1,list2):
    d = collections.defaultdict(int)

    for num in list2:
        d[num] += 1

    for num in list1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


 # use exclusive or XOR
def finder3(list1,list2):
    result = 0 
    for num in list1+list2:
        result^=num
        print(str(result))
        


finder3([1,2,3,4,5,6,7],[3,5,6,2,7,1])


