a=10
b=3
print("Sum:",a+b)
print("Diff:",a-b)
print("Product:",a*b)
print("Division:",a/b)
print("Modulo:",a%b)

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

a=14


a+=b
print("Sum is : ",a )
a-=b
print("Diff is : ",a )
a*=b
print("Product is : ",a )
a/=b
print("Division is : ",a )
a%=b
print("Modulo is : ",a )

a=False
b=True

if(a==False):
    print("Yeaaaa")
    
    if(b==True):
        print("Noooooo")
        
        if(a==False and b==True):
            print("Yeaaaa Noooooo")
            
            
            if(a==False or b==True):
                print("Helllllll Yeaaaaaaaa")
                
                print(not(a<b))
                print(not(a!=b))
