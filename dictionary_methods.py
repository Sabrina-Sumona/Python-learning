a = {1: 100, 4: 400, 3: 300, 2: 200}

# values method
"""
for i in a.values():
    print(i)
"""

# keys method
"""
for i in a.keys():
    print(i)
"""

# items method
# both key & value
"""
for i in a.items():
    print(i)
"""

# make a list of values
"""
b = list(a.values())
print(b)
"""

# make a list of keys
"""
c = list(a.keys())
print(c)
"""

# a handy trick
"""
for i, j in a.items():
    print('key: '+str(i)+', value: '+str(j))
"""

# in keyword
# by default checks key
"""
print(1 in a)
print(5 in a)
print(100 in a.values())
print(900 in a.values())
print(3 in a.keys())
"""

# get method
# get(key, default_value)
# it checks key, if exists it prints it's value else prints a certain value
"""
print(str(a.get(3, 404)))
print(str(a.get(9, 201)))
print(a)
"""

# setdefault method
# setdefault(key, value)
# it checks key, if exists it prints it's value else  it adds
print(str(a.setdefault(3, 404)))
print(str(a.setdefault(9, 201)))
print(a)
