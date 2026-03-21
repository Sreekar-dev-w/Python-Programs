#This program find the first non repeated character in a string

def first_non_repeated_character(s):
    char_count = {}
    
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    
    for char in s:
        if char_count[char] == 1:
            return char
            
    return None  

input_string = input("Enter a string: ")
result = first_non_repeated_character(input_string)
if result:
    print(f"The first non-repeated character is: {result}")
else:
    print("There are no non-repeated characters in the string.")