# tuples is a data structure which is a immutable form of list
# tuples is faster than list
# if we don't need to alter data we can use tuples

# str tuples
a = ('mango', 'banana', 'apple')

# print a specific element
print(a[1])

# num tuples
b = (1, 2, 3, 4)
print(b)

# type print
print(type(b))

# mixed tuples
c = (1.3, 2, 3, 4.4, 'a', 'b', 'c')
print(c)

# slice a tuples
print(c[1:4])

# tuples and list are interchangeable

# tuple to list
new_list = list(c)
print(new_list)
print(type(new_list))

# list to tuple
new_tuple = tuple(new_list)
print(new_tuple)
print(type(new_tuple))
