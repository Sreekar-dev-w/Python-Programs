questions=[
    ("What is 2+2?","4"),
    ("What is the capital of France?","Paris"),
    ("What is the largest planet in our solar system?","Jupiter"),  
    ("What is the chemical symbol for water?","H2O")
]
s=0
for q in questions:
    print(q[0])
    answer=input("Your answer: ")
    if answer.lower()==q[1].lower():
        print("Correct😛😛😛😛")
        s+=1
    else:
        print("Wrong😔😔😔😔")
        
print(f"Your score is {s}/{len(questions)}")
print("Dobbey")