#-----------------------------------------------------------------------------------------
# calculatingGrades3.py
# Author: Claire Tanner
# Date: 3/6/2023

# The prupose of this program is to process the file Grades.txt line by line
# The average, maximum, and minimum will be calculated and printed
# Program will also determine whether a grade, or name of a stutdent is a valid entry 
#-----------------------------------------------------------------------------------------

# imports
import sys
import itertools
import string

def main():
    # counter to keep track of valid entries
    counter = 0
    # counter to add up the total of valid entries
    addSum = 0
     
    # empty list to store valid student information
    studentInfo = []
    
    # empty list to store valid grades
    gradeLst = []

    
    # open Grades.txt
    with open("Grades.txt", "r") as infile:
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
                # add valid information to corresponding lists
                studentInfo.append(firstName)
                studentInfo.append(lastName)
                gradeLst.append(grade)
                # calculate the valid grades to find the sum
                addSum = addSum + grade
                validStudentInfo = print("The grade entered for", firstName, lastName, "is" ,  grade)
                # update counter
                counter = counter + 1  
                
                
        # calculate the average of the valid grades
        avgGrade = float(addSum) / float(counter)
        # find the maximum
        maximumGrade = max(gradeLst)
        # find the minimum
        minimumGrade = min(gradeLst)
        
           
        # print the results
        print("\n")
        print("Total number of grades entered = " , counter)
        print("The average of the grades = %0.2f" %avgGrade)
        print("The maximum of the grades = %0.2f" %maximumGrade)
        print("The minimum of the grades = %0.2f" %minimumGrade)
        print("The grdaes entered: " , gradeLst)        
            
        # close Grades.txt
        infile.close()
        
main()
    