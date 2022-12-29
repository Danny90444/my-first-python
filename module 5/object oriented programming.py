#print(dir(""))
#print(help(""))

from argparse import ArgumentDefaultsHelpFormatter


class Apple: 
    pass

class Apple:
    color = ""
    flavor = ""

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"

print(jonagold.color)
print(jonagold.flavor)


# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
 highest_city = ""
 return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
 if city1.population >= min_population:
  return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
 if city2.population >= min_population and city2.elevation > return_city.elevation:
  return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
 if city3.population >= min_population and city3.elevation > return_city.elevation:
		return_city = city3

	##Format the return string
 #if return_city.name:
 # return f"{return_city.name}, {return_city.country}"
 # else:
 #  return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""

g = type("")
print (g)

class Person:
	def __init__(self, name):
		self.name = name
	def greeting(self):
		# Should return "hi, my name is " followed by the name of the Person.
		return ("hi, my name is {}".format(self.name))

# Create a new instance with a name of your choice
some_person = Person("Jacob")
# Call the greeting method
print(some_person.greeting())


class Apple:
	#initialize the self variable and sets the parameters
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor
		#define method that converts it to a string
	def __str__(self):
		return "This apple is {} and its flavor is {}".format(self.color, self.flvaor)
   #declare an instance variable and assign two values to its attributes
jonagold = Apple("red", "sweet")
print(jonagold.color)


class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person."""
    print("Hello! My name is {name}.".format(name=self.name)) 

#help(Person)

def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes and seconds."""
    return hours*3600+minutes*60+seconds

class Salary:
	def __init__(self, pay, bonus):
		self.pay=pay 
		self.bonus=bonus
	def annual_salary(self):
		return (self.pay*12) + self.bonus
class Employee:
	def __init__(self, name, age, pay, bonus):
		self.name=name 
		self.age = age 
		self.obj_salary=Salary(pay, bonus)
	def total_salary(self):
		return self.obj_salary.annual_salary()

emp = Employee('max',25, 15000, 10000)
print(emp.total_salary())


class Repository:
     def __init__(self):
         self.packages = {}
     def add_package(self, package):
         self.packages[package.name] = package
     def total_size(self):
         result = 0
         for package in self.packages.values():
             result += package.size
         return result

#import datetime
#now = datetime.datetime.now()
#type(now)
#<class 'datetime.datetime'>
#print(now)


#import random
#random.randint(1,10)

#random.randint(1,10)

#random.randint(1,10)


#print(now)

#now.year

#print(now + datetime.timedelta(days=28))


#inheritance 

class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = 'reptile'

print(Turtle.category)

class Snake(Animal):
    catergory = 'reptile'

def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))
print (((10 >= 5*2) and (10 <= 5*2)))
