class StoryBook:

    def __init__(self, name, price, author_name, author_born):
        # print('This is called when the object is being created!')
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born

    def get_author_description(self):
        print(f'The author is {self.author_name} and was born in {self.author_born}')


# creating an object or instance of the class
book_1 = StoryBook('Hamlet', 300, 'Shakespeare', 1564)
book_2 = StoryBook('the_kite_runner', 450, 'Khaled Hosseini', 1965)
book_2.get_author_description()
StoryBook.get_author_description(book_1)
# print(book_1)

# instance variables
# book_1.name = 'hamlet'
# book_1.price = 350
# book_1.author = 'Shakespeare'
#
# book_2.name = 'the_kite_runner'
# book_2.price = 450
# book_2.author = 'Khaled Hosseini'

print(book_1.name)
print(book_1.author_name)
print(book_1.price)

