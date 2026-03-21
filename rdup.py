list=[]
for i in range(5):
    a=int(input("Enter the number: "))
    list.append(a)
    
nl=[]
for i in range(len(list)):
    if list[i] not in nl:
        nl.append(list[i])

print(f"Unique numbers: {nl}")
    