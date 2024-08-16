'''
Continuation of 15
Object Oriented Programming
 - delete objects
 - perform introspection
 - dynamic modifications to attributes
 - invoke methods and understand the method resolution(MRO) in inheritance
 - use name mangling to create private variables
'''
import mypackages.car as vehicle
# create an instance
redbull = vehicle.Car(numberDoors=0,
                      registrationNum='RB 999',
                      make='Red Bull',
                      model='RB9',
                      year='500 BC',
                      max_speed=210,
                      acceleration_rate=18,
                      deceleration_rate=6)
print(redbull)
# delete
del redbull
try:
    print(redbull)
except NameError as e:
    print(e)

'''
15.7 Introspection
Accessing Objects attributes and introspection allow us to examine
the attributes and methods if objects and classes.
'''
# assume mercedes is another car object
mercedes = vehicle.Car(numberDoors=2,
                      registrationNum='RB 690',
                      make='Mercedes',
                      model='AMG F1',
                      year='200 BCE',
                      max_speed=300,
                      acceleration_rate=26,
                      deceleration_rate=72)

# access an object's attribute references
print(mercedes.__dict__)
# access a class name
print(vehicle.__name__)
# access an object name
print(mercedes.__class__.__name__)

'''
15.8 Adding Attributes
You can add new attributes to an object at runtime using the setattr() function
'''
print(mercedes)
setattr(mercedes,"color","Red")
setattr(mercedes,"tinted",True)
setattr(mercedes,"turbo",True)


print(mercedes)
print(mercedes.__getattribute__("color"))

'''
15.9 Invoke Method
Methods of an object are invoked when called upon using the dot notation.
'''

mercedes.acceleration()

'''
15.10 Inheritance
Understand super classes and sub classes attributes.
'''
ferrari = vehicle.Car(numberDoors=2,
                      registrationNum='RB 696',
                      make='Ferrari',
                      model='raptor',
                      year='3000 BCE',
                      max_speed=300,
                      acceleration_rate=26,
                      deceleration_rate=72)
print(ferrari.numberDoors)

class myCar(vehicle.Car):
    def __init__(self, numberDoors, registrationNum, make, model, year, max_speed, acceleration_rate, deceleration_rate) -> None:
        super().__init__(numberDoors, registrationNum, make, model, year, max_speed, acceleration_rate, deceleration_rate)
        self.number_of_car = 3
    def __str__(self) -> str:
        return super().__str__() + " 'number_of_car' : {self.number_of_car}"
    def turnOn(self):
        print("Vroom Vroom Car is on")
becky = myCar(numberDoors=2,
                      registrationNum='RB 0000',
                      make='Honda',
                      model='CIVIC',
                      year='Mesozoic Era',
                      max_speed=1_000_000,
                      acceleration_rate=500,
                      deceleration_rate=0)
print(becky)
becky.turnOn

'''
15.11 Constructors
A constructor uses the __init__ method. This is a special keyword in Python.
'''
class A:
    # constructor
    def __init__(self) -> None:
        print("A class was made.")
    def print_me(self):
        print("YAY you printed A from the method!")
a = A()
a.print_me()
class B:
    # default constructor
    def print_me(self):
        print("YAY you printed B from the method.")
b = B()
b.print_me()
class C:
    def __init__(self) -> None:
        A.__init__(self)
        print("From C")
    def print_me(self):
        print("YAY you printed C from the method.")
c = C()
c.print_me()

'''
15.12 Name Mangling
Name mangling is when you make an attribute private using the '__' before the variable name.
'''
# define a class with private variable
class User:
    def __init__(self,fname,lname,email,dob,address) -> None:
        self.fname = fname
        self.lname = lname
        self.email = email
        self.__dob = dob
        self.__address = address
    def display_dob(self):
        print(self.__dob)
    def display_address(self):
        print(self.__address)

barack_Obama = User("Barack", "Obama", "obama@gmail.com", "08/04/1961", "2569 pkwy Chino Hills")
barack_Obama.display_dob()

'''
15.13 Common Function for Class
'''

print(hasattr(barack_Obama,"Age"))
print(hasattr(barack_Obama,"fname"))

print(type(barack_Obama))
print(type([1,2]))
