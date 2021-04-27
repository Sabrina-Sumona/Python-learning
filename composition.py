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


class Library:
    def __init__(self, book_list=None):
        if book_list is None:
            self.book_list = []
        else:
            self.book_list = book_list

    def get_all_books(self):
        for book in self.book_list:
            print(f'Title: {book.name}, Author: {book.author_name}, Price:{book.price}')

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, book):
        self.book_list.remove(book)


# creating an instance/object of the StoryBook class
book_1 = StoryBook('Hamlet', 350, 'Shakespeare', 1564, 500)
book_2 = StoryBook('the_kite_runner', 200, 'khaled hosseini', 1965, 200)

public_library = Library()

public_library.add_book(book_1)
public_library.add_book(book_2)

public_library.get_all_books()

public_library.remove_book(book_2)

public_library.get_all_books()









