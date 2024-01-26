def del_user():
    import codecs
    import getpass

    password_file_path = "passwd.txt"  #to store user information in format

    #reads the content of the password file
    def read_passwd_file():
        with codecs.open(password_file_path, 'r', encoding = "utf-8") as file:
            return file.readlines()

    #writes a list of lines to the password file    
    def write_passwd_file(lines):
        with codecs.open(password_file_path, 'w', encoding = "utf-8") as file:
            file.writelines(lines) 
            
    def delete_user():
    #deletes user from the file by comparing username    
        username = input("Enter the username to delete: ").strip().lower()
        
        lines = read_passwd_file()
        next_lines =  [line for line in lines if not line.startswith(f"{username}:")]  
        
        if len(next_lines) == len(lines):
            print("No user found with that username.")
        else:
            write_passwd_file(next_lines) 
            print("User deleted successfully.")   
    
    delete_user()