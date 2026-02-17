num=input("Enter numbers separated by commas: ")

parts=num.split(",")

numbers=[]

for i in parts:
    try:
        num=int(i)
        numbers.append(num)
    
    except ValueError as e :
        print(e)
        continue
    
if numbers:
    print("Valid numbers:", numbers)
    print("Sum:", sum(numbers))
    print("Largest:", max(numbers))
    print("Smallest:", min(numbers))
else:
    print("No valid integers found.")
    