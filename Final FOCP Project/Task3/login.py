import codecs
import getpass
def login():

    password_file_path = "passwd.txt"  #to store user information in format

    #reads the content of the password file
    def read_passwd_file():
        with codecs.open(password_file_path, 'r', encoding = "utf-8") as file:
            return file.readlines()

    #writes a list of lines to the password file    
    def write_passwd_file(lines):
        with codecs.open(password_file_path, 'w', encoding = "utf-8") as file:
            file.writelines(lines) 
            
    def login_user():
        username = input("Enter your username: ").strip().lower()
        password = getpass.getpass("Enter your password: ")
        password = codecs.encode(password,'rot_13')
        lines = read_passwd_file()
        for line in lines:
            if line.startswith(f"{username}:"):#to check if the entered username and password match any existing user in the pw file
                _, _, encrypted_password = line.strip().split(":")
                if password == encrypted_password:
                    print("Login Successful.")
                    return
        print("Login failed. Invalid username or password.")        
                    
    login_user()
login()