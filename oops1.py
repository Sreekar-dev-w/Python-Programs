

class Student:
    name="Sreekar"
    age=17
    city="Hyderabad"
    
s1=Student()
print(s1.name)
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

#Third example
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


class car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.color} {self.model} is driving.")
        
    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")
        
c1=car("Red","BMW",2026)
c2=car("Blue","Audi",2025)
c1.drive()
c2.stop()
print(c1.model)
print(c1)
print(c2)


#Sixth example
class Class:
    count = 0
    
    def __init__(self, name, year, classroom):
        self.name = name
        self.year = year
        self.classroom = classroom
        Class.count += 1
        
    def details(self):
        print(f"{self.name} - {self.year} - {self.classroom}")

    def friends(self):
        print(f"{self.name} is in {self.classroom} and has friends.")
        
students = [
    Class("Sreekar", 2024, "10th"),
    Class("Sree", 2025, "10th"),
    Class("Sreee", 2026, "10th")
]

for s in students:
    s.details()

print("Total students:", Class.count)


# Seventh example(Inheritance)
class Animal:
    def __init__(self,name):
        self.name=name
        
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
class Dog(Animal):
    pass
class Cat(Animal):
    pass
d1=Dog("Buddy")
c1=Cat("Whiskers")
d1.eat()
print(d1.name)
c1.sleep()
print(c1.name)


#Eighth example(Multiple Inheritance,Multilevel Inheritance)
class Animal:
    def __init__(self,name):
        self.name=name
        
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
class Prey(Animal):
    def flee(self):
        print(f"{self.name} flees.")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} hunts.")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
r1=Rabbit("Thunder")
h1=Hawk("Sky")
r1.flee()
h1.hunt()
r1.sleep()
h1.eat()

#Ninth example(Abstact CLasses)
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def __init__(self,name):
        self.name=name
    def start(self):
        print(f"{self.name} is starting.")
    def stop(self):
        print(f"{self.name} is stopping.")
    

car = Car("BMW")
car.start()
car.stop()

#Tenth example(super())
class Shape:
    def __init__(self,color,name):
        self.color=color
        self.name=name
        
    def describe(self):
        print(f"{self.name} is {self.color}.")
class Circle(Shape):
    def __init__(self,color,name,radius):
        super().__init__(color,name)
        self.radius=radius
    def describe(self):
        print(f"{self.name} is a {self.color}.")
c1=Circle("Red","Circle",5)
print(c1.color)
print(c1.radius)
class Rectangle(Shape):
    def __init__(self,color,name,length,width):
        super().__init__(color,name)
        self.length=length
        self.width=width
r1=Rectangle("Blue","Rectangle",10,5)
print(r1.name)
print(r1.color)
#so over here we used a method called describe in both parent and child class but when we call it
#in circle it will see that if a method is present in circle or not if not present in the circle then it will use the method from the super class 


# Eleventh example(Polymorphism)









