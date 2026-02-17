#First example

tu = (1,4,9,16,25,36,49,64,81,100)
for i in tu:
    print(i)
    i+=1
    
else:
    print("Dobbey")
    
    #Second example
    
for i in range(5):
    
    if(i==4):
        break
    print(i)
else:
    print("Dobbey")
    
    
    #Third example

for i in range(1,10,4):
    if(i==9):
        break
    print(i)

else:
    print("Dobbey")
    
    #Fourth example
    
for i in range(1,100,1):
    if(i%2!=0):
     print(i)
else:
    print("Dobbey")
    
    
for i in range(1,100,1):
    if(i%2==0):
     print(i)
else:
    print("Dobbey")
    
    #Fifth example
    
n=int(input("Enter n: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

else:
    print("Dobbey")

print("Done")
    
    
    
    
