

# Operators in Python


# 1 . Arithmetic Operators
#  + - * / ** // %

num1 = 100
num2 = 50

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 % num2) # remainder
# print(3 % 2)

# print(10 / 7)  # floor division
#
# print(10 // 7)  # floor division
#
# print(9999999 / 5555)  # floor / integer division
# print(9999999 // 5555)  # floor division

# res = 10 // 7
# print(res,type(res))

# print(8 ** 2)  # exponential
# print(8 ** 3)
#

#
#
# num = 100
# print(num // 25)
#
# # num = num // 25
# num //= 25
# print(num)
#
# a = 10
# a += 1   # a = a + 1
# # a -=1  # a = a - 1
#
# print(a)
#
# # i++ => i = i + 1   => i += 1



# 2. Assignment operator (=)
# assign a value (literal) to a variable
#
# joy = 100
# pilot = True
#
# print(joy, type(joy))
# print(pilot, type(pilot))

# False = 'Hi'

# 10000000 = house


# 3. Relational / Comparison Operators
# Compare one operand with the other
# returns the answer in boolean

# >, <, >=, <= , == , !=
#
# print(100 > 200)
# print(100 < 200)
# print(100 >= 200)
# print(100 <= 200)
# print(100 == 200)
# print(100 == 100)
# print(100 != 200)




# 4. Logical Operators

# and, or, not

# And Logic -> Return TRUE, if all conditions are True, else FALSE

# x y  z
# 0 0  0
# 1 0  0
# 0 1  0
# 1 1  1

# print(10 > 3)
# print(5 == 5)

# print( (10 > 3) and (5 == 5) )
# print( (10 < 3) and (5 != 5) )
# print( (10 > 3) and (5 != 5) )
# print( (10 < 3) and (5 == 5) )


# OR logic => Return FALSE if all conditions are FALSE, else TRUE


# x y  z
# 0 0  0
# 1 0  1
# 0 1  1
# 1 1  1

# print( (10 > 3) or (5 == 5) )
# print( (10 < 3) or (5 != 5) )
# print( (10 > 3) or (5 != 5) )
# print( (10 < 3) or (5 == 5) )


# NOT Logic => converts True to False and vice versa

# print( not(10 > 3) )
# print( not(5 != 5) )

# print(not(0))
# print(not(False))



# 5. Identity Operator => is, is not
# Evaluate the data type of the operand
# data types = int, float, str, bool, complex

# is operator returns TRUE, if operand belongs to the specified class

# x = 100
# print(type(x))
#
# print(type(x) is int)
# print(type(x) is float)
#

# is not

# x = 100
# print(type(x))
#
# print(type(x) is not int)
# print(type(x) is not float)


# print(100 == 100)
# print(100 is 100)
# print( type(100) is type(100))

# print(100 == 100.0)
# print(100 is 100.0)


# print(isinstance(100, int))
# print(isinstance(100, str))   # type(100) to the data type mentioned




# 6. Membership Operator
# check weather element is present inside the sequence
# in, not in

# in => Returns TRUE if element is found inside the sequence, else FALSE

# print(100 in 1000) # element in element

# str = seq. of char
# list, tuple, set => seq of elements
# dict

# print('delhi' in "My Birth city is DELHI")
#
# print('DELHI' in "My Birth city is DELHI")
#
# print("1234" in 'Your OTP is 12345')

#
# print(10 in [4, 'Tiger', False, 10.0])
#
# print(10 in [4, 'Tiger', False, 10.5])
#
# print(10 == 10.0)
# print(10 == 10.5)

# print("flag" in "You got red")
# print("flag" not in "You got red")
#


# 7. Bitwise Operator
# Bit level operations

# &,  |, <<, >>, ~

# Bitwise and (&)
# Return TRUE, if all are TRUE

# 0 & 0 => 0
# 0 & 1 => 0
# 1 & 0 => 0
# 1 & 1 => 1
#


### Binary representation => 0b
## Type cast a number to binary => bin(number)

a = 10
b = 5

a_bin = bin(a)
b_bin = bin(b)

# print(a_bin, b_bin)

# 1 0 1 0 -> a bin
# 0 1 0 1  -> b bin
#
# 0 0 0 0
# print(0b0000)
# print(int(0b0000))
# print(0b0001)
# print(int(0b0001))

# print(a & b)

# Bitwise Or operator (|)
# Return FALSE, if all are FALSE

# 0 | 0 => 0
# 0 | 1 => 1
# 1 | 0 => 1
# 1 | 1 => 1

# a = 10
# b = 5
#
# a_bin = bin(a)
# b_bin = bin(b)
#
# # print(a_bin, b_bin)
#
# # 1 0 1 0
# # 0 1 0 1
# # 1 1 1 1
#
# # print(0b1111)
#
# print(a | b)
#


# Bitwise negation (~)
# ~number  ==> -(number + 1)

# print(~12)  # - (12 + 1)



# Bitwise Left Operator (<<)
# number << n bits   ==> shift binary number by n bits from the left

print(100 << 10)  # shift bin100 by 10 bits from the left


# step1 - get the binary value of the number
# s1 = 100
# print(bin(s1))  # 1100100


# step2 - get the 32 or 64 bit representation
# 00000000000000000000000001100100

# print(len("00000000000000000000000001100100"))

# step3 - shift n bits from the left and insert n 0's to the right
# finalNum = 0b00000000000000011001000000000000


# step3 - get the int value of the bin finalNum

# print(finalNum)  ## 102400






















































































