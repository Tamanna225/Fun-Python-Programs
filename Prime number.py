#To find wheather a number is prime or not
x = input("Do you want to know wheather your number is Prime or not?")
if x=="yes":    
    num = eval(input("Enter a number: "))
    for i in range(2,num):
        if num%i==0:
            print("It's not a Prime number")
            break
        else:
            print("It's a Prime number")
            break
elif x=="no":
    print("It's Ok")
else:
    print("You haven't entered valied input")
input("Press ENTER to exit")    
