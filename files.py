#First example

f=open("test.txt","a")
f.write("This is a test file.\n")
f.write("This file is used for testing purposes.\n")
f.close()


#Second example
with open("test1.txt","r") as f:
    content=f.read()
print(content)
print("Dobbey")

#More examples there coming soon.......