# files are used to store digital info
# we can read, write or update info of the files

# file modes:
# r = read
# r+ = read + write
# w = write (edit starts from the begin)
# w+ = write + read
# a = append(edit starts from the end)
# a+ = append + read

# open a file in write mode
"""
f = open('a.txt', 'w')
# here write mode creates & open a file if it does not exist
# and if exists it just writes
# getting file name
print('Name = ', f.name)

# getting file mode
print('Mode = ', f.mode)

# closed or not
# it's open so result is false
print('Is it closed? ', f.closed)

# write in write mode
f.write('This is Sabrina')

# closing
f.close()

# closed or not
# it's close now so result is true
print('Is it closed? ', f.closed)

"""

# appending a file
"""
f = open('a.txt', 'a')
# here append mode creates & open a file if it does not exist
# and if exists it just appends

# getting file mode
print('Mode = ', f.mode)


# write in append mode
f.write(' Sumona')

# closing
f.close()

"""

# read + a file
"""
f = open('a.txt', 'r+')

# getting file mode
print('Mode = ', f.mode)

# # read in read+ mode
# info = f.read()
# print(info)

# read up to a specific position in read+ mode
info = f.read(13)
print(info)

# write in read+ mode
f.write('. I love coding.')

# closing
f.close()

"""

# write + a file
f = open('a.txt', 'w+')

# write in write+ mode
# its rewrite all info & vanish previous
f.write('Hello SNS')

f.close()

"""
 The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
"""
