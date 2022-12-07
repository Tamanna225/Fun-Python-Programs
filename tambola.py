#random
import random
x = input("do you want me to be your caller in tambola?\na.yes\nb.no\n")
if x == "a":
    def tambola():
          print(random.randint(0,90))
          h = input("want to run again type r\n")
          if h == "r":
                tambola()
          else:
             print("thank you")
    tambola()     
    h = input("want to run again type r\n")
    if h == "r":
                tambola()
    else:
        print("thank you")      
elif x == "b":
    print("it's ok if you have another caller")
else:
    print("you have entered invalid input")
input("press ENTER to exit")    


          
