class StoryBook:

    # CLASS VARIABLE
    no_of_books = 0

    discount = 0.5

    def __init__(self, name, price, author_name, author_born, no_of_pages):
        # setting the instance variables here
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.publishing_year = 2020
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books += 1

    # regular method 1
    def get_book_info(self):
        print(f'The book name: {self.name}, price: {self.price}, pages: {self.no_of_pages}')

    # regular method 2
    def get_author_info(self):
        print(f'The author name: {self.author_name}, born: {self.author_born}')

    # applying discount to an instance
    def apply_discount(self):
        self.price = int(self.price - self.price * StoryBook.discount)


# creating an instance/object of the StoryBook class
book_1 = StoryBook('Hamlet', 350, 'Shakespeare', 1564, 500)
book_2 = StoryBook('the_kite_runner', 200, 'khaled hosseini', 1965, 200)

# book_1.get_book_info()
# StoryBook.get_book_info(book_1)
#
# book_1.get_author_info()

# print(book_1.publishing_year)
# print(book_2.price)

# print(book_1.no_of_books)
# print(book_2.no_of_books)
# print(StoryBook.no_of_books)

print(book_2.price)
book_2.apply_discount()
print(book_2.price)




