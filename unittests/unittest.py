#!/usr/bin/env python
import unittest
import main

class BasicMathematicsTest(unittest.TestCase):

    def test_returnString(self):
        Expected_Test_Result = 'Hello World'
        Actual_Test_Result = main.printHelloWorld()
        self.assertEqual(Expected_Test_Result,Actual_Test_Result)
        print "Return String Test Completed"

    def test_BasicAdditionCheck(self):
        Expected_Test_Result = 15
        Actual_Test_Result = main.performBasicAddition(6,9)
        self.assertEqual(Expected_Test_Result,Actual_Test_Result)
        print "Basic Addtion Check Completed"

    def test_BasicSubtractionCheck(self):
        Expected_Test_Result = 5
        Actual_Test_Result = main.performBasicSubtraction(15,20)
        self.assertEqual(Expected_Test_Result,Actual_Test_Result)
        print "Basic Subtraction Check Completed"

    def test_BasicMultiplicationCheck(self):
        Expected_Test_Result = 14
        Actual_Test_Result = main.performBasicMultiplication(7,2)
        self.assertEqual(Expected_Test_Result,Actual_Test_Result)
        print "Basic Multiplication Check Completed"

    def test_DigitalBooleanCheck(self):
        Expected_Test_Result = True
        Actual_Test_Result = main.DigitalBooleanCheck('10')
        self.assertEqual(Expected_Test_Result,Actual_Test_Result)
        print "Basic Boolean Check Completed"

if __name__ == '__main__':
    unittest.main()

