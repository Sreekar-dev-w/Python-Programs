# Check if a person is a minor or an adult based on their age
# and it even checks for invalid age input

age = int(input("Enter your age: "))
if age<0:
    print("Invalid age")
elif age<18:
    print("You are a minor")

else:
    print("You are an adult")