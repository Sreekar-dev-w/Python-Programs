from math import sqrt

n=int(input("Enter the number: "))

if n>0:
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            print(f"{n} is not a prime number.")
            break
        
    else:
        print(f"{n} is a prime number.")
        
else:
    print("Please enter a positive integer.")

print("Program ended.")
