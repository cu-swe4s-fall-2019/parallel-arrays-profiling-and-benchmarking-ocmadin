import unittest
import math_lib as ml
import random
import statistics

class TestListMean(unittest.TestCase):
    def test_list_mean_no_input(self):
        # test if no input is passed to the function
        self.assertRaises(TypeError, ml.list_mean, None)
    
    def test_list_mean_type(self):
        # test if the input is the wrong type
        self.assertRaises(TypeError, ml.list_mean, 1)
        self.assertRaises(TypeError, ml.list_mean,1.05)
        self.assertRaises(TypeError, ml.list_mean,{})
        self.assertRaises(TypeError, ml.list_mean,True)
        self.assertRaises(TypeError, ml.list_mean,'Text')
        
    def test_list_mean_empty(self):
        # test if the list is empty
        self.assertRaises(IndexError,ml.list_mean,[])
        
    def test_list_mean_invalid_types(self):
        # test if there are invalid types in the list
        self.assertRaises(TypeError, ml.list_mean,['text','text'])
        self.assertRaises(TypeError, ml.list_mean,[[1,2],[1,2]])
        
    def test_list_mean_basic(self):
        # test a basic integer mean
        input_list=[1,2,3]
        self.assertEqual(ml.list_mean(input_list),2)

    def test_list_mean_random(self):
        # test a list of random numbers of random length
        for i in range(100):
            input_list_length = random.randint(1,1000)
            input_list = []
            list_sum = 0
            for i in range(input_list_length):
                element = random.random()
                input_list.append(element)
                list_sum += element
            self.assertEqual(ml.list_mean(input_list),list_sum/input_list_length)
            
class TestListStdev(unittest.TestCase):
    def test_list_stdev_no_input(self):
         # test if no input is passed to the function
        self.assertRaises(TypeError, ml.list_stdev, None)
        
    def test_list_stdev_type(self):
        # test if the input is the wrong type
        self.assertRaises(TypeError, ml.list_stdev, 1)
        self.assertRaises(TypeError, ml.list_stdev,1.05)
        self.assertRaises(TypeError, ml.list_stdev,{})
        self.assertRaises(TypeError, ml.list_stdev,True)
        self.assertRaises(TypeError, ml.list_stdev,'Text')
        
    def test_list_stdev_empty(self):
        # test if the list is empty
        self.assertRaises(IndexError,ml.list_stdev,[])
        
    def test_list_stdev_invalid_types(self):
        # test if there are invalid types in the list
        self.assertRaises(TypeError, ml.list_stdev,['text','text'])
        self.assertRaises(TypeError, ml.list_stdev,[[1,2],[1,2]])
        
    def test_list_stdev_basic(self):
        # test a basic integer stdev
        input_list=[1,2,3]        
        self.assertEqual(ml.list_stdev(input_list),statistics.pstdev(input_list))
        
    def test_list_stdev_random(self):
        # test a list of random numbers of random length
        for i in range(100):
            input_list_length = random.randint(1,1000)
            input_list = []
            for i in range(input_list_length):
                element = random.random()
                input_list.append(element)
            self.assertAlmostEqual(ml.list_stdev(input_list),statistics.pstdev(input_list),places=1)
    
    
        