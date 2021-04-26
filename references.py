# reference is var which holds a location of another var and uses to point a certain memory of the var
# list reference uses to point a list

"""
# here a ref the list
a = [1, 2, 3, 4]

# now ref is copied from a to b
b = a

# if we alter b then the list will be changed
# because we don't change the referenced values
# so a or b both will ref the modified list
b[1] = 5
print(a)

# ref changing function example
def f(n):
    n.append('new')

m = ['old', 'brand_new']
f(m)

print(m)

"""

# so if we copy a list it can be troublesome, it don't want to alter
# for solving this, we can create a new list instead of coping and modify that list
# or we can copy by importing built-in function copy

"""

import copy as cp

a = [1, 2, 3, 4]
b = cp.copy(a)
b[1] = 5
print(a)
print(b)

# function example

def f(n):
    n.append('new')
    print(n)

m = ['old', 'brand_new']
f(cp.copy(m))

print(m)

"""

# we can use deepcopy for nested list
# working of copy & deepcopy are the same

import copy as cp

a = [[1, 2], 3, 4]
b = cp.deepcopy(a)
b[1] = 5
print(a)
print(b)

# function example

def f(n):
    n.append('new')
    print(n)

m = [['old', 'antique'], 'brand_new']
f(cp.deepcopy(m))

print(m)
