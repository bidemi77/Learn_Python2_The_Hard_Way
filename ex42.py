# What is the difference between a Fish and a Salmon 
# What is the difference between Mary and a Salmon?

## Animal is-a object (yes, sort of confusing) look at the extra credit 

class Animal(object):
	pass

##  class 

class Dog(Animal):

	def __init__(self, name):
		##  has-a
		self.name = name 


## ??
class Cat(Animal):

	def __init__(self,name):
		## has-a
		self.name = name 

## is-a 
class Person(object):
	def __init__(self,name):
		## has-a
	    self.name = name 

	    ## Person has a pet of some kind 
	    self.pet = None 

## is-a 
class Employee(Person):

	def __init__(self,name,salary):
		## has-a hmm what is this strange magic?
	    super(Employee,self).__init__(name)
	    ## inheritance 
	    self.salary = salary 

## is-a
class Fish(object):
	pass

## is-a
class Salmon(Fish):
	pass

## is-a
class Halibut(Fish):
	pass

## rover is-a Dog 
rover = Dog("Rover")

## is-a 
satan = Cat("Satan")

## is-a
mary = Person("Mary")

## has.a
mary.pet = satan

## has-a
frank= Employee("Frank", 120000)

## has-a
frank.pet = rover 

## Instantiating an object
flipper = Fish()

## Instantiating an object
crouse = Salmon()

## Instantiating an object
harry=Halibut()



# is-a is an inheritance concept 
# has-a is a composition concept 
