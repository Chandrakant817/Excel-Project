# Data Structures in Python

# fundemental data types -> Strings
# derived data types -> List, Tuple, Dictionary, Sets, Arrays


### STRINGS ###
# defined as collection of characters (alphabets, numbers, puntuations)
# enclosed in a pair of single (') or double (") quotes.
# we can type cast objects to string by using the function 'str'

# How we write the strings
# name = "New Delhi"
# pm = 'Narendra Modi'
#
# print(name, type(name))
# print(pm, type(pm))
#
# # type casting
# a = str(100)
# b = str(False)
# c = str(5.0 - 6.2j)
#
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))


# msg = "I've completed the tasks."
# print(msg)
#
#
# msg = 'I"ve completed the tasks.'
# print(msg)
#
#
# msg = 'I've completed the tasks.'
# print(msg)


# display = """You are required to complete tasks as below :
#
# 1. Sleep
# 2. Learn
# 3. Work
# """
# print(type(display))
# print(display)


# Basic operations in Strings

stringName = "I love to play Football"
# print(stringName)

# 1. Length => return number of characters inside the string
# len(stringName)

# print(len(stringName))

# 2. Indexing => return the character at specified position
# stringName[positionNumber] # int format

# print(stringName[0])
# print(stringName[2])
# print(stringName[10])

# print(stringName[len(stringName) - 1])


# 3. Slicing => extracting smaller chunk from the sequence
# stringName[start : end : step_size]
# end is not included
# step_size default value is 1
# print(stringName)
# print(stringName[5])
# print(stringName[0 : 5])


# print(stringName[12 : 18])

# print(stringName[0 : len(stringName)])
# print(stringName[0 : len(stringName) : 1])
# print(stringName[0 : len(stringName) : 5]) # 0 5 10 15 20

# print(stringName[0 : len(stringName) : 1])
# print(stringName[ : len(stringName) : 1])  # start default value is 0
# print(stringName[0 :  : 1])  # end default is length of seq
# print(stringName[0 : len(stringName) : ]) # default step size is 1


# print(stringName[ : : ])











# Basic operations of string

stringName = "I love to play Basketball"

# 4. concatenation : merging 2 or more strings into a single string
# str1 + str2 + .... + strN

# print(stringName + " since 2000")
# # print(stringName + 2000)
#
# print(stringName + ' since => ' + str(2000))
#
# stringName = stringName + str(2000)
# print(stringName)



# 5. Repitition -> repeat the string by n times
# stringName * n

# print(stringName)
# # print(stringName * 2)
# # # print(10 * 20)
# #
# # # print(2 * stringName)
# #
# # print(stringName[15])
# # print(type(stringName[15]))
# # print(stringName[15] * 10)
#
#
# print(stringName[10 : 15] * 5)




# Basic operations in strings

# Membership operator
# in, not in
# in => Returns TRUE, if char or str-chunk is present inside the string

stringName = 'ball call Bat cat'
# print("b" in stringName)
# print("C" in stringName)
#
# print("ball" in stringName)
# print("bat" in stringName)
#
# print("at" in stringName)

# stringName = 'ball call Bat cat'
# stringName = 'Bill call Bat cat'
# if ('ball' in stringName) :
#     print("Play Cricket")
# else :
#     print("Play Badminton")


# stringName = 'ball call Bat cat'
# print("Hello" not in stringName)
# print("call" not in stringName)




# Built in Functions



# 1. Convert the case of the strings
stringName = 'East or WEST, HomE is the BEst'

# print(stringName.upper())
# print(stringName.lower())
# print(stringName.title())  # every first letter of the word will be capital, rest all are lowercase
# print(stringName.swapcase())



# 2. remove blank spaces from left or rigth side of the string
# stringName = '   East or WEST, HomE is the BEst       '
#
# print(len(stringName))
# print(stringName)
#

# print(len(stringName.strip()))
# print(stringName.strip())

# print(len(stringName.lstrip()))
# print(stringName.lstrip())


# print(len(stringName.rstrip()))
# print(stringName.rstrip())




# 3. Count character inside the string
# stringName = 'East or WEST, HomE is the BEst'
# stringName = stringName.lower()
#
# print(stringName)
# print(stringName.count('e'))


# print(stringName)
# print(stringName.count('or'))


# print(stringName)
# print(stringName.count('st'))



# 4. replace old word by new word
# stringName = 'East or WEST, HomE is the BEst'
# stringName = stringName.lower()
#
# print(stringName.replace('or', 'and'))

# stringName = stringName.replace('or', 'and')


# 5. Sort the string
# stringName = 'East or WEST, HomE is the BEst'
# print(sorted(stringName))




## Split and Join

# split - break down the string into sub string based on some pattern.
# It returns the list

# stringName.split(special character)

# str_a = 'Introduction to Python'
# list_a = str_a.split(" ")
#
# print(str_a, "\n", list_a, "\n", type(list_a))
#
# print()
#
# str_b = 'Introduction to Python'
# list_b = str_b.split("o")
#
# print(str_b, "\n", list_b, "\n", type(list_b))
#
#
# print()
#
# str_c = '13-06-2000'
# list_c = str_c.split("-")
#
# print(str_c, "\n", list_c, "\n", type(list_c))



# JOIN
# Convert the list back to string on the basis of some special char
# "special char".join(listName)

#
# list_a = ['Introduction', 'to', 'Python']
# str_a = "_".join(list_a)
#
# print(str_a, "\n", list_a, "\n", type(str_a))
#
# print()
#
# list_b = ['Intr', 'ducti', 'n t', ' Pyth', 'n']
# str_b = "o".join(list_b)
#
# print(str_b, "\n", list_b, "\n", type(str_b))
#
#
# print()
#
# list_c = ['13', '06', '2000']
# str_c = "/".join(list_c)
#
# print(str_c, "\n", list_c, "\n", type(str_c))
#





# Test Cases in the Strings
# islpha - returns TRUE is string contains only alphabets (a-z, A-Z)
#isdigit - returns TRUE, if string contains digit
# isalnum - Returns TRUE, if string contains either alphabets or numbers
# isspace = returns TRUE, if string contains spacess
# isupper
# islower
# istitle

string_1 = "Peacock"
string_2 = "88557744524"
string_3 = "OTP9874"
string_4 = "     "
string_5 = "$100"
string_6 = "9*8/5"
string_7 = "rabbit"
string_8 = "EAGLE"

string_1 = "Peacock"
# print(string_1.isalpha())
# print(string_1.isdigit())
# print(string_1.isalnum())
# print(string_1.isspace())
# print(string_1.islower())
# print(string_1.isupper())
# print(string_1.istitle())


string_2 = "88557744524"
# print(string_2.isalpha())
# print(string_2.isdigit())
# print(string_2.isalnum())
# print(string_2.isspace())
# print(string_2.islower())
# print(string_2.isupper())
# print(string_2.istitle())



string_3 = "OTP9874"
# print(string_3.isalpha())
# print(string_3.isdigit())
# print(string_3.isalnum())
# print(string_3.isspace())
# print(string_3.islower())
# print(string_3.isupper())
# print(string_3.istitle())



string_4 = "     "
# print(string_4.isalpha())
# print(string_4.isdigit())
# print(string_4.isalnum())
# print(string_4.isspace())
# print(string_4.islower())
# print(string_4.isupper())
# print(string_4.istitle())



string_5 = "$100"
# print(string_5.isalpha())
# print(string_5.isdigit())
# print(string_5.isalnum())
# print(string_5.isspace())
# print(string_5.islower())
# print(string_5.isupper())
# print(string_5.istitle())


#
# string_5 = "eagle"
# print(string_5.isalpha())
# print(string_5.isdigit())
# print(string_5.isalnum())
# print(string_5.isspace())
# print(string_5.islower())
# print(string_5.isupper())
# print(string_5.istitle())



# string_5 = "EAGLE"
# print(string_5.isalpha())
# print(string_5.isdigit())
# print(string_5.isalnum())
# print(string_5.isspace())
# print(string_5.islower())
# print(string_5.isupper())
# print(string_5.istitle())


# Q. to extract only alphabets from the string given
# msg = "6989%$%$%#hgfvhjvhjbhjb  241(*GFJU UFG"
#
# empty_ = ""
#
# for i in msg :
#     if i.isalpha() :
#         empty_= empty_ + i
#     else : continue
#
# print(empty_)


# Formatting of the Strings

# username = 'ironman'
# otp = 4777

# print("Hi username, your otp for the transaction is otp")
# print("Hi ironman, your otp for the transaction is 4562")


# print("Hi {}, your otp for the transaction is {}".format(username, otp))

# print("Hi {}, your otp for the transaction is {}".format(otp, username))

# print("""Hi {}, your otp for the transaction is {}.
# Please don't share it with anyone {}.
# """.format(username, otp, username))


# print("""Hi {0}, your otp for the transaction is {1}.
# Please don't share it with anyone, {0}.
# """.format(username, otp))

# String is Immutable object
# Mutable -> to modify any char inside the string at any time.
# insertion, deletion, updation

stringName = 'Earth Geometry'
# print(stringName.insert(10, 20))

# print(stringName[2])
# stringName[2] = 'Z'

# stringName.remove('Earth')

# delete any object in python
# del objectName

# x = 100
# y = 45.25
# z = True
# print(x, y, z)
#
# del x, y, z
#
# print(x, y, z)



#** developer / programmer logic to perform insertion, updation and deletion in strings

stringName = 'Earth Geometry'
# delete the Entire string, but not the character
# del stringName
# print(stringName)


# del stringName[0]
# print(stringName)

# # insertion
# print(stringName[ : 6])
# print(stringName[6 : ])
#
# print(stringName[ : 6] + "2021 " + stringName[6 : ])

# stringName = stringName[ : 6] + "2021 " + stringName[6 : ]


# Updation
stringName = 'Earth Geometry'
# print(stringName[ : 6])

print(stringName.replace("Earth", 'Mars'))


















