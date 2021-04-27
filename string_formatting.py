# old way of formatting strings -- C style

print('I am %s' % 'Sumona')
print('I am %s and I am %d years old' % ('Sumona', 23))

name = 'Nova'
age = 22
profession = 'Player'
earning = 245000.344
print('I am %s and I am %d years old. I am a %s and I earn %.2f$' % (name, age, profession, earning))

# a slightly better way of formatting strings, introduced in python 2.6
print('I am {} and I am {}'.format('Sumona', 'happy'))
print('I am {1} and I am {0}'.format(name, 'happy'))

# a much better way of formatting strings, introduced in python 3 and above
food = 'sandwich'
language = 'python'
# f string
print(f'I am {name} and I eat {food}. I don\'t believe in {language} haters\nAnd {2**2} == {4}')
