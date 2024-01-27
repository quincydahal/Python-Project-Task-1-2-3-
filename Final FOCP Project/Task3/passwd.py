import codecs
import getpass
def change():

    password_file_path = "passwd.txt"  #to store user information in format

    #reads the content of the password file
    def read_passwd_file():
        with codecs.open(password_file_path, 'r', encoding = "utf-8") as file:
            return file.readlines()

    #writes a list of lines to the password file    
    def write_passwd_file(lines):
        with codecs.open(password_file_path, 'w', encoding = "utf-8") as file:
            file.writelines(lines) 
            

    def change_password():
    #allows the user to change password    
        username = input("Enter your username: ").strip().lower()
        current_password = getpass.getpass("Enter your current password: ") 
        current_password = codecs.encode(current_password,'rot_13')
        
        lines = read_passwd_file()
        for index, line in enumerate(lines): 
            if line.startswith(f"{username}:"):
                _, real_name, encrypted_password = line.strip().split(":") #
                if current_password == encrypted_password: #verifies the current password
                    while True:
                        original_password = getpass.getpass("Enter your new password: ")
                        original_password = codecs.encode(original_password,'rot_13')
                        confirm_password = getpass.getpass("Confirm your new password: ")
                        confirm_password = codecs.encode(confirm_password,'rot_13')
                    
                        if original_password == confirm_password:#confirms the new password
                            
                            lines[index] = f"{username}:{real_name}:{confirm_password}\n"
                    
                            write_passwd_file(lines)
                            print("The password is changed successfully.")
                            return
                        else:
                            print("Error: New passwords do not match.")
                else:    
                    print("Error: Invalid current password.")  
                    return
        print("Error: Invalid Username")      
        
    change_password() 
change() 