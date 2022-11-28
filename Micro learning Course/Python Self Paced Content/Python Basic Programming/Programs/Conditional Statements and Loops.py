
# Conditional statements and loops

# if else, for, while, break, continue, pass


# IF BLOCK

# if (expression) :
#     (statements....)
#     (sta..)




# # Area of the Figure
# sides = int(input("Enter number of Sides : "))
#
# # area of circle
# if (sides == 1) :
#     rad = int(input("Enter the Radius : "))
#     print('Area of circle = ', 3.14 * rad * rad)
#
# # area of triangle :
# if (sides == 3) :
#     p = int(input("Enter Perpendicular : "))
#     b = int(input("Enter Base : "))
#     print('Area of Triangle = ', 0.5 * p * b)
#
# # area of rectangle
# if (sides == 4) :
#     l = int(input("Enter Length : "))
#     b = int(input("Enter Base : "))
#     print('Area of Rectangle = ', l * b)


## IF ELSE BLOCK

# if (expression) :
#     star;;;;;
#     hgffjbbgjf...
# else :
#     hgfudyhgwuidg

# Area of the Figure
# sides = int(input("Enter number of Sides : "))

# # area of circle
# if (sides == 1) :
#     rad = int(input("Enter the Radius : "))
#     print('Area of circle = ', 3.14 * rad * rad)
# else :
#     print("TRY AGAIN..")
#
#



## IF ELIF ELSE BLOCK

# if (expression) :
#     wghfqugdvbwqujdqw
#     dqwdqwddwwqd
# elif (expression) :
#     hjfgqyudhjwdwq
#     ddwqdqwdqdw
# else :
#     dhjgfhkjduwhdkj



# # Area of the Figure
# sides = int(input("Enter number of Sides : "))
#
# # area of circle
# if (sides == 1) :
#     rad = int(input("Enter the Radius : "))
#     print('Area of circle = ', 3.14 * rad * rad)
#
# # area of triangle :
# elif (sides == 3) :
#     p = int(input("Enter Perpendicular : "))
#     b = int(input("Enter Base : "))
#     print('Area of Triangle = ', 0.5 * p * b)
#
# # area of rectangle
# elif (sides == 4) :
#     l = int(input("Enter Length : "))
#     b = int(input("Enter Base : "))
#     print('Area of Rectangle = ', l * b)
#
# else :
#     print("TRY AGAIN...")
#




## NESTED IF ELSE :

# if (expression) :
#     if (expression) :
#         fefefffqw
#     else :
#         sjhbvgjyhqdnbjwd
#
# else :
#      hjusbd kdbwq kjhdwqnkjdw


# # Area of the Figure
# sides = int(input("Enter number of Sides : "))
#
# # area of circle
# if (sides == 1) :
#     rad = int(input("Enter the Radius : "))
#     print('Area of circle = ', 3.14 * rad * rad)
#
# # area of triangle :
# elif (sides == 3) :
#     p = int(input("Enter Perpendicular : "))
#     b = int(input("Enter Base : "))
#     print('Area of Triangle = ', 0.5 * p * b)
#
# # area of quadilateral
# elif (sides == 4) :
#     shape = input("Enter [R] for Rectangle or [S] for Square : ")
#
#     if (shape == 'R') :
#         l = int(input("Enter Length : "))
#         b = int(input("Enter Base : "))
#         print('Area of Rectangle = ', l * b)
#
#     elif (shape == 'S') :
#         s = int(input("Enter Side : "))
#         print('Area of Square = ', s * s)
#     else :
#         print("Invalid Value")
#
# else :
#     print("TRY AGAIN...")





# Statements - break, continue, pass


# break = to come out of the loop or block, if expression is TRUE
# continue = to skip the block if expression is TRUE
# pass - to just let it go the execution


# msg = "The OTP for current transaction is 1234"
# print(msg)
# otp = input("Enter the OTP : ")

# if (otp in msg) :
#     print("Authorize the transaction")
# else :
#     print("INVALID")



# msg = "The OTP for current transaction is 1234"
# print(msg)
#
# for i in range(0, 3 ) :
#     otp = input("Enter the OTP : ")
#     if (otp in msg):
#         print("Authorize the transaction")
#         break
#     else:
#         print("TRY AGAIN")



# msg = "The OTP for current transaction is 1234"
# print(msg)
#
# for i in range(0, 3 ) :
#     otp = input("Enter the OTP : ")
#     if (otp in msg):
#         print("Authorize the transaction")
#     else:
#         continue
#         print("TRY AGAIN")




# msg = "The OTP for current transaction is 1234"
# print(msg)
#
# for i in range(0, 3 ) :
#     pass
#     otp = input("Enter the OTP : ")
#     if (otp in msg):
#         print("Authorize the transaction")
#
#     else:
#
#         print("TRY AGAIN")
#
#     pass
#


# LOOPS

# for block, while block


# range - defines a numerical seq from start to end
# range(start, end, step size)  # end is excluded

# print(list(range(1, 21)))

# for iterator in range() :
#     ahgagkhjahndhkjandbh
#     dfewfe
#     fewf
#     ewfewf
#     ewfewf



# for iterator in seqName :
#     ahgagkhjahndhkjandbh
#     dfewfe
#     fewf
#     ewfewf
#     ewfewf


# for nitish in range(1, 11) :
#     print(" Hi" )
    # nitish = nitish + 1 # nitish + stepsize


# for i in range(1, 10) :
#     print("$" * i)



# for i in range(1, 10, 5) :
#     print("$" * i)  # 1 6

# for i in range(10, 0, -1) :
#     print("$" * i)


# msg = "Welcome to Delhi"
# print(msg)
# print(msg[11])  # indexing
# print(len(msg))


# for i in range(0, len(msg)) :
#     print(msg[i])   # msg[0], msg[1], msg[2]...msg[15]
#
# for i in msg:
#     print(i)



# msg = "Welcome to Delhi"
#
# for i in msg:
#     print(i, end = "-")  #W e l c o m e

# print(4, True, 5.2, "jhgjh", sep = " -- ** --")
# print(end = "\n")







# msg = "Welcome to Delhi"
#
# for i in msg:
#     if (i == "D") :
#         break
#     else :
#         print(i)




# msg = "Welcome to Delhi"
#
# for i in msg:
#     if (i == "e") :
#         continue
#     else :
#         print(i)



# msg = "Welcome to Delhi"
#
# for i in msg:
#     pass
#     print(i)
#





# WHILE LOOP

# iterator =
# while (expression) :
#     hdgfuhj  ew
#     ewq
#     r rwqr
#
#     iterator = iterator +- 1



# Keep on dividing the number by 15 till 0 is given as numerator

# while True :
#     numerator = int(input("Enter numerator : "))
#
#     if numerator == 0:
#         break
#
#
#     res = numerator / 15
#     print(res)
#
#




msg = "Welcome to Delhi"  # 16
# print(msg[0])
# print(msg[15])


# i = 0
# while i < len(msg) :
#     print(msg[i])
#
#     i = i + 1


# reversing the string
i = len(msg) - 1  # 15 14 13
while i >= 0  :
    print(msg[i])

    i = i - 1

























































