

## ARRAYS ###
# it is defined as collection of homogeneous(same data type) elements
# it is represented by []
# use 'array' library


# How to write an array
import array

# arr = array.array('i', [7, 2, 0, -8])
# print(arr)
#
# print(type(arr))



# arr = array.array('i', [7, 2, 0, -8, 55.55])
# print(arr)
#
# print(type(arr))



# arr = array.array('f', [7, 2, 0, -8, 55.55])
# print(arr)
#
# print(type(arr))



# arr = array.array('u', ["h", 'T', 'k', '7'])
# print(arr)
#
# print(type(arr))
#
# import numpy
#
# n1 = numpy.array(["Hello", 'delhi', 75])
# print(n1)
# print(type(n1))



##### Basic Operations  ##############

import array

# 1. Length => total number of elements inside the array
# len(arrayName)

# a1 = array.array('i', [7,0,1,-6,-8,10])
# print(len(a1))


# 2. Indexing => Return the element at defined position number
# arrName[pos]
#
# a1 = array.array('i', [7,0,1,-6,-8,10])
# print(a1[2])
# print(a1[-1])
#

# 3. Slicing => Returns the chunk of array
# arrName[start : end : step size]
# start = 0
# end = length of seq
# step size = 1

# a1 = array.array('i', [7,0,1,-6,-8,10])
# print(a1[0 : 4])
#
# # return the element at  odd pos only
# print(a1[1 : : 2])
#

# Basic Operations

# 1. Concatenation (+)

# a1 = array.array('i', [7,0,1,-6,-8,10])
# a2 = array.array("f", [0.2, 5.2, -6.8, 4.2])
# # print(a1 + a2)
#
# print(a1 + a1)
# print(a2 + a2)


# 2. Repitition (*)

# a1 = array.array('i', [7,0,1,-6,-8,10])
# # print(a1 * 5)
#
# # repeat the elements 8 times which are at position multiple of 3
#
# # print(a1[0 : : 3] * 8)
# print(a1[4] * 2)


# 3. Membership (in)
# Return TRUE if element is present inside the array

# a1 = array.array('i', [7,0,1,-6,-8,10])
#
# print(900 in a1)
# print(0 in a1)
#







# Built in functions

# Array is also a mutable object
# you can modify the element at any position number (insert, delete, update)


# Insertion

# APPEND => inserting an elment to the end of the array
# a1 = array.array('i', [2, 8, -3, 0, -4, 1])
# a1.append(99)
# a1.append(-100)
# a1.append(0)
# print(a1)

# INSERT => inserts at defined position number
# arrName.insert(pos, value)

a1 = array.array('i', [2, 8, -3, 0, -4, 1])

# # insert -100 at pos 4
# print(a1[4])
# a1.insert(4, -100)
# print(a1)
#
# # insert 840 at 0 pos
# a1.insert(0, 840)
# print(a1)
#
#
# # insert 1111 at end of array
# a1.insert(len(a1), 1111)
# print(a1)


# Updation
# arrayName[pos] = value

# a1 = array.array('i', [2, 8, -3, 0, -4, 1])

# replace 0 by 9999
# print(a1[3])
# a1[3] = 9999
# print(a1)

# modify the negative element to the square of it

# for each in a1 :
#     if each < 0 :
#         pos = a1.index(each)
#         a1[pos] = a1[pos] ** 2
#
# print(a1)




# Removing the element

# 1. remove by element VALUE, but only the first occurence of it
# arrayName.remove(element)

# a1 = array.array('i', [2, 8, -3, 0, -4, 1, 0])
# a1.remove(0)
#
# print(a1)


# a1 = array.array('i', [2, 8, -3, 0, -4, 1, 0])
# for each in a1 :
#     if 0 in a1 :
#         a1.remove(0)
#
# print(a1)


# 2. POP method
# removes the element from the end of the sequence and returns the element

# a1 = array.array('i', [2, 8, -3, 0, -4, 1, 0])
# print(a1.pop())
# print(a1.pop())
# print(a1.pop())
# print(a1.pop())
# print(a1.pop(1))
#
# print(a1)



# Built in functions

# 1. Count => returns the occurence of the element
# arrayName.count(element)

# a1 = array.array('i', [2, 8, -3, 0, -4, 1, 0])
# print(a1.count(0))
# print(a1.count(-3))


# 2. Reverse the array
# arrayName.reverse()


# a1 = array.array('i', [2, 8, -3, 0, -4, 1, 0])
# a1.reverse()
# print(a1)



# 3. Extend
# inserting elements freom one array to another

# a1 = array.array('i', [2, 8, -3, 0, -4, 1, 0])
# a2 = array.array("i", [-88, -77, -55])
#
# a1.extend(a2)
# print(a1)
#
#
#
# a1 = array.array('i', [2, 8, -3, 0, -4, 1, 0])
# a2 = array.array("i", [-88, -77, -55])
#
# a1.append(12)
# print(a1)
#




# 4. Indexing => Return the position number of the element
# arrayName.index(elemtn)

# a1 = array.array('i', [2, 8, -3, 0, -4, 1, 0])
# print(a1.index(-4))
# print(a1.index(2))


















































