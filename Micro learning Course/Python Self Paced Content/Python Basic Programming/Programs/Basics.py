


### Data types in Python ###

# string
# int
# bool
# float
# complex

# Let say you have a basket of 20 apples and total price is Rs. 500.
# find the price of an apple

# price of apple = x
# total apples, n = 20
# total price, p = 500
#
# x = p / n
# x = 25

# total_apples = 20
# total_price = 500
# x = total_price / total_apples
# print(x)


# Python is dynamicaly typed language
# x = 10
# print(x, type(x))
#
# x = 10.0
# print(x, type(x))
#
# x = '10'
# print(x, type(x))


#
# # Strings - written in a pair of single or double quotes
#
# print("Saturday")
# print('Sunday')
#
# print(type("Saturday"))
# print(type('Sunday'))
#
#
# # int
# x = 10
# y = 20
# z = -9
# print(x, type(x))
# print(y, type(y))
# print(z, type(z))
#
#
# # float
# x = 10.0
# y = 20.5878
# z = -9.455612534531350560123
# print(x, type(x))
# print(y, type(y))
# print(z, type(z))


# complex - real + imaginary => a + bj
#
# c1 = 4 - 9j
# c2 = 10 + 20j
# c3 = 5j
#
# print(c1, type(c1))
# print(c2, type(c2))
# print(c3, type(c3))
#




# boolean - True or False
# f = True
# g = False
# print(f, type(f))
# print(g, type(g))
# print(10 > 20)
# print(50 <= 52)








# What is a Variable??
# What is a keyword
# What is a Literal
# Rules for writing a variable

#
# price = 5000
# name = 'Python'
# r1 = True
# echo = 77.89
#
#
# print(price, type(price))
# print(name, type(name))
# print(r1, type(r1))
# print(echo, type(echo))


# Literal - defined as the value on the right side of the equalSign
# Variable - anything that can store the literal. defined on left side of equalSign


### Making A Tea
# sugar = 2, tea leaves = 5, water = 0, milk = 5, gas = 10
# making charges = 3
#
# print("Fianl price of Tea = ")
# print(2 + 5 + 0 + 5 + 10 + 3)
#
#
#
#
# # sugar = 3, tea leaves = 7, water = 0, milk = 7, gas = 20
# # making charges = 5
#
# print("Fianl price of Tea = ")
# print(3 + 7 + 0 + 7 + 20 + 5)









# What is a Variable??
# What is a keyword
# What is a Literal


# # Python keywords
#
# # if = 52000
# if_1 = 520000
#
# # while = 'Hello'
#
# import keyword
# kw = keyword.kwlist
#
# # for each in kw :
# #     print(each)
# x = 100

# print(keyword.iskeyword(variableName))




# Rules for writing a variable

# 1. Variable name shall have alphabets, numbers and _ only

# hello = "Python"
# print(hello, type(hello))
#
# place_585 = "Delhi"
# print(place_585 , type(place_585))


# 2. Variable names shall not start with number

# hello = 'python '
# print(hello)
#
#
# # 7744_hello = 'python '
# # print(hello)
#
# _hello = 'python '
# print(_hello)



# 3. variable name can of any length

# x = 'delhi'
# myPlaceName = 'delhi'
# rteytghuijo354651_jhjgkjhnmkhgyuthyinj = 'delhi'
#


# 4. Special characters are not allowed

# place& = 'delhi'
# place% = 'delhi'
# place ofCountry = 'delhi'


# 5. Keywords are not allowed to be taken as a variable

# break = False
# while = 250



# display anything on the output screen, use PRINT

# x = 100
# # print(x)
#
# place_5 = 'Delhi '
#
# # print(52, 74, 96 + 4)
# #
# # print(True, 'Pilot', 400, 96.33, 5j)
# #
# #
# # print(True, 'Pilot', 400, 96.33, 5j, sep = "-")
# # print(True, 'Pilot', 400, 96.33, 5j, sep = ".*.")
# #
#
# print(x, place_5, True, 'Pilot', 400, 96.33, 5j, sep = "  --  ")
#
#
#

# derived data types
# list
# tuple
# dictionary
# sets





#
#
# # input - take value from the user at real time
#
# # day = input("What is your favourite DAY - ")
# # print(day, type(day))
#
# # stockPrice = input("Enter Stock Price (500 - 1000) = ")
# # print(stockPrice + 1000)
#
#
# # Typecast the value to work with some other operations
# # Convert one datatype to another
#
# # a = 100
# # b = str(a)
# # print(a, type(a))
# # print(b, type(b))
# #
# # c = float(a)
# # print(c, type(c))
#
#
# # num1 = 14.25
# # print(num1, type(num1))
# # num2 = int(num1)
# # print(num2, type(num2))
# #
# # str_1 = str(num1)           # "14.25"
# # print(str_1, type(str_1))
#
#
# # integer values of the boolean
# # p1 = 1
# # print(p1, type(p1))
# #
# #
# # p2 = False
# # print(p2, type(p2))
#
#
# # q1 = int(True)
# # print(q1, type(q1))
# #
# #
# # q2 = int(False)
# # print(q2, type(q2))
# #
# #
# #
# # r1 = bool(1)
# # r2 = bool(0)
# #
# # print(r1, type(r1))
# # print(r2, type(r2))
#
#
# salary = float(input("What is your salary : "))
# print("Salary = ", salary + 100)
#
# age = int(input("Write AGE = "))  # "23" -> 23
# print("Age = ", age, type(age))
#

































