
## Functions  ####

# module designed to perform a task
# reduce the line of codes
# code reusability

# How to write a function

# Function Declaration / Function creation
# def functionName(arguments...) :
#     state1....
#     state 2 ....
#     .complex    .
#     .
#     .
#     return value

# Function Calling
# functionName(arguments...)



# create a function that returns square of a number


# def sqr_fun(num) :
#     print(num ** 2)
# sqr_fun(10)
#
#
#
# def sqr_fun_2(n) :
#     return (n**2)
#
# print(sqr_fun_2(-9))





# Why FUNCTION

# retrieve only characters (alphabets and numbers) from the string

# stringName = input("Enter the string : ")


# stringName = " Earth to the Moon..  "
# print(stringName)
#
# output = ""
#
# for c in stringName :
#     if c.isalpha() :
#         output = output + c
# print(output)



# stringName = " $ 85 mhnbj  45742 ... "
# print(stringName)
#
# output = ""
#
# for c in stringName :
#     if c.isalnum() :
#         output = output + c
# print(output)


# stringName = "---   Hey Friend, Get the car number 8787 from shop       "
# print(stringName)
#
# output = ""
#
# for c in stringName :
#     if c.isalnum() :
#         output = output + c
# print(output)


# return the string aftyer removing blank spaces at the of the string
# and also, return only characters

# " new job = 45420    "
# "new job  45420"

# def fun(s) :
#     output = ""
#
#     for c in s :
#         if c.isalnum() :
#             output = output + c
#
#     return output



# def fun(s) :
#
#     s = s.strip()
#     output = ""
#
#     for c in s :
#         if c.isalnum() :
#             output = output + c
#         elif c.isspace() :
#             output = output + c
#     return output
#
#
# stringName = " Earth to the Moon..  "
# print(stringName, " : \n", fun(stringName))
#
# stringName = " $ 85 mhnbj  45742 ... "
# print(stringName, " : \n", fun(stringName))
#
# stringName = "---   Hey Friend, Get the car number 8787 from shop       "
# print(stringName, " : \n", fun(stringName))
#






### Python Built in Functions

# x = 100
# x = str(x)
# print(type(x))

# type casting functions
# print(str(4 - 7j))
# print(int(14.2))
# print(float("70.25"))
# print(bool(1))
# print(bool(0))
#
# print(int(True))
# print(int(False))
#
# print(list((4, 7, 'Hi', False)))
#
# print(set((4, 7, 'Hi', False, 4, 4)))




## math Functions

# s1 = (4, 7, -9, 10, 0, -2)
#
# print(min(s1))
# print(max(s1))
# print(sum(s1))



# print function
# print(, , , , ,)

# input function
# input("Enter msg : ")


# range => generate a number sequence from start to end
# print(range(1, 50))
# print(list(range(1, 50)))
# print(tuple(range(1, 50)))


# Verify that particular element belongs to that data type class

# isinstance(element, className)  # className => int, float, str, bool, list, tupple

# x = '100'
# print(isinstance(x, int))

# y = [4, "K"]
# print(isinstance(y, set))
# print(isinstance(y, list))




## Create a Function

# check if "all" is present inside the string
# if found, convert that 'all' to "AT"



# def fun_string(s) :
#     if "all" in s :
#         s = s.replace('all', 'AT')
#
#     # print(s)
#
#     return s
#
#
#
# stringName_1 = 'ball call cost boast'
# print(stringName_1, " : \n", fun_string(stringName_1))
#
# print()
#
# stringName_2 = 'CaN Allow call cost boast'
# print(stringName_2, " : \n", fun_string(stringName_2))






#
#
# def ghl(x) :
#     x = x / 10
#
#     return x  # 10.0
#
# x = 100
#
#
# print(ghl(x))  # ghl(100)
# print(x)

# local and global variable
# local variables are the variables that have scope defined in the function only
# global variables are the variables that have scope all over the program





# def ghl(y) :  # 100
#     y = y / 10  # 10.0
#
#     return y # 10.0
#
# x = 100
#

# print(ghl(x))  # ghl(100)
# print(x)
# print(y)



# def ghl(y) :  # formal arguments
#     y = y / 10  # 10.0
#     return y # 10.0
#
# x = 100
#
#
# print(ghl(x))  # actual arguments






## Function Arguments

# 1. Positional Arguments

# def area_circle(rad, pie_) :
#     return (pie_ * rad * rad)

# print(area_circle(10, 3.14))
# print(area_circle(3.14, 10))

# print(area_circle(10))
# print(area_circle(3.14, 10, 10))



# 2. Keyword argument

# def area_circle(rad, pie_) :
#     return (pie_ * rad * rad)
#
# print(area_circle(rad = 10, pie_ = 3.14))
# print(area_circle(pie_ = 3.14, rad = 10))
# print(area_circle(rad = 10, 3.14))


# 3. Default argument

# def area_circle(rad, pie_ = 3.14) :
#     return (pie_ * rad * rad)
#
# print(area_circle(rad = 10, pie_ = 3.14))
# print(area_circle(pie_ = 10, rad = 10))
# print(area_circle(rad = 10))





## LAMBDAS

# single line functions , tenary operators
# def less functions

# lambda arguments : expression

# using Simple Function (non - lambda)
#
# def square_fun(num) :
#     return (num ** 2)
#
# num = int(input("Enter Number : "))
#
# print("Square of {} = {}".format(num, square_fun(num)))
#
#
# # using Lambda
#
# lambda_fun = lambda num : num ** 2
# num = int(input("Enter Number : "))
# print("Square of {} = {}".format(num, lambda_fun(num)))
#


# Finding max of 2 numbers using lambda

# max_fun = lambda a, b : a if a > b else b
# print(max_fun(10, 20))
# print(max_fun(999, -5))


# If 'all' is present in string then replace it by 'AT', else return FALSE

# fun_1 = lambda s : s.replace("all", "AT") if 'all' in s else False
#
# stringName = "Coat ALLow, call Beast"
# print(fun_1(stringName))
#
# stringName = "Coat "
# print(fun_1(stringName))







































































