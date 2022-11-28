

## OOPS

# Pen, Mobile - OBJECT

# •	OOPS provides a good way to define a cluster reflecting
# attributes and behavior of similar objects.
# This cluster is referred as class.

# •	It makes the code lengthier to perform a simple task.

# •	It makes the task easier if more and more objects with
# similar properties has to be created or if, child class
# has to inherit properties from parent class.

# •	There are five important features :
#
#     Classes and Objects
#     Encapsulation
#     Polymorphism
# 	  Abstraction
#     Inheritance









# Syntax:  class className :

# 		def __init__ (self, x) : 		# for initialization
# 			object attributes
# 			object attributes
#           self.name = x  # x = data variable

# 		def methodName (self) : 	# class function
# 			statements
#           statements
##          f = 10
#           res = x * f  # res, f = instance variable

# obj = className()


# OOPS Terminology
# Class ->
# user defined prototype of an object that defines a set of attributes which
# characterizes any object of the class

# class variable ->
# Variables that are defined in the class

# Object => obj
# unique instance of data structure that is defined by the class

# Method ->
# function that is defined inside the class

# Instance ->
# individual object assigned to the class.
# the process of creating an instance is referred as INSTANTIATION

# Data Variable
# variables that are defined at the time of initialization

# Instance Variable
# variables that are defined in the methods





## CLASS AND OBJECT #####

## OBJECT => Anything that exists in real world and can be distinguished from others
# ex : pen, mobile, table. laptop

# Each object is represented by its attributes and actions.

# CLASS => collection of objects with similar behaviour




# Syntax:  class className :

# 		def __init__ (self, x) : 		# for initialization
# 			object attributes
# 			object attributes
#           self.name = x  # x = data variable

# 		def methodName (self) : 	# class function
# 			statements
#           statements
##          f = 10
#           res = x * f  # res, f = instance variable

# obj = className()

## First Simple Class Example --


# class Person :
#
#     def __init__(self):
#         name = 'Peter'
#         age = 30
#
#     def talk(self):
#         print(name)
#         print(age)
#
# p = Person()  # Created an instance to the class
# p.talk()


## self => keyword is used for method syntax, to help interpreter understand that attributes or methods
# belongs to the relevant Class (person)


# name = 'Nitish'
#
#
# class Person :
#
#     def __init__(self):
#         self.name = 'Peter'
#         self.age = 30
#
#     def talk(self):
#         print(self.name)
#         print(self.age)
#
# p = Person()  # Created an instance to the class
# p.talk()
#
# print(name)


# Class with Actual arguments
#
# class Person :
#
#     def __init__(self, name, age):  # Passing Actual arguments
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print(self.name)
#         print(self.age)
#
# p = Person('Robert', 51)  # Passing Actual arguments
# p.talk()
#










# Create a class 'Employee' to hold employee name, department name and age of 3 employees.
# Also display them

# class Employee :
#     """ Practicing First Class Program  """
#
#     def __init__(self):
#         self.name = input("Enter Your Name : ")
#         self.dept = input('Enter Dept Name : ')
#         self.age = int(input('Enter age : '))
#
#     def display(self):
#         print("Hi, Your data is received as below : ")
#         print("{} \t {} \t {}".format(self.name, self.dept, self.age))
#
# print("FOR LOOP started ...\n")
# for i in range(0, 3) : # 0 1 2
#     emp = Employee()
#     # emp = Employee(name, dept, age)
#     emp.display()
#     print("-" * 100)










## 2. ENCAPSULATION

# mechanisism where data (variables) and code (method) are bind together
# variables and methods are called as members.
# Encapsulation isolates members of one class from another class

# class C :
#     def __init__(self):
#         x
#         y
#
#     def getFood(self):
#         print()
#
#
# class D:
#     def __init__(self):
#         x
#         y
#
#     def getFood(self):
#         print()



# Example :
# Create a class 'Telephone' that calls a person if name is present in directory

# import time
# class Telephone :
#
#     def __init__(self, phone_directory):
#         self.phone_list = phone_directory
#
#     def call(self):
#         self.name = input("Enter Name : ")
#
#         if self.name in self.phone_list :
#             print("Calling : {}".format(self.phone_list[self.name]))
#             print("Ring...Tring..Ring...")
#             time.sleep(5)
#             print("The User not available")
#
#         else :
#             print("Name not in directory")
#
#
# directory_ = {"Nitish" : 78787878787,
#               'Mandeep' : 5587997989,
#               "Varun" : 78787496874,
#               'Aastha' : 1245456446,
#               'Himanshi' : 7878798969}
#
# my_telephone = Telephone(directory_)  # instantitation
# my_telephone.call()




# ABSTRACTION ###
# Hide the unnecessary data from the user and expose only that data which is relevant to them.
# Python follows Uniform Access Prinicple, stating, that variable is public
# You can make a variable private by "__variableName" inside Class
# You can access  private variable  outside class by "_className__variableName


# Generate emplyee name and password for the user who joins organization.
# Show password if user asks for it.


#
# class CreateData :
#
#     def __init__(self, fname, lname, mob, email):
#         self.fname = fname.lower().strip()
#         self.lname = lname.lower().strip()
#         self.email = email.lower().strip()
#         self.mob = str(mob)
#         self.__password = ""
#         #self.username = ''
#
#
#     def generateUserName(self):
#         username = self.fname + self.lname + self.mob[-1 : -5 : -1]
#         return username
#
#     def generatePassword(self):
#         import string, random
#
#         s = string.ascii_letters + string.digits
#         password = "".join(random.sample(s, 10))
#
#         self.__password += password
#         return 'Password is secured'
#
#
# firstName = "Nitish"
# lastName = "   Vig     "
# mob = 8787965630
# email = "NitiSH.Vig10@GMAIL.com"
#
# emp = CreateData(firstName, lastName, mob, email)
# print("Please save your credentials...")
# print(emp.generateUserName(), "---", emp.generatePassword())
# print("Your Password = ", emp._CreateData__password)
#
#







# username logic : firstName + lastName + str(mobile)[-1 : -5 : -1]

# user = firstName.lower().strip() + lastName.lower().strip() + str(mob)[-1 : -5 : -1]
# print(user)

# import string, random
# print(string.ascii_letters + string.digits)
# s = string.ascii_letters + string.digits
#
# print("".join(random.sample(s, 10)))
# print("".join(random.sample(s, 10)))
# print("".join(random.sample(s, 10)))
# print("".join(random.sample(s, 10)))











## INHERITENCE ####

# Creating new classes freom previous classes so that they can
# acquire all the features of existing class

# base / parent / origial class => Parent
# Inherited / Child / Derived => sub class



# Simple Inheritance Example -> product of 2 numbers carried to the child


# class parentClass :
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def parentMethod(self):
#         product_of_numbers = self.a * self.b
#         return product_of_numbers
#
# p_obj = parentClass(5, -9)
# print("Product =  ", p_obj.parentMethod())
#
#
# # child class will raise the parent answer to the power of x
# class childClass(parentClass) :
#
#     def __init__(self, x):
#         parentClass.__init__(self, 5, -9)
#         self.x = x
#
#     def childMethod(self):
#         result = self.parentMethod() ** self.x
#         return result
#
# c_obj = childClass(10)
# print("Answer = ", c_obj.childMethod())



# Example :
# Create a parent class 'Telephone' that calls a person if name is present in directory.
# create a child class 'Cellphone' that can call and message

import time
class Telephone :

    def __init__(self, phone_directory):
        self.phone_list = phone_directory

    def call(self):
        self.name = input("Enter Name : ")

        if self.name in self.phone_list :
            print("Calling : {}".format(self.phone_list[self.name]))
            print("Ring...Tring..Ring...")
            time.sleep(5)
            print("The User not available")

        else :
            print("Name not in directory")


# directory_ = {"Nitish" : 78787878787,
#               'Mandeep' : 5587997989,
#               "Varun" : 78787496874,
#               'Aastha' : 1245456446,
#               'Himanshi' : 7878798969}

# my_telephone = Telephone(directory_)  # instantitation
# my_telephone.call()
#
# class Cellphone(Telephone) :
#
#     def __init__(self, phone_directory):
#         self.phone_list = phone_directory
#
#     def message(self):
#         self.name = input("Enter Name : ")
#
#         if self.name in self.phone_list:
#             msg = input("Enter the Message : ")
#             time.sleep(5)
#             print("Message Sent...")
#
#         else:
#             print("Name not in directory")
#
# directory_ = {"Nitish" : 78787878787,
#               'Mandeep' : 5587997989,
#               "Varun" : 78787496874,
#               'Aastha' : 1245456446,
#               'Himanshi' : 7878798969}
#
# my_cellphone = Cellphone(directory_)
# print("""Type from below choice :
# 1. Call
# 2. Message
# """)
# ch = int(input())
#
# if ch == 1 :
#     my_cellphone.call()
# elif ch == 2 :
#     my_cellphone.message()
# else :
#     print("Invalid Choice")
#
#



## POLYMORPHISM

# OBJECT OR METHOD is exhibiting different behaviour in different context
# provides flexibility in writing programs in such a way that programmer uses
# same method call to perform different operations.


## Operator Overidding

# class coding :
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def merge_fun(self):
#         result = self.a + self.b
#         return result
#
#
# s1 = coding("Python", " Programming ")
# print(s1.merge_fun())
#
# s2 = coding(str(True), " Programming ")
# print(s2.merge_fun())
#
# s3 = coding(100, -50)
# print(s3.merge_fun())



# Method Overriding
# Use same method name in different classes

#
# class rectArea :
#
#     def __init__(self, l, b): # formal args
#         self.length = l
#         self.breadth = b
#
#     def getArea(self):
#         return self.length * self.breadth
#
# s1 = rectArea(10, 2) # actual args
# print("Area = ", s1.getArea())
#
#
# class sqrArea(rectArea) :
#
#     def __init__(self, side):
#         self.side = side
#
#     def getArea(self):
#         return self.side * self.side
#
# s2 = sqrArea(4)
# print("Area = ", s2.getArea())




# Method Overloading
# Using method name in same class
# parameters that you are passing can be of different size


# # return the size of all elements provided in list format
#
# class fun :
#
#     def __init__(self, listName):
#         self.listName = listName
#
#     def getSize(self):
#         for each in self.listName :
#             print("Element '{}' size = {}".format(each, len(str(each))))
#
#
#
# f1 = fun(['Python', 'Green'])  # 6 5
# f1.getSize()
#
# f2 = fun([True, 'Seeing the sea']) # 4 14
# f2.getSize()
#
# f3 = fun([[4, 2], False, 'Classes']) # 2 5 8
# f3.getSize()
#












































