# VidyaMandir/main.py
# main.py
from librarymanage import LibraryManage
from usermanage import UserManage

admin = LibraryManage()
user = UserManage()

def admin_login():
    # admin credentails hard values # uname == "admin" and pwd == "admin1234"
    try:
        print(f"You chose Admin login")
        uname = input("Admin Username: ")
        pwd = input("Admin Password: ")
        print(f"you entered admin username : {uname} and admin password : {pwd}")
        if uname == "admin" and pwd == "admin1234":
            print("Admin login successful")
            # admin.add_book()
            # admin.update_book()
            # admin.show_books()
            # admin.delete_book()
            return True
        else:
            print("Incorrect admin credentials")
            return False
    except Exception as e:
        print(f"Exception : {e}")
        return False


ch = 0
while(True): # while ch != "4":
    print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
    print("                                                   ᴠɪᴅʏᴀᴍᴀɴᴅɪʀ                       ")
    print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")

    print("\t\t1. Admin Login\t\t2. User Login\t\t3. Register User\t\t4. Exit\n")

    ch = input("Enter your choice: ")
    # ADMIN LOGIN
    if ch == "1":
        if admin_login():
            a = 0
            while a != "7":
                print("\n✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨ Admin menu ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
                print("     1. Add Book\t2. Show Books\t3. Search Book\t4. Update Book\t5. Delete Book\t6. Show Users\t7. Logout")       # logout option
                a = input("\nEnter your choice: ")

                if a == "1":
                    admin.add_book()    # admin is object of LibraryManage()
                elif a == "2":
                    admin.show_books()
                elif(a == "3"):
                    admin.search_book()
                elif a == "4":
                    admin.update_book()
                elif a == "5":
                    admin.delete_book()
                elif a == "6":
                    admin.show_users()    # new function
                elif a == "7":
                    print("Admin has been logged out\n")
                    # break
                else:
                    print("Invalid choice")


    # USER LOGIN
    elif ch == "2":
        if user.login():    # user is object of UserManage()
            print(f"\nYou chose User login")
            u = 0
            while u != "5":
                print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨ User menu ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
                print("   1. Borrow Book\t\t2. Return Book\t\t3. Search Book\t\t4. Show Books\t\t5. Logout")
                # print("")
                # print("")
                # print("")
                # print("")

                u = input("Enter your choice: ")

                if u == "1":
                    user.borrow_book()
                elif u == "2":
                    user.return_book()
                elif(u == "3"):
                    admin.search_book()
                elif(u == "4"):
                    admin.show_books()
                elif u == "5":
                    print("User logged out")
                    # break
                else:
                    print("Invalid choice")

    # REGISTER AS USER
    # random username to register
    # users_data = [
    # ("prem", "prem@123")
    # ("ruchi_rai", "Ruchi@123"),
    # ("ananya_singh", "Ananya@456"),
    # ("vishal_kumar", "Vishal@789"),
    # ("priya_mehta", "Priya@321"),
    # ("amit_joshi", "Amit@654")
    # ]
    elif ch == "3":
        print("\n✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨ User Register ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
        print(f"\nYou chose Register User")
        user.register()     # ser is object of UserManage()

    elif ch == "4":
        print("\t\t\t\t\t    Thank You, Visit Again!!")
        print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
        print("\n\t\t\t\t\t\t    Sayonara!\n")
        print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
        break

    else:
        print("Invalid choice")

