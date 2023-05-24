#-----------------------------------------------------------------------------------------
# testStudentGradeProcessor.py
# Author: Claire Tanner
# Date: 4/5/2023

# The prupose of this program is to test the program studentGradeProcessor.py
# The unit testing ensures that all methods pass. This program implements 
# the Student class, the StudentGradeProcessor class, and the Fernet Cipher.
#-----------------------------------------------------------------------------------------  

import unittest
import os
from studentGradeProcessor import StudentGradeProcessor
from studentGradeProcessor import Student
from cryptography.fernet import Fernet

# This class will test the Student class and the StudentGradeProcessor class.
class TestStudentGradeProcessor(unittest.TestCase):   
    
    # this will test the constructor for the Student class
    def testInit(self): 
        
        student1 = Student("Claire", "Tanner", 95)
        
        self.assertEqual(student1.firstName, "Claire")
        self.assertEqual(student1.lastName, "Tanner")
        self.assertEqual(student1.grade, 95)
        
    # this will test the __repr__ method in the Student class
    def testRepr(self):
        # Create a student object
        student = Student("Claire", "Tanner", 95)
        
        expectedRepr = "Claire Tanner: 95"
        self.assertEqual(repr(student), expectedRepr)        
    
    # this will test the __lt__ method  in the Student class
    def testLt(self):
        # create student variable to test if they are less than eachother 
        student1 = Student("Claire", "Tanner", 95)
        student2 = Student("Claire", "Elizabeth", 85)
        student3 = Student("Elizabeth", "Tanner", 90)
        
        self.assertTrue(student3 < student1)
        self.assertFalse(student1 < student2)
        self.assertFalse(student3 < student2)        
        
    # this will test the __gt__ method in the Student class
    def testGt(self):
        # create student variable to test if they are greater than each other
        student1 = Student("Claire", "Tanner", 95)
        student2 = Student("Claire", "Elizabeth", 85)
        student3 = Student("Elizabeth", "Tanner", 90)
        
        
        self.assertTrue(student1 > student2)
        self.assertFalse(student2 > student1)
        self.assertFalse(student3 > student1)
            
    # this will test the __add__ method in the Student class
    def testAdd(self):
        # create student varaible to add the grades
        student1 = Student("Claire", "Tanner", 95)
        student2 = Student("Claire", "Elizabeth", 85)
        
        expectedResult = student1 + student2
        self.assertEqual(expectedResult, 180)
        
    # this will test the __eq__ method in the Student class 
    def testEq(self):
        # create student variable to test if they are equal
        student1 = Student("Claire", "Tanner", 95)
        student2 = Student("Claire", "Elizabeth", 85)
        student3 = Student("Elizabeth", "Tanner", 90)
        
        self.assertTrue(student1 == student1)
        self.assertFalse(student1 == student2)
        self.assertFalse(student2 == student3)    
        
    
#------------------------------------------------------------------------------------
    
    # this will test the StudentGradeProcessor class
    def testStudentGradeProcessor(self):
        # create the text file test_grades.txt
        with open("test_grades.txt", "w") as testfile:
            # write student information to the test_grades.txt
            testfile.write("Claire Tanner 95\n")
            testfile.write("Claire Elizabeth 85\n")
            testfile.write("Elizabeth Tanner 90\n")
            
        # create an instance of StudentGradeProcessor with test_grades.txt
        gradeProcessor = StudentGradeProcessor("test_grades.txt")
        
        # call this method to test the data in test_grades.txt
        gradeProcessor.processGrades()
        
        # call this method to test if the program can write the encrypted data to the file
        gradeProcessor.encAndWrite()
        
        # call this method to test if program and read and decrypt the data in the file
        gradeProcessor.decAndRead()

        # remove the test file and other generated files
        os.remove("test_grades.txt")
        os.remove("Assignment4.txt")
        os.remove("key.key")

if __name__ == "__main__":
    unittest.main()









 











        
  
  


        


