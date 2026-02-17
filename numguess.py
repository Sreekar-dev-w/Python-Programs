import random 
number=random.randint(1, 500)
attempts=0

while True:
    guess=int(input("Guess the number between 1 to 500 : "))
    attempts+=1
    
    if guess<number:
        print("Too low")
    
    elif guess>number:
        print("Too high")
     
    else:
        print("Correct")
    
    print("Attempts : ",attempts)
    
    break        