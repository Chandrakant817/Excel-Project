

##### Types of Errors #####


# 1. Compile time error :
# These type of errors arise at the time of compilation
# Grammer of porgramming is incorrect, compiler will show error

# syntax error, name error , indentation error

# 100
# b = 20
#
# print(a + b)


# a = 100
#     b = 20
# print(a + b)



# 2. Run time error
# errors identified by the interpretter
# Run arising during execution of the program

# File not found error, index error, zero division

# f = open('fileName.txt', 'r')

# listName = ['mango', 'apple', "GRAPES", "cherry"]
# print(listName[4])

# res = 10 / 0
# print(res)



## NOTE ###
## Exception Class Name :
# these are the names which you pass in except blovk


# 3. Logical error
# These errors progammer has to take care of...

# Find out perimter of the circle
# p = 2 * pie * r

# pie_ = 3.14
# r = 10
#
# # perimeter_circle = pie_ * r * r
# perimeter_circle = 2 * pie_ * r
#
# print(perimeter_circle)






## BLOCKS OF EXCEPTION HANDLING ###
## TRY, EXCEPT, FINALLY
## Runt ime errors are found in Exceptional Handling

# # Simple Try Except Block
# # best case and worst case
#
# num1 = 20
# num2 = 100
#
# fileName = "myText.txt"
# # fileName = "habit.txt"
#
# listName = ['zebra', 'Eagle', '  Elephant', 'tiger   ']
#
# try :
#     add_ = num1 + num2
#     div_ = num1  / num2
#
#     print("Addition = {}".format(add_))
#     print("Division = {}".format(div_))
#
#     print("-" * 100)
#
#     f = open(fileName, mode = 'r')
#     msg = f.read()
#     print(msg)
#
#     print("-" * 100)
#
#     print(listName[3])
#
#     print("-" * 100)
#
# except :
#     # print("MAke sure, you are not dividing by 0")
#     print("Error Found")
#     print("-" * 100)
#     print()
#
#
# finally:
#     print("Thank you for using US.")
#     import datetime
#     print(datetime.date.today())
#






# Simple Try Except Block
# best case and worst case

num1 = 20
num2 = 100

# fileName = "myText.txt"
fileName = "habit.txt"

listName = ['zebra', 'Eagle', '  Elephant', 'tiger   ']

try :
    add_ = num1 + num2
    div_ = num1  / num2
    print("Addition = {}".format(add_))
    print("Division = {}".format(div_))
    print("-" * 100)

    f = open(fileName, mode = 'r')
    msg = f.read()
    print(msg)
    print("-" * 100)

    print(listName[10])
    print("-" * 100)

except ZeroDivisionError:
    print("MAke sure, you are not dividing by 0")
    print("-" * 100)
    print()

except FileNotFoundError:
    print("MAke sure, FILE exists in data base")
    print("-" * 100)
    print()

except IndexError:
    print("Check for OUT OF BOUND variable in TRY block")
    print("-" * 100)
    print()

finally:
    print("Thank you for using US.")
    import datetime
    print(datetime.date.today())















































