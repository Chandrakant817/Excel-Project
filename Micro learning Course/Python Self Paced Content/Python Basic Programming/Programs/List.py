
### LIST ###
# collection of elements of different data types
# list is represented by []
# List are mutable -> modify the element inside the list at any time
# Objects can be type casted to list by using the syntax --- list(sequence)   # sequence is string, list, tuple, sets, dict



# c1 = []
# print(type(c1))


# listName = [False, 1.2, 3, 8-8j, 'G', 'Moons and Stars']
# print(type(listName))
# print(listName)


# listName = [False 1.2  3 8-8j 'G' 'Moons and Stars']
# print(type(listName))
# print(listName)

# print(list("jhg igubiuh"))

# print(list( (4, 7, 8) ))

# print(type((4, 7, 8)))



# basic Operations on List


# 1. length - total number of elements
listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]

# print(listName)
# print(len(listName))


# 2. Indexing -> Return the element with reference to the position number
# listName[index]

listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
# print(listName)
# print(listName[0])
# print(listName[4])
#
# print(listName[len(listName) - 1])

# 3. Slicing -> Extract chunk of elements from the list
# listName[start : end : stepsize]
# start => default value is 0
# end => default value is length of the list. end is exluded
# stepsize => default value is 1


listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
# print(listName)
# print(listName[0 : len(listName) : 1])
#
# # print(listName[0 : len(listName) : 2])  # 0 2 4
#
# print(listName[ : len(listName) : 1])
#
# print(listName[0 : : 1])
#
# print(listName[ : : ])
#
# # print(listName[ ])
#
# print(listName[ : :  -1])

# print(listName[ :  : 1])



# basic Operations on List

# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
# print(listName)

# concatenation (+)

# print([4, 8] + [-6, False] + [0.2])
# print([4, 8] + [-6, False] + [0.2] + 'hello')


# repitition => listName * integer
# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
# print(listName)
# print(listName * 2)
# print()
#
# print(listName[0 : 3] * 5)
#
# print(listName[3])
# print(listName[3] * 10)
#
# print(listName[2])
# print(listName[2] * 10)
#

# print(listName[0])
# print(listName[0] * 2)  # TrueTrue; 2
# print(str(listName[0]) * 2)  # TrueTrue; 2


# membership : in, not in
# in => returns TRUE, if element is present inside the sequence, else False

# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
#
# print(80 in listName)
# print(100 not in listName)
#
# print("Moons" in listName)
#
# print(listName[4])
# print("Moons" in listName[4])



##################### List is Mutable Object #################

# any element can be modified at any time at any place
# insert, delete, update

# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
# print(listName)

# Insertion

# a. Append = Insert at the end of the list
# listName.append(element)

# add 0 in the end of the list
# listName.append(0)
# listName.append(False)
# listName.append(9999999999)
# listName.append(['a', 'b'])
#
#
# print(listName)


# b. Insert = Insert the element at any position number
# listName.insert(pos, element)

# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
# print(listName)

# add False at pos 2

# print(listName[2])
# listName.insert(2, False)
# print(listName)


# insert ['heaven', 'hell'] at pos 0
# listName.insert(0, ['heaven', 'hell'])
# print(listName)


# Use case of APPEND
# mobile = []
# for i in range(0,3) :
#     # print(i)
#
#     x = input("Enter Mobile Number : ")
#     mobile.append(x)
#
# print(mobile)




## Updation of element
# listName[index] = value


# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
# print(listName)
#
# # replace 'k' by False
# # replace 'moons and stars' by 'earth '
# print(listName[3])
# print(listName[4])
#
# listName[3] = False
# listName[4] = 'Earth'
#
#
# print(listName)




## Delete the value

# 1. remove = deletes the first occurence of elemenbt from
# the list by passing the value
# listName.remove(value)


# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j, True]
# print(listName)
#
# # listName.remove(True)
# # print(listName)
#
# for i in listName :
#     if True in listName :
#         listName.remove(True)
#     else :
#         continue
#
#
# print(listName)


# 2. pop method - deletes the last element from the list and
# returns the last element

# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j, True]
# print(listName)
#
# print(listName.pop())
# print(listName.pop())
# print(listName.pop())
# print(listName.pop())
# print(listName.pop())
#
#
# print(listName)



# # 3. del = delete the element from the python
#
# x = 4
# y = 50.25
# z = True
# s = 'moons and stars'
# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j, True]
# print(listName)
#
# # del x, y, z, s, listName, s[10]
# # print(x, y, z, s, listName)
#
# # del s[10]
# # print(s)
#
# del listName[1]
# print(listName)
#


# LIST Built in  Functions

# sum, clear, copy, extend, sort, insert, remove, pop, append


# 1. Clear the LIST

# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
# print(listName)
#
# listName.clear()
# print(listName)

# 2. Indexing => Return the position number of the element inside the list

# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
# print(listName)

# print(listName.index('k'))
# print(listName.index(80))

## #Q. Insert False before 80 ???

# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
# print(listName)

# pos = listName.index(80)
# listName.insert(pos, False)
# print(listName)



# 3. Copy

# listName = [True, 80, -5.66, 'k', 'Moons and Stars', 7-1j]
# print(listName)
#
# print(id(listName))
#
# abc = listName.copy()
# print(id(abc))
#
# xyz = listName
# print(id(xyz))
#
#
# listName.pop()
# print(listName)
# print(xyz)
# print(abc)


# 4. Extend => copying the values of one list to another

# Insert s2 elements into s1

# s1 = [4, "Life"]
# s2 = [50.5, False]
#
# s1.append(s2)
# print(s1)
#
#
#
# s1 = [4, "Life"]
# s2 = [50.5, False]
#
# s1.extend(s2)
# print(s1)


# 5. Sort => sort the elements inside the list in ascending order

# d1 = [9, 1, 0, -9, 22]
# print(d1)
# d1.sort()
# print(d1)
#
#
# d1.sort(reverse = True)
# print(d1)



# 6. Math operations on the list
# d1 = [9, 1, 0, -9, 22]
# print(d1)
#
# print(sum(d1))
# print(min(d1))
# print(max(d1))




























