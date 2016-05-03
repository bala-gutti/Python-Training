#!/usr/bin/python

def func_constant(values):
    print(values[0])

def func_lin(values):
    for x in values:
        print(x)

def func_quad(values):
    for item_1 in values:
        for item_2 in values:
            print(item_1,item_2)


lst = [1,2,3,4,5]

func_constant(lst)

func_lin(lst)

func_quad(lst)
