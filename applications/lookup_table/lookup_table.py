# Your code here
import math
import random

# create a lookup table
lookup = {}

# check table for key(x, y)
# if present, return value
# else, calculate, add value to lookup table 
# return value



def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    key = (x, y)
    # check table for key(x,y)
    if key not in lookup:
        # if not present, calculate => slowfun_too_slow add value to table and return value
        lookup[key] = slowfun_too_slow(x, y)
    # if present, return value
    return lookup[key]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
