import adduser, deluser, login, passwd
if __name__ == "__main__":
        while True:
            
            choice = input("Enter Command: ")
            
            if choice == "adduser":
                adduser.user_add()
            elif choice == "deluser":
                deluser.del_user()
            elif choice == "passwd":
                passwd.change()
            elif choice == "login":
                login.login()
            elif choice == "exit":
                print("Exit program.")
                break        
            else:
                print("Invalid choice.")
                print("Commands: adduser, deluser, passwd, login, exit")
            
                           
                