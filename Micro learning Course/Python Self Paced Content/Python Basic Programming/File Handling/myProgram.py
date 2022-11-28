
## FILE HANDLING  ###

# Data is very important
# file that is opened, make sure they are closed also. Data is not lost

# # Types of Files :
# 1. Text File
# 2. Binary File


# Open File and Close File


# f = open(fileName, mode)

# fileName => C\Desktop\File.txt, File.txt
# mode = r, w, a
# f = file handler

# f.close()  -- closing the file


## Read And Write in a file

# You can read the file, only if it exists
# you can create a text file by pursuing your write operation
# In write mode, the previous data is overwritten


# f = open('data.txt', 'w')
#
# f.write("10 + 20 = 30 \n")
# f.write("This is Python File Handling Class.")
# f.write("\n")
# f.write("Earth and Ocean.")
#
# f.close()
#
#
#
# f = open('data.txt', 'r')
# msg = f.read()
# print(msg)
# f.close()





#### Append Action

# Append action writes the data after the end of previous file
# No overwritten of data
# File will be created if it doesn't exist
# Both Append and Write mode uses file handler 'write' action to send data to the file


# f = open('data.txt', 'a')
#
# f.write("\n 50 - 6 \n")
# f.write("This is the Append Action.")
# f.write("\n")
# f.write("Sky is Dark")
#
# f.close()
#
#
#
# f = open('data.txt', 'r')
# msg = f.read()
# print(msg)
# f.close()










## Modes of Reading the Data

# 1. Read mode
# read(n) => n defines, how many characters to read from the 0th index


# f1 = open('habit.txt', mode = 'r')
# msg_1 = f1.read()
# print(msg_1)
# print(len(msg_1))
# f1.close()
#
# """
# Habit: a settled or regular tendency or practice, especially one that is hard to give up.
#
# The topic of this article is particularly interesting to me because I believe that most of us really donâ€™t consciously create our habits, and yet, they are what influence our actions and thoughts the most.
#
# A productive habit could be a morning ritual of gratitude journaling, or even just drinking a glass of water when you get out of bed.
#
# A self-sabotaging habit could be procrastinating on tasks that could be easily completed on the spot, or mindlessly eating bread when you sit down for dinner.
#
# Most of our thoughts and actions seem to be on autopilot.  This could be great if habits are designed proactively, but it can also harm us in the long run.
#
# We tend to act and think based on what automatically serves our most immediate needs and what we are familiar with.  This often works against us in the long run because we get used to making unconscious (unaware) decisions.
#
# """
#
#
# f1 = open('habit.txt', mode = 'r')
# msg_1 = f1.read(50)
# print(msg_1)
# print(len(msg_1))
# f1.close()
#
# """
# Habit: a settled or regular tendency or practice, especially one that is hard to give up.
#
# The topic
#
# """
#


# 2. Readline mode
# Read the first line only
# readline(n) => n defines, how many characters to read from first line only
#
# f2 = open('habit.txt', mode = 'r')
#
# msg_2 = f2.readline()
#
# print(msg_2)
# print(len(msg_2))
# f2.close()
#
# print("-" * 100)
#
#
#
# f2 = open('habit.txt', mode = 'r')
#
# msg_2 = f2.readline(50)
#
# print(msg_2)
# print(len(msg_2))
# f2.close()
#
# print("-" * 100)
#
# f3 = open('habit.txt', mode = 'r')
#
# msg_3 = f3.readline(500)
#
# print(msg_3)
# print(len(msg_3))
# f3.close()




# 3. Readlines mode
# returns the message in the list format
#
# f1 = open('habit.txt', mode = 'r')
#
# msg_1 = f1.readlines()
#
# print(msg_1)
# print(len(msg_1))
#
# for m in msg_1 :
#     print(m)
#
# f1.close()


"""
['Habit: a settled or regular tendency or practice, especially one that is hard to give up.',
"\n",
'The topic of this article is particularly interesting to me because I believe that most of us really donâ€™t consciously create our habits, and yet, they are what influence our actions and thoughts the most.'
'\n',
'A productive habit could be a morning ritual of gratitude journaling, or even just drinking a glass of water when you get out of bed.'

A self-sabotaging habit could be procrastinating on tasks that could be easily completed on the spot, or mindlessly eating bread when you sit down for dinner.

Most of our thoughts and actions seem to be on autopilot.  This could be great if habits are designed proactively, but it can also harm us in the long run.

We tend to act and think based on what automatically serves our most immediate needs and what we are familiar with.  This often works against us in the long run because we get used to making unconscious (unaware) decisions.

"""





# find out the passage where  "self-sabotaging habit" is mentioned
# word = 'self-sabotaging habit'
#
#
# f1 = open('habit.txt', mode = 'r')
#
# msg_1 = f1.readlines()
#
# passage = ""
# for m in msg_1 :
#     if word in m :  # m as 7th element
#         pos = msg_1.index(m)
#         passage =  msg_1[pos]
#
# print(passage)
# print(word in passage)
#
#
# f1.close()







### DIRECTORY """"
"""path => directory => C\Desktop|Folder"""

# directory is defined as collection of files or sub directories
# Operating System (os) helps us to perform actions on directories
# import os


# 1. Check Current Working Directory
# os.getcwd()

# import os
#
# print(currentFolder)
# currentFolder = os.getcwd()


# 2. Create a Directory
# os.mkdir('FolderName')

# import os
#
# print("Current Folder => ",  os.getcwd())
# os.mkdir('FirstFolder')


# 3. Remove the directory
# os.rmdir()

# import os
#
# print("Current folder : ", os.getcwd())
#
# os.rmdir('FirstFolder')




# 4. Changing the Directory
# os.chdir('pathName') : move into the folder
# os.chdir('..') : move out of the folder

import os

# print("Current Working Folder : ", os.getcwd())
#
# os.mkdir("FirstProject")
#
# os.chdir('FirstProject')
#
# print("Current Working Folder : ", os.getcwd())
#
# os.chdir('..')

# print("Current Working Folder : ", os.getcwd())
#
# os.rmdir('FirstProject')
#
# os.chdir('FirstProject')




# 5. Rename the Folder
# os.renmae(oldName, newName)

import os

print("Current Folder = ", os.getcwd())
os.rename('First Project', 'Python Project')


























