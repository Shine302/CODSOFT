import random
import string
#Colection of required elements in pasword
str1 = string.ascii_letters
str2 = string.digits
str3 = string.punctuation
element = str1 + str2 + str3

while 1:

#Title
    print("\nWelcome to Password generator")
    print("`````````````````````````````")

#Asking the user for password length
    pass_len = int(input("\nInput required length of the Password : "))

#Printing the pasword
    print("\nHere are some {} digit password: ".format(pass_len))
    for x in range(0,7):
        password = ""
        for y in range(0,pass_len):
            pass_char = random.choice(element)
            password = password + pass_char
        print("-----",password) 

#Asking the user for genaret more password
    dission = input("\nDo want more password?\n'Y' for Yes\n'N' for No\n: ").upper()
    if dission == 'Y':
        print("\nOk")         
    elif dission == 'N':
        print("\nThank you for using password generator")
        break    
    else:
        print("Invalid input")
        break