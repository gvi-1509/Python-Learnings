'''
def my_map(my_func, my_iter):
  result = []
  for item in my_iter:
    new_item = my_func(item)
    result.append(new_item)
    return(result)
  
nums = [3,4,5,6,7]

cubed = my_map(lambda x: x**3,nums)

print(cubed)
'''

'''
def add(x,y):
    return x+y
print(add(4,5))

print((lambda x,y : x+y)(4,5))

'''
#cars=["Ford","Volvo","BMW"]
#print(cars)
#print(cars[0])
#print(len(cars))

#cars=["Ford","Volvo","BMW"]
#for x  in cars:
 #   print(x)

#cars.append("Honda")
#print(cars)
#cars.pop(1)
#print(cars)

#fruits = ['apple','banana','chiku']
#fruits.extend(cars)
#print(fruits)
#x=fruits.index("chiku")
#print(x)
#fruits.insert(1,"mango")
#print(fruits)
#fruits.reverse()
#print(fruits)
#fruits.sort()
#print(fruits)
'''
class Myclass:
   # x=5
    #print(x)
#p1= Myclass()
#print(p1.x)
   def __init__(self,name ,age):
    self.name= name
    self.age= age 
   def __str__(self):
     return f"{self.name}({self.age})"

p1 = Myclass("Gauri",21) 
#print(p1.name,p1.age)   
print(p1)
#del p1.age

class intern(Myclass):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.graduationyear = 2025

    x = intern("gauri","pal",2025)
  
'''
'''
mytuple = ("apple","chiku","cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

'''
''''
class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
         
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")    

for x in (car1, boat1, plane1):
  x.move()

'''
'''
x = 500  #global scope
def myFunc():

    #x= 300 #local scope
    print(x)

myFunc()
'''

'''
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

'''
'''
# = min(5, 10, 25)
#y=max(5, 10, 25)
#x= abs(-7.25)
x=pow(4,3)

print(x)
'''


    