#to add, subtract , multiply or divide two numbers
t = eval(input("enter a number: \n"))
m = eval(input("enter another number: \n"))         
x = input("what you want to do with numbers?\t(Note:choose one option)\n\na.add two nubers\nb.subtract two numbers\nc.multiply two numbers\nd.divide two numbers\ne.do all of the above\n\n")
if x == "a":
    print("\nsum of two numbers is ",t+m)
elif x == "b":
    print("\ndifference of two numbers is ",t-m)
elif x == "c":
    print("\nproduct of two numbers is ",t*m)
elif x == "b":
    print("\ndivision of two numbers is ",t/m)
elif x =="e":
    print("\nsum of two numbers is ",t+m)
    print("difference of two numbers is ",t-m)
    print("product of two numbers is ",t*m)
    print("division of two numbers is ",t/m)
else:
    print("you have not entered a valid input")
input("Press ENTER to exit")    
