def x():
    num = int(input("Enter a non-negative number: "))
    x = 1
    for i in range(num):
        x=x*(i+1)
    print("factorial of",num,"is",x)
x()
h = input("do you want to calculate factorial of another number?\na.yes\nb.no\n")
if h == "a":
    x()
elif h == "b":
    print("Thank you")
else:
    print("i don't really know what you meant")
input("Press ENTER to exit")    
    
