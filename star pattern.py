# for printing a star pattern
x = eval(input("enter maximum number of stars you want in a line in pattern: "))
for i in range(0,x):
    for j in range(0,i+1):
        print("*",end = "")
    print()
input("press ENTER to exit")    
    
