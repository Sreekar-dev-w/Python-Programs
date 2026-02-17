# As a programmer never use spaces in your code but use ( _ )instead and even in  folder names or variable names 

#First expample

def calc_sum(a,b):
    return a+b

print(calc_sum(5,6))

#Second example

n=int(input("Enter the number of inputs: "))
res=[]
for i in range(n):
    num=int(input("Enter a number:"))
    res.append(num)

resul=list(filter(lambda x: x>=10,res)) #Instead of these line from 16 to 21 we can write one single line using list comprehension

def cal(resul):
    return resul**3

resu=list(map(cal,resul))

print(resu)

print("Letssss Gooooooooooooooo")

#Third example 

n=int(input("Enter the number of inputs: "))
res=[]
for i in range(n):
    num=int(input("Enter a number:"))
    res.append(num)
    
resu=[x**3 for x in res if x>=10] #This is the line which is equivalent to lines 16 to 21
    
print(resu)


#Fourth example


def f(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
    
num=int(input("Enter a number: "))
f(num)




def f(stock):
    if(stock==0 or stock==1):
        return 1
    
    elif stock<0:
        raise ValueError("Dobbey")
    
    else:
        return stock*f(stock-1)
try:   
    turbo=int(input("Enter a number : "))

    print(f"Factorial = {f(turbo)}")

except ValueError as e:
   print(e)












