import codecs
import getpass
def user_add():

    password_file_path = "passwd.txt"  #to store user information in format

    #reads the content of the password file
    def read_passwd_file():
        with codecs.open(password_file_path, 'r', encoding = "utf-8") as file:
            return file.readlines()

    #writes a list of lines to the password file    
    def write_passwd_file(lines):
        with codecs.open(password_file_path, 'w', encoding = "utf-8") as file:
            file.writelines(lines) 
            

    def add_user():
    #takes in input username,real name and password     
        username = input("Enter the Username: ").strip().lower()
        real_name = input("Enter the Real Name: ")
        password = getpass.getpass("Enter the Password: ") 
        password = codecs.encode(password,'rot_13')
        
        lines = read_passwd_file()
    #checks if username already exists    
        for line in lines:
            if line.startswith(f"{username}"+":"):
                print("Error: Username already exists.")
                return
                
        lines.append(f"{username}:{real_name}:{password}\n") 
        write_passwd_file(lines)
        print("User added successfully.")
        
    add_user()
user_add()
        