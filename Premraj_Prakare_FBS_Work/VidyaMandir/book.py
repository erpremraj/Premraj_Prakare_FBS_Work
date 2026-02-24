from prettytable import PrettyTable

class Book:
    def __init__(self, book_id=0, book_title=None, book_author=None, book_price=0, copies=0):
        self.book_id = int(book_id)
        self.book_title = book_title
        self.book_author = book_author
        self.book_price = int(book_price)
        self.copies = int(copies)

    # to display data in simple format
    # def add_book(self, book):
    #     self.books.append(book)
    def display(self):
        # table = PrettyTable([self.book_id,self.book_title,self.book_author,self.book_price,self.copies])
        print(f"Book id : {self.book_id}, Book title : {self.book_title}, Book author : {self.book_author}, Book price : ₹{self.book_price}, Book copies : {self.copies}")

    def __str__(self):  # to override __str__() method to avoid hashcode
        return f"Book id : {self.book_id}, Book title : {self.book_title}, Book author : {self.book_author}, Book price : {self.book_price}, Book copies : {self.copies}"

    def to_file(self):  # to write in txt file
        return f"{self.book_id}, {self.book_title}, {self.book_author}, {self.book_price}, {self.copies}"

# menu driven code
# its important to use this module menu drven code
# lakshat asu de mhanun
if (__name__ == "__main__"):
    # pass
    # books = []
    b1 = Book(101, "Python Programming", "Guiddo", 350, 2)  # sample
    # books.append(b1)
    b1.display()          # to call display() explicitly
    # print(b1)             # to call __str__() implicitly
