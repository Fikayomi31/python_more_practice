#!/usr/bin/python3
"""Binding of attribute to object"""
def bind(x):
    return 56

# binding the return value to variable x
bind.t = 5
bind.i = 56
print(bind.i)
print(bind.t)
