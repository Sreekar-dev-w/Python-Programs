import random 
number=random.randint(1, 50)
attempts=0

while True:
    guess=int(input("Guess the number between 1 to 50 : "))
    attempts+=1
    
    if guess<number:
        print("Too low")
    
    elif guess>number:
        print("Too high")
     
    else:
        print("Correct")
    
    print("Attempts : ")
    
    break        