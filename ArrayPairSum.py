#!/usr/bin/python

class ArrayPairSum(object):

    def pair_sum(self,value,listNum):
        
        if len(listNum) < 2:
            return False
        
        seen = set()
        output = set()

        for num in listNum:
            target  = value - num

            if target not in seen:
                seen.add(num)
            else:
                output.add((min(num,target),max(num,target)))

        # print '\n'.join(map(str,list(output)))
        print(output)

arr = ArrayPairSum()

arr.pair_sum(4,[1,2,3,3])



