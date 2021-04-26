"""
# movie list
fav_movie = []

while True:
    print('Enter the movie no '+str(len(fav_movie)+1)+' or press Enter to stop adding to the list.')
    movie = input()

    if movie == '':
        break
    fav_movie = fav_movie + [movie]

if len(fav_movie) != 0:
    print('The list of movies: ')
    for i in range(len(fav_movie)):
        print(fav_movie[i])
else:
    print('The list is empty.')

"""

"""
# in and not in keywords
my_tech = ['iphone', 'android', 'laptop', 'tab', 'tv']

print('Enter the name of a device:')
device = input()

if device not in my_tech:
    print(device+' is not in the list')
else:
    print(device+' is in the list')

"""

"""
# assume multiple values

burger = ['bun', 'cheese', 'meat', 'ketchup', 'mayo', 'egg']
a, b, c, d, e, f = burger
print(a, b, c, d, e, f)

"""

# str is also a list
# in str space are also count as a char
z = 'This is Sabrina'
print(z[4])
# strings are basically immutable forms of list, str can't be changed after creation, but list can be modified
# if we want to add, del, or modify we need to slice the str
