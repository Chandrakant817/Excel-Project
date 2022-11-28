
### TUPLE ###
# collection of elements of different data types
# tuple is represented by ()
# Tuple are immutable -> can't modify the element inside the tuple at any time
# Objects can be type casted to tuple by using the syntax --- tuple(sequence)
# sequence is string, list, tuple, sets, dict


# How to write a tuple

# t1 = ()
# print("type(t1) = ", type(t1))
#
# t2 = (False, 45, 9.3, 'J', 'Earth & Ocean', 8-8j)
# print(t2)
# print("type(t2) = ", type(t2))
#
# t3 = (75, )
# print("type(t3) = ", type(t3))
# print(len(t3))





# basic Operations in Tuple

# 1. Length => Return total elements inside tuple
# t1 = (True, "L", 50.25, [1,2], 'Delhi to Mumbai', 8-9j, 999)
# print(t1)
# print(type(t1))
#
# print(len(t1))



# 2. Indexing => Return the element at specified position number
# tupName[pos]

# print(t1)
# t1 = (True, "L", 50.25, [1,2], 'Delhi to Mumbai', 8-9j, 999)
#
#
# print(t1[1])
# print(t1[4])
#
# # x = [1, 2] = t1[3]
# print(t1[3][1])
#
# print(t1[-1])
# print(t1[len(t1) - 1])
#


# 3. Slicing => Return a chunk of seq from the tuple
# tupName[start : end : stepsize]

# t1 = (True, "L", 50.25, [1,2], 'Delhi to Mumbai', 8-9j, 999)
# # print(t1)
# #
# #
# # print(t1[0 : 3 : 1])
# # print(t1[0 : 3 ])
# # print(t1[0 : 3 : 2])
#
# # elements at only odd position number
# print(t1[1 : : 2])
#






# Basic Operations

# t1 = (True, "L", 50.25, [1,2], 'Delhi to Mumbai', 8-9j, 999)
# print(t1)


# 4 Concatenation (+)

# print( (False, 1, "K") + (80, 41.2, True) + (100, ) )


# 5. Reptition (*)

# print( ("N", ) * 10)
# print( (0, ) * 5)
#
# print( (False, 'Hi') * 2 )
#



# 6. Membership (in)
# => Returns TRUE if element is present inside the tuple


# t1 = (True, "L", 50.25, [1,2], 'Delhi to Mumbai', 8-9j, 999)
# print(t1)

# print('l' in t1)
# print('L' in t1)
#
# print(2 in t1)

# print(t1[3])
# print(2 in t1[3])









# Built in Functions

# t1 = (4, 7.2, "Kite", False, 4, 4)

# Count of the element

# print(t1.count(4))
# print(t1.count(1200))

# Indexing

# print(t1.index(4))
# print(t1.index(False))
#
# print(t1.index(-99))
#




# TUPLE IS IMMUTABLE OBJECT

#Mutable means that element inside the sequence can be modified (insert, update, delete)

# t1 = (4, 7.2, "Kite", False, 4, 4)

# t1.insert(1, 999)

# print(t1[2])

# t1[2] = 'Sky'

# t1.remove(4)

# t1.pop()

# x = 100
# # del x
#
# print(x)

# del t1[2]

# print(t1)




t1 = (4, 7.2, "Kite", False, 4, 4)

# INSERT 99 at pos 5

# print(t1[5])

res = t1[ : 5] + (99, ) + t1[5 : ]

print(t1[ : 5])
print(t1[5 : ])

print(res)
















































































