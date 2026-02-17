
# #First example

class Student:
    name="Sreekar"
    age=17
    city="Hyderabad"
    
s1=Student()
print(s1.name)
del s1.city
print(s1.name)
print(s1.city)

#Second example

class EMP:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
        
e1=EMP("Sreekar",17,"Hyderabad")
print(e1.name)
print(e1.age)
print(e1.city)

#Third exapmple

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def avg(self):
        return sum(self.marks.values()) / len(self.marks)
s1 = Student("Sreekar")
s1.add_mark("Math", 85)
s1.add_mark("Science", 90)
print(s1.name)
print(s1.marks)
print(s1.avg())
print("Dobbey")

#Fourth example

class car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
        
    def show_info(self):
        print(f"Brand: {self.brand},speed: {self.speed}")
        
    def acc_speed(self,acc):
        self.speed+=acc
        print(f"Accelerated speed: {self.speed}")
        

c1=car("BMW",350)
c1.show_info()
c1.acc_speed(-500)


#Fifth example









