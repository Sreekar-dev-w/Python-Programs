num=input("Enter a number: ")

special_chars = "!@#$%^&*()_+-"
try:
    for ch in str(num):
       if ch in special_chars:
        print("Special character")
        break
       elif ch.isdigit():
        print("Digit")
       elif ch.islower():
        print("Lowercase")
       elif ch.isupper():
        print("Uppercase")
       else:
        print("Invalid input")
        
except ValueError:
    print("Invalid input: Please enter a valid number.")