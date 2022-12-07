#dice
import random
x = input("have you lost you dice aand want to play a dice game\na.yes\nb.no\n")
if x== "a":
    def dice():
        print(random.randint(1,6))
        g = input("want to run again type r\n")
        if g == "r":
               dice()
        else:
             print("Thank you")
    dice()         
    g = input("want to run again type r\n")
    if g == "r":
              dice()
    else:
        print("Thank you")
elif x == "b":
    print("it's ok you have dice")
else:
    print("you have entered invalid input")
input("Press ENTER to exit")
