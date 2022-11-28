
############ DICTIONARY #############

# A dictionary is an unordered data structure
# represents a group of elements in the form of key-value pair.
#
# Elements in dictionary can be accessed by calling key in dictionary
#
# Values are Mutuable
# Keys are immutuable.
#
# Dictionary is represented as {}.


# d = {}
# print(type(d))

# d = {k : v}

# d = {1 : 'a',
#      2 : 'b',
#      3 : 'C'}
#
# print(d)
# print(type(d))


# Rules to follow while creating the dictionary

# KEYS are Immutable
# VALUES are Mutable

# d = {1 : 'a',
#      "B" : 100,
#      5.2 : True,
#      False : 44.44,
#      "Hi Friend" : 8-8j,
#      0 + 4j : 'You are AWESOME'}
#
# print(d)
#
# # Keys in dictionary
# print(d.keys())
#
# # Values in dictionary
# print(d.values())
# #
#
#
#
# # d = {1 : 'a',
# #      "B" : 100,
# #      5.2 : True,
# #      False : 44.44,
# #      "Hi Friend" : 8-8j,
# #      0 + 4j : 'You are AWESOME',
# #      'list' : [1,2,4,0],
# #      "dict" : {1 : "A", 2 : "B"},
# #      'tuple' : ('a', False, 'Green')}
# #
# # print(d)
#
# #
# # d = {1 : 'a',
# #      "B" : 100,
# #      5.2 : True,
# #      False : 44.44,
# #      "Hi Friend" : 8-8j,
# #      0 + 4j : 'You are AWESOME',
# #      ('a', False, 'Green') : 'tuple' }
# #
# # print(d)
# #
# #
# #
#
#
#
# # Basic Operations
#
# d = {1 : 'a',
#      "B" : 100,
#      5.2 : True,
#      False : 44.44,
#      "Hi Friend" : 8-8j,
#      0 + 4j : 'You are AWESOME'}
#
# # length => total key -value pairs
# # print(len(d))
#
# # d[1 : 3]
#
# # d + d
#
# # d * 3
#
#
# # Membership Operator (in)
# # Key is present in side the dictionary
#
# print(99 in d)
# print('B' in d) # B as a key is present
# print(44.44 in d) ## 44.44 as value is not able to access
#




# Built in functions

# Dictionary is Mutable

# d = {1 : 'A',
#      2 : 'B',
#      3 : "C"}
#
# print(d)

# Insert a key value PAIR
# dict[keyName] = Value

# d[10] = "Freedom"
# d[5.2] = 99999
#
# print(d)


# Update a Value against the KEY
# dict[keyName]= Value

# print(d[3])
# d[3] = 'Python'
# print(d)


# Delete  KEY VALUE pair
# d = {1 : 'A',
#      2 : 'B',
#      3 : "C"}
#
# print(d)
#
# del d[1]
#
# print(d)




# Built in functions

# d = {1 : 'A',
#      2 : 'B',
#      3 : "C"}
# print(d)
#
# # d.clear()
# # print(d)
#
# s1 = d.copy()
# print(s1)
# print(type(s1))
#
# print(id(d))
# print(id(s1))
#



### Iterate over Key and Value

d = {1 : 'a',
     "B" : 100,
     5.2 : True,
     False : 44.44,
     "Hi Friend" : 8-8j,
     0 + 4j : 'You are AWESOME'}

# print(d)
# print(d.keys())
# print(d.values())
# print(type(d.keys()))

# Loop over KEY

# for i in d.keys() :
#     print(i)


# for i in d.values() :
# #     print(i)
#
# print(d.items())
#
# for i, j in d.items() :
#     print(i, " : ", j)
#
# print()
#
# for i in d.items() :
#     print(i)













































