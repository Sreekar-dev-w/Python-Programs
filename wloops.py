#First example
i=1
n=int(input("Enter n: "))
while i<=10:
        print("{} x {} = {}".format(n, i, n*i))
        i += 1
    
    #Second example
i=1
while i**2 <=100:
     print(i**2)
     i +=1   
print("Done")

#Third example

i=0
tup=[1,4,9,16,25,36,49,64,81,100]
n=int(input("Enter finding element : "))
while i<len(tup):
    if tup[i]==n:
        print("Element found at index : ",i)
        break
    i +=1
else:
    print("Element not found")
    
print("Done")

#Fourth example

n=int(input("Enter n: "))
i=0
s=0
while i<=n:
    s+=i
    i+=1
print("Sum of first {} natural numbers is : {}".format(n,s))

#Fifth example

n=int(input("Enter n: "))
f=1
for i in range(1,n+1):
    f=f*i
    print("Factorial of {} is : {}".format(n,f))
    
print("Dobbey if you entered number between 1 and ∞")
    