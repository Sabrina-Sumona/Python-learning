"""
# in dictionaries index can be fixed by any no., char or str
# dict = {key : value}
# here key is similar to index
# so it is more flexible than list
# it is similar to hash table in other language
# we can not slice a dictionary
"""
# we can use key to print it's value

"""
my_dict = {'laptop': 'acer', 'mobile': 'samsung', 'calculator': 'casio', 'shoe': 'apex'}
print(my_dict['mobile'])

# int value & int key
a = {0: 100, 1: 200, 3: 400, 4: 500}
print(a[1])

"""

# dictionary is orderless, where list is not

"""

m = [1, 2, 3]
n = [3, 1, 2]

print(m == n)

r = {1: 200, 2: 300, 3: 500}
s = {3: 500, 1: 200, 2: 300}

print(r == s)

"""

# concat 2 dictionaries

d1 = {1: 100, 4: 400, 3: 300, 2: 200}
d2 = {5: 500, 7: 700, 8: 800, 6: 600}

D = d1.copy()
D.update(d2)

print(D)
