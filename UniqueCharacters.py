#!/usr/bin/python

def uni_Chars(s):

    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)

    return True

print(uni_Chars('abcdefg'))

print(uni_Chars('abcdefgggg'))

