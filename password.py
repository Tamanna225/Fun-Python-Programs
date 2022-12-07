#applying password to a program
x = input("enter passcode to access program: ")
if x == "qwerasdf":
    print("you have entered correct password")
    print("this program is related to the source code of this program. ")
    y = input("we want your identification: ")
    if y == "tamanna who made this":
        a = open("password.py","r")
        print(a.read())
    else:
        print("Wrong identification")
else:
    print("Wrong passcode entered")
input("press ENTER to exit")    







