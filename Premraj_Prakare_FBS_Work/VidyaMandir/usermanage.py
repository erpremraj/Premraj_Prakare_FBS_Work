from book import Book
from datetime import datetime
from librarymanage import LibraryManage

class UserManage:
    def __init__(self):
        self.username = None

    # User login
    def login(self):
        try:
            uname = input("Username: ")
            pwd = input("Password: ")
            with open("VidyaMandir/users.txt", "r") as fp:
                for line in fp:
                    if not line.strip():
                        continue
                    data = line.strip().split(", ")
                    if data[0] == uname and data[1] == pwd:
                        print(f"User '{uname}' login successful")
                        self.username = uname
                        return True
            print("Invalid credentials")
            return False
        except FileNotFoundError:
            print("User not found")
            return False

    # Register user
    def register(self):
        try:
            uname = input("Create username: ")
            pwd = input("Create password: ")
            with open("VidyaMandir/users.txt", "a") as fp:
                fp.write(f"{uname}, {pwd}\n")
            print(f"User '{uname}' registered successfully")
        except Exception as e:
            print(f"Error: {e}")

    # Borrow book
    def borrow_book(self):
        if not self.username:
            print("Login first to borrow books")
            return
        try:
            book_id = int(input("Enter Book ID to borrow: "))
            borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
            # borrow_date = datetime.strftime(borrow_date, "%Y-%m-%d")
            # borrow_date = datetime.date()
            borrow_date = datetime.strptime(borrow_date, "%Y-%m-%d")

            books = []
            found = False
            with open("VidyaMandir/bookDetails1.txt", "r") as fp:
                for line in fp:
                    if not line.strip():
                        continue
                    data = line.strip().split(", ")
                    book = Book(
                        int(data[0]),
                        data[1],
                        data[2],
                        int(data[3]),
                        int(data[4])
                    )
                    if (book.book_id == book_id):
                        found = True
                        if (book.copies > 0):
                            # Ask user to pay
                            print(f"The price of '{book.book_title}' is ₹{book.book_price}")
                            # pay amount from user
                            amount = input("Enter payment amount:₹ ")
                            try:
                                amount = int(amount)
                                if (amount == book.book_price):
                                    book.copies -= 1
                                    with open("VidyaMandir/borrow.txt", "a") as bp:
                                        bp.write(f"{self.username}, {book_id}, {book.book_title}, {book.book_author}, {borrow_date}\n")
                                    print("Payment successful. Book borrowed successfully!")
                                else:
                                    print("Payment failed — incorrect amount entered")
                            except ValueError:
                                print("Invalid amount entered — payment failed")
                        else:
                            print("Book unavailable")
                    books.append(book)

            if not found:
                print("Book not found")
                return

            # Update book file
            with open("VidyaMandir/bookDetails1.txt", "w") as fp:
                for b in books:
                    fp.write(b.to_file() + "\n")

        except ValueError:
            print("Invalid input")
        except FileNotFoundError:
            print("bookDetails1.txt not found")
        except Exception as e:
            print(f"Error: {e}")

    # Return book
    def return_book(self):
        if not self.username:
            print("Login first to return books")
            return

        try:
            # Step 1: Take Book ID input safely
            book_id_input = input("Enter Book ID to return: ")
            if not book_id_input.isdigit():
                print("Please enter a valid numeric Book ID")
                return
            return_id = int(book_id_input)

            fine = 0
            returned = False
            remaining_records = []

            # Step 2: Read borrow records
            with open("VidyaMandir/borrow.txt", "r") as fp:
                for line in fp:
                    if not line.strip():
                        continue
                    # Expecting format: username, book_id, book_title, book_author, borrow_date
                    uname, book_id_str, title, author, borrow_date_str = line.strip().split(", ")
                    book_id = int(book_id_str)

                    if uname == self.username and book_id == return_id and not returned:
                        # Step 3: Calculate fine
                        borrow_date_only = borrow_date_str.split()[0]  # remove time if present
                        borrow_date = datetime.strptime(borrow_date_only, "%Y-%m-%d")
                        days_diff = (datetime.now() - borrow_date).days

                        if days_diff <= 7:
                            fine = 0
                            print("Book returned on time. No fine.")
                            payment_required = False
                        else:
                            extra_days = days_diff - 7
                            weeks_late = extra_days // 7 + 1
                            fine = weeks_late * 100
                            print(f"Book returned late. Fine: ₹{fine}")
                            payment_required = True

                        # Step 4: Collect fine if needed
                        if payment_required:
                            amount_input = input(f"Enter payment amount to clear fine of ₹{fine}: ₹")
                            if not amount_input.isdigit():
                                print("Invalid amount. Book not returned.")
                                remaining_records.append(line.strip())
                                returned = True
                                continue

                            amount = int(amount_input)
                            if amount == fine:
                                print("Fine paid successfully. Book returned!")
                            else:
                                print("Payment failed — incorrect amount. Book not returned.")
                                remaining_records.append(line.strip())
                                returned = True
                                continue

                        # Mark as returned
                        returned = True
                    else:
                        remaining_records.append(line.strip())

            # Step 5: Handle no record found
            if not returned:
                print("No such borrowed book found")
                return

            # Step 6: Update borrow.txt
            with open("VidyaMandir/borrow.txt", "w") as fp:
                for record in remaining_records:
                    fp.write(record + "\n")

            # Step 7: Update book copies
            books = []
            with open("VidyaMandir/bookDetails1.txt", "r") as fp:
                for line in fp:
                    if not line.strip():
                        continue
                    data = line.strip().split(", ")
                    book = Book(
                        int(data[0]),
                        data[1],
                        data[2],
                        int(data[3]),
                        int(data[4])
                    )
                    if book.book_id == return_id:
                        book.copies += 1
                    books.append(book)

            with open("VidyaMandir/bookDetails1.txt", "w") as fp:
                for b in books:
                    fp.write(b.to_file() + "\n")

            # Step 8: Final message
            if fine == 0:
                print("Book returned successfully")
            else:
                print(f"Book returned successfully after fine payment: ₹{fine}")

        except FileNotFoundError:
            print("Required file not found")
        except Exception as e:
            print(f"Error: {e}")