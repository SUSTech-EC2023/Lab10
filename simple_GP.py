import random
import matplotlib.pyplot as plt

# Define the target function
def target_function(x):
    return x**2 + x + 1

# Define primitive functions
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

# TODO: implement a simple GP algorithm here to find an expression with one input (independent variable x), whose output equals the value of the target function