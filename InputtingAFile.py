''' Check working Directory '''
import os
print(os.getcwd())

''' Use relative or absolute path '''
readdata = open('readdata.txt', 'r')
readdata = open('C:/Users/poets/github/DevOps/readdata.txt')

''' Opens the file, appends the fourth line, and closes the file '''
with open("readdata.txt", "a+") as data:
    print(type(data))
    data.write('\nFourth line added by Python')

''' Print file without creating variable '''
with open("readdata.txt", "r") as data:
    print(data.read())

''' Print file after creating variable '''
print(readdata.read())
