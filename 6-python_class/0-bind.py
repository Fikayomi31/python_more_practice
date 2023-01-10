#!/usr/bin/python3
"""Binding of attribute to object"""
def bind(x):
    return 56

# binding the return value to variable x
bind.x = 56
print(bind.x)
