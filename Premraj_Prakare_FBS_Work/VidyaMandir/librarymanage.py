from book import Book
from prettytable import PrettyTable # import module prettytable class PrettyTable

class LibraryManage:

    # Show all users
    def show_users(self):
        try:
            table = PrettyTable(["Username", "Password"])
            found = False   # to check present or not
            # file handling to read all users
            with open("VidyaMandir/users.txt", "r") as fp:
                for line in fp:
                    if not line.strip():
                        continue
                    data = line.strip().split(", ")
                    table.add_row([data[0], data[1]])
                    found = True
            if found:
                print(table)
            else:
                print("No registered users")
        except FileNotFoundError:
            print("users.txt not found")
        except Exception as e:
            print(f"Error: {e}")

    # Add a new book
    def add_book(self):
        try:
            book_id = int(input("Book ID: "))
            book_title = input("Book Title: ")
            book_author = input("Book Author: ")
            book_price = int(input("Book Price: "))
            copies = int(input("Copies: "))

            book = Book(book_id, book_title, book_author, book_price, copies)
            # file handling auto create
            with open("VidyaMandir/bookDetails1.txt", "a") as fp:
                fp.write(book.to_file() + "\n")
            print("Book added successfully")
        except ValueError:
            print("Please enter valid numeric values")
        except Exception as e:
            print(f"Error: {e}")

    # Show all books
    def show_books(self):
        try:
            table = PrettyTable(["Book ID", "Title", "Author", "Price", "Copies"])
            found = False
            with open("VidyaMandir/bookDetails1.txt", "r") as fp:
                for line in fp:
                    if not line.strip():
                        continue
                    data = line.strip().split(", ")
                    table.add_row([int(data[0]), data[1], data[2], f"₹{int(data[3])}", int(data[4])])
                    found = True
            if found:
                print(table)
            else:
                print("No books available")
        except FileNotFoundError:
            print("bookDetails1.txt not found")
        except Exception as e:
            print(f"Error: {e}")

    # Search for a book by ID or Title
    def search_book(self):
        try:
            search = input("Enter Book ID or Title to search: ").strip()
            table = PrettyTable(["Book ID", "Title", "Author", "Price", "Copies"])
            found = False

            with open("VidyaMandir/bookDetails1.txt", "r") as fp:
                for line in fp:
                    if not line.strip():
                        continue
                    data = line.strip().split(", ")
                    book_id, title = int(data[0]), data[1]
                    # isdigit() to check it is digit or not (digit means number/integer)
                    # it present ten returns True otherwise False
                    if (search.isdigit() and int(search) == book_id) or search.lower() == title.lower():
                        table.add_row([book_id, title, data[2], f"₹{int(data[3])}", int(data[4])])
                        found = True

            if found:
                print("\n--- Book Found ---")
                print(table)
            else:
                print("No matching book found")
        except FileNotFoundError:
            print("bookDetails1.txt not found")
        except Exception as e:
            print(f"Error: {e}")

    # Update book details
    def update_book(self):
        try:
            book_id = int(input("Enter Book ID to update: "))
            books = []
            found = False

            with open("VidyaMandir/bookDetails1.txt", "r") as fp:
                for line in fp:
                    if not line.strip():
                        continue
                    data = line.strip().split(", ")
                    # book = Book(*data)
                    book = Book(
                                    int(data[0]),   # book_id
                                    data[1],        # book_title
                                    data[2],        # book_author
                                    int(data[3]),   # book_price
                                    int(data[4])    # copies
                                    )
                    if book.book_id == book_id:
                        print("Enter new details (leave blank to keep old value):")
                        title = input(f"Title ({book.book_title}): ")
                        author = input(f"Author ({book.book_author}): ")
                        price = input(f"Price ({book.book_price}): ")
                        copies = input(f"Copies ({book.copies}): ")
                        if title: book.book_title = title
                        if author: book.book_author = author
                        if price: book.book_price = int(price)
                        if copies: book.copies = int(copies)
                        found = True
                    books.append(book)

            if not found:
                print("Book not found")
                return

            with open("VidyaMandir/bookDetails1.txt", "w") as fp:
                for b in books:
                    fp.write(b.to_file() + "\n")
            print("Book updated successfully")

        except ValueError:
            print("Please enter valid numeric values")
        except FileNotFoundError:
            print("bookDetails1.txt not found")
        except Exception as e:
            print(f"Error: {e}")

    # Delete a book
    def delete_book(self):
        try:
            book_id = int(input("Enter Book ID to delete: "))
            books = []  # to store book details
            found = False   # is book present or not

            with open("VidyaMandir/bookDetails1.txt", "r") as fp:
                for line in fp:
                    if not line.strip():
                        continue
                    # data = line.strip().split(", ")
                    # book = Book(*data)
                    data = line.strip().split(", ")
                    book = Book(
                                    int(data[0]),   # book_id
                                    data[1],        # book_title
                                    data[2],        # book_author
                                    int(data[3]),   # book_price
                                    int(data[4])    # copies
                                )
                    if book.book_id != book_id:
                        books.append(book)  # adding in empty books
                    else:
                        found = True

            if not found:
                print("Book not found")
                return

            with open("VidyaMandir/bookDetails1.txt", "w") as fp:
                for b in books: # to check one by one and delete the book
                    fp.write(b.to_file() + "\n")
            print("Book deleted successfully")
        except ValueError:
            print("Please enter valid numeric values")
        except FileNotFoundError:
            print("bookDetails1.txt not found")
        except Exception as e:
            print(f"Error: {e}")