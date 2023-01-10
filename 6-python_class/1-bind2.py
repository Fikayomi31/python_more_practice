#!/usr/bin/python3

"""Another way of using counter attribute"""
def bind(x):
    bind.counter = getattr(bind, 'counter', 0) + 1
    return "Monty Python"
for i in range(10):
    #will be incrumented by +1 for the loop
    bind(i)
print(bind.counter) #output will be 10
