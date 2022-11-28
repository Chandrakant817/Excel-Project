
################### SETS ###

# Syntax : s1 = set(); {""}, {''}
# Represented by unordered collection of unique datatype elements.
# set itself is mutable.
# No Index Wise Operations possible HERE

# s1 = {False, 1.2, 50, 'SKY BLUE', 'a'}
# print(s1)
# print(type(s1))

# s1 = {False, 1.2, 50, 'SKY BLUE', 'a', -8}
# print(s1)

# Basic Operation in SET

# s1 = {False, 1.2, 50, 'SKY BLUE', 'a', 'a', 50, False}
# # print(s1)
# # print(type(s1))
# #
# #
# # print(len(s1))
#
# # s1[5]
# # s1[0 : 2]
#
# # s1 * 5
# # s1 + s1
#
# print(False in s1)
# print("a" in s1)
#







# Built in Functions

# Mutable => Modify the element

# s1 = {True, 11, 52.25, "K", 'Tigers Zoo', 11, "K", 11}
# print(s1)


# 1. set.add(elemnt) => insert the element inside the set

# s1 = {True, 11, 52.25, "K", 'Tigers Zoo', 11, "K", 11}
# print(s1)
#
# s1.add(0)
# s1.add('Mango')
# s1.add(45.3366)
#
# s1.add('a', 'b')
# print(s1)


# 2. set.remove(element) => Remove the element by referring to its value

# s1 = {True, 11, 52.25, "K", 'Tigers Zoo', 11, "K", 11}
# print(s1)
# s1.remove(11)
#
# print(s1)

# 3. set.pop()
# s1 = {True, 11, 52.25, "K", 'Tigers Zoo', 11, "K", 11}
# print(s1)
#
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())
#
# print(s1)



#. Updation => inserting mulitple values

# s1 = {True, 11, 52.25, "K", 'Tigers Zoo', 11, "K", 11}
# # s1[5] = 4000
#
# s1.update(['a', 'b', 80])
# print(s1)



# clear the SET

# s1 = {True, 11, 52.25, "K", 'Tigers Zoo', 11, "K", 11}
# s1.clear()
#
# print(s1)








### SET OPerations ######

# UNION => Returns set containing all items from both sets

# s1 = {1, 'sql', 'python', 5.01}
# s2 = {'python', 1, 'a', 'b', -99}
#
# res = s1.union(s2)
#
# print(s1)
# print(s2)
# print(res)



# INTERSECTION => Return sets containing common elements from both sets

s1 = {1, 'sql', 'python', 5.01}
s2 = {'python', 1, 'a', 'b', -99}

res = s1.intersection(s2)

print(s1)
print(res)


# DIFFERENCE
s1 = {1, 'sql', 'python', 5.01}
s2 = {'python', 1, 'a', 'b', -99}

res = s1.difference(s2)  # s1 - s1(intersection)s2

# print(s1)
# print(s2)
print(res)



















