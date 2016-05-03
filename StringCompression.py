#!/usr/bin/python

def CompressString(val):

    result = ""
    l = len(val)

    if l == 0:
        return ""
    if l ==1:
        return val + "1"
    
    last = val[0]
    count = 1
    i = 1
    while i < l:
        if val[i] == val[i-1]:
            count += 1
        else:
            result = result + val[i-1] + str(count)
            count = 1

        i += 1
    
    result = result + val[i-1] + str(count)

    print(result)

CompressString('AAAAABBBBBBBBBBCCCCC')



