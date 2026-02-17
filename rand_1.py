stock=int(input("Enter a number: "))

if stock%2==0:
    print("Even")
else:
    print("Odd")
    
if stock <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(stock**0.5) + 1):
        if stock % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

        
        
if str(stock )== str(stock)[::-1]:
    print("Palindrome")
    
else:
    print("Not Palindrome")
    
turbo=stock
diecast = len(str(stock))
supercharged=0

while turbo>0:
    diesel=turbo%10
    supercharged+=diesel**diecast
    turbo//=10
    
if supercharged==stock:
    print("Armstrong")
else:
    print("Not Armstrong")
    