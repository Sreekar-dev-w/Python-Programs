# We store the first 100 digits of Pi in a tuple 📦
# Position 0 = 3, Position 1 = 1, Position 2 = 4...
pi_tuple = (
    3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 
    6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 
    1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 
    4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 
    9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9
)

# User Input ⌨️
try:
    n = int(input("Enter the position (0-100) to find the digit: "))
    
    # Accessing the digit directly using the index [n] 🎯
    digit = pi_tuple[n]
    
    print(f"The digit at position {n} is {digit}! ✅")
    
except IndexError:
    print("Oops! I only have 100 digits stored. 🛑")
except ValueError:
    print("Please enter a valid whole number! ❌")

# import math
# n=int(input())
# b=math.pi*(10**(n-1))
# c=int(b%10)
# print(c)