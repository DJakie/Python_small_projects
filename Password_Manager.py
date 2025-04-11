## PASSWORD MANAGER WITH ENCRYPTION


from cryptography.fernet import Fernet  #Module to encrpyt text

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:   #wb is write bytes mode
        key_file.write(key) '''

def load_key():
    file = open("key.key", "rb")  # rb is read bytes mode
    key = file.read()             # reading the key from the file
    file.close()                  # closing the file
    return key

key = load_key()         # calling the load key function to get the key
fer = Fernet(key)        # initailizing the encryption model

    
def view():
    with open("passwords.txt","r") as file:
        for line in file.readlines():      # reading each line from the file
            data = line.rstrip()           # stripping the gap created by /n
            user, passw = data.split("|")  # splitting the line into user and password
            print(f"User: {user}, Password: {fer.decrypt(passw.encode()).decode()}")  # encoding the password into bytes to decrpyt it and the decoding it to return string

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt","a") as file:     # w makes new file clearing old file, r is read mode, a is append mode
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") # encoding into bytes to encrypt and then decoding to string

# loop to carry out the whole process
while True:
    mode = input("Would you like to add a new password or view existing password? (view/add) or press q to quit ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add() 
    else:
        print("Invalid Mode.")
        continue