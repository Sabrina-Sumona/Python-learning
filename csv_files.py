# CSV (Comma Separated Value)
# it's similar to spreadsheet
# it stores info row-wise and separate them by using comma
# it is used to fetch data from a database
# csv uses similar methods like normal files

import csv

# read

"""

file = open('example.csv')

# creating csv file reader obj
file_reader = csv.reader(file)

print(file_reader)

# converting file reader obj into list
data = list(file_reader)
print(data)
# now we can print specific info according to index
print(data[0][2])

# fetching info using loop
for row in file_reader:
    print("Row_"+str(file_reader.line_num)+': '+str(row))

file.close()

"""

# write

"""

output_file = open('output.csv', 'w', newline = '')
# newline will be create automatically after each row

# output_file = open('output.csv', 'w', newline = '')
# here we can modify the newline option & '' means there will be no new line after each rows

# output_writer = csv.writer(output_file)

# in csv by default comma is used, but we can also modify it by using delimiter
output_writer = csv.writer(output_file, delimiter = ';')
output_writer = csv.writer(output_file, delimiter = ' ')

output_writer.writerow(['1', '2', '3'])
output_writer.writerow(['3', '2', '1'])

output_file.close()

"""

# append

output_file = open('output.csv', 'a', newline = '')

output_writer = csv.writer(output_file, delimiter = ' ')

output_writer.writerow(['11', '12', '13'])
output_writer.writerow(['23', '22', '21'])

output_file.close()
