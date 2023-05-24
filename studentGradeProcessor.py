#-----------------------------------------------------------------------------------------
# studentGradeProcessor.py
# Author: Claire Tanner
# Date: 4/5/2023

# The prupose of this program is to process the file Grades.txt line by line
# The average, maximum, and minimum will be calculated and printed
# Program will also determine whether a grade, or name of a stutdent is a valid entry 
# This program implements the Fernet Cipher.
#-----------------------------------------------------------------------------------------

import sys
import itertools
import string
from cryptography.fernet import Fernet

class Student:
    # this is the constructor for this class
    # @param first_name is the stuent's first name  
    def __init__(self, firstName, lastName, grade):
        self.firstName = firstName
        self.lastName = lastName
        self.grade = grade

    # the __repr__ method will return the correct string format
    def __repr__(self):
        return f"{self.firstName} {self.lastName}: {self.grade}"
    
    # the __lt__ method will compare two student objects based on their grades
    # @param other is the other object that will be used to compare
    def __lt__(self, other):
        return self.grade < other.grade


    # the __gt__ method will compare two student objects based on their grades
    # @param other is the other object that will be used to compare   
    def __gt__(self, other):
        return self.grade > other.grade
    
    def __add__(self, other):
        return self.grade + other.grade  
    
    def __eq__(self, other):
        return self.grade == other.grade    

class StudentGradeProcessor:
    # this is the constructor for this class
    # @param file_name is used to take in data from Grades.txt
    def __init__(self, fileName):
        self.fileName = fileName
        
        # counter to keep track of valid entries
        self.counter = 0
        
        # counter to add up the total of valid entries
        self.addSum = 0
        
        # empty list to store valid student information
        self.studentInfo = []
        
        # empty list to store valid grades
        self.gradeLst = []
        
    # this methtod will process student information to determine if the information in Grades.txt is valid
    def processGrades(self):
        # open Grades.txt
        with open(self.fileName, "r") as infile:
            for line in infile:
                # split data so first and last name, and grades are separared
                data = line.split()
                grade = float(data[-1])
                firstName = data[0]
                lastName = data[1]
                
                
                # this will check if the student's first and last name is valid (no spaces or special characters
                # this will also check if the student's grade is in range ( > 0 or < 100)                
                if not firstName.isalpha() or not lastName.isalpha() or grade < 0 or grade > 100:
                    print("Invalid name or grade")
                else:
                    # create a Student instance with valid information
                    student = Student(firstName, lastName, grade)
                    # add the Student instance to the student_info list
                    self.studentInfo.append(student)
                    # add the grade to the grade_lst list
                    self.gradeLst.append(grade)                
                    
                    # calculate the valid grades to find the sum
                    self.addSum = self.addSum + grade
                    
                    # print the results the correctly 
                    print("The grade entered for", firstName, lastName, "is", grade)
                    
                    # update the counter for valid entries
                    self.counter = self.counter + 1
                    
        # calculate the avgerage of the grades
        avgGrade = float(self.addSum) / float(self.counter) if self.counter > 0 else 0
        # find the maximum grade in gradeLst
        maximumGrade = max(self.gradeLst) if self.gradeLst else 0
        # fins the minimum grades in grade_lst
        minimumGrade = min(self.gradeLst) if self.gradeLst else 0
        
        # print the results
        print("\n")
        print("Total number of grades entered =", self.counter)
        print("The average of the grades = %0.2f" % avgGrade)
        print("The maximum of the grades = %0.2f" % maximumGrade)
        print("The minimum of the grades = %0.2f" % minimumGrade)
        print("The grades entered: ", self.gradeLst , "\n")


    # this method will write encrypted student information to the text file Assignment4.txt
    def encAndWrite(self):
        
        # generate the key
        key = Fernet.generate_key()
        
        # create an instance of the Fernet Cipher
        cipher = Fernet(key)
        
        # encrypt that data in self.student_info
        encData = cipher.encrypt(str(self.studentInfo).encode())
        
        # open the text file Assignment4.txt
        with open("Assignment4.txt", "wb") as outfile:
            # writen encrypted data to Assignment4.txt
            outfile.write(encData)
        
        # open and write the encryption key
        with open("key.key", "wb") as keyfile:
            keyfile.write(key)
            
        # send a message to the user that student inforomationw was written to Assignment4.txt    
        print("Encryption was successful", "\n")

    # this method will read the encrypted information and will decrypt it
    # results will also 
    def decAndRead(self):
        
        # open and read the encrpyted file Assignment4.txt
        with open("Assignment4.txt", "rb") as infile:
            encData = infile.read()
        
        # open and read the encryption key 
        with open("key.key", "rb") as keyfile:
            key = keyfile.read()
        
        # create an instance of the Fernet Cipher
        cipher = Fernet(key)
        
        # decrypt the data in encrypted information
        decData = cipher.decrypt(encData).decode()
        
        print("Decrypted student information:")
        for item in decData.split(", "):
            # assuming each item is a string in the format "Name: Score"
            name, score = item.split(": ")
            # process each item as needed
            print("{}: {}".format(name, score))        


if __name__ == "__main__":
    # create instance to of this class with "Grades.txt"
    gradeProcessor = StudentGradeProcessor("Grades.txt")
    
    # call this method to process student info
    gradeProcessor.processGrades()
    
    # call this method to encrypt 
    gradeProcessor.encAndWrite()
    
    # call this method to decrypt
    gradeProcessor.decAndRead()

    
            
    
        





        
   




    
    
  
        
    
    
    
    
    
    
    
  
    
    
        
    

    
        







   
    






    
    








 




                        
                        


