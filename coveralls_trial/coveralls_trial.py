# -*- coding: utf-8 -*-

def foo():
    return True

def bar():
    return False

x = 2
def baz():
    if x:
        return x**2
    elif x == 0:
        return x + 17
    else:
        return x
