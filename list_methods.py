place_visited = ['Bangladesh', 'India', 'bali', 'Nepal', 'thailand', 'Malaysia', 'maldives', 'Bhutan', 'USA', 'Australia']

"""
#  index method
print(place_visited.index('Bhutan'))

# append method to add element at last of the list
place_visited.append('Pakistan')
print(place_visited)

# insert method
# insert(index, value)
place_visited.insert(2, 'UK')
print(place_visited)

# remove method
place_visited.remove('Nepal')
print(place_visited)

# sort method

# ascending sort

# by default ascending sort capital letters , then small letters
place_visited.sort()
print(place_visited)

# ascending sort capital letters  & small letters both by converting them into lower case
place_visited.sort(key = str.lower)
print(place_visited)

# ascending sort capital letters  & small letters both by converting them into upper case
place_visited.sort(key = str.upper)
print(place_visited)

# descending sort

# descending sort small letters , then capital letters
place_visited.sort(reverse = True)
print(place_visited)

# descending sort capital letters  & small letters both by converting them into lower case
place_visited.sort(key = str.lower, reverse = True)
print(place_visited)

# descending sort capital letters  & small letters both by converting them into upper case
place_visited.sort(key = str.upper, reverse = True)
print(place_visited)

"""
