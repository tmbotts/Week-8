import os

#user inputs directory name and file name
directoryPath = input("Please enter name of directory: ")
fileName = input("Enter file name: ")

#checks to see if the directory exists
#if not, it will create it
if not os.path.isdir(directoryPath):
    os.makedirs(directoryPath)

#complete path name and file type
completeName = os.path.join(directoryPath, fileName + ".txt")

#used 'a' so that new data will be added to the end of the file and not erased
file1 = open(completeName, 'a')

#prompts user for their name, address, and phone number
name = input("Enter your name: ")
address = input("Enter your address: ")
phoneNum = input("Enter your phone number: ")

#writes name, address, and phone number to file
file1.write(name+', '+address+', '+phoneNum+'\n')

#closes file
file1.close()

#reads the created file and prints contents
file1 = open(completeName, 'r')
print("File created: \n", file1.read())
file1.close()