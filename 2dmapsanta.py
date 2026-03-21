# #suggest the code changes required to run this code without any errors and to achieve the intended functionality.
# l=[[],[],[],[],[],]
# for i in range(0,4):
    
#     l[i].append(input())
# print(l)
# f1=[]
# f2=[]
# for h in range(0,4):
#     for k in range(0,4):
#         if l[h][k]=='p':
#             f1.append((h, k))
# print(f1)


l=[[],[],[],[],[],]
print("Enter 5 characters per row (e.g., 'p...') and press Enter:")

for i in range(0,5):
    # This takes your whole string and chops it into a list of 5 items! 🪓
    l[i] = list(input(f"Row {i}: "))

for t in l:
    print(t)

f1=[]
f2=[]
for h in range(0,5):
    for k in range(0,5):
        if l[h][k]=='p':
            f1.append([h+1, k+1])
print(f1)
if f1[0][0]== f1[1][0]:
    f2.append(f1[0][0])
    if f1[0][1]<f1[1][1]:
        print(f"should move towards rightfor {f1[1][1]-f1[0][1]} moves")
    elif f1[0][1]>f1[1][1]:
        print(f"should move towards left for {f1[0][1]-f1[1][1]} moves")
 
   
    

elif f1[0][0]<f1[1][0]:
    f2.append(int(f1[1][0]-f1[0][0]))
    print(f"should move towards down for {f1[1][0]-f1[0][0]} moves")
    if f1[0][1]<f1[1][1]:
        print(f"should move towards rightfor {f1[1][1]-f1[0][1]} moves")
    elif f1[0][1]>f1[1][1]:
        print(f"should move towards left for {f1[0][1]-f1[1][1]} moves")
 
elif f1[0][0]>f1[1][0]:
    f2.append(int(f1[0][0]-f1[1][0]))
    print(f"should move towards up for {f1[0][0]-f1[1][0]} moves")
    if f1[0][1]<f1[1][1]:
        print(f"should move towards rightfor {f1[1][1]-f1[0][1]} moves")
    elif f1[0][1]>f1[1][1]:
        print(f"should move towards left for {f1[0][1]-f1[1][1]} moves")
 
   
