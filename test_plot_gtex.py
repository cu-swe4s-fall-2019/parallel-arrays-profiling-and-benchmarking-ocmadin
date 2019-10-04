import unittest
import plot_gtex as pgtx

class TestLinearSearch(unittest.TestCase):
    def test_input_type_key(self):
        self.assertRaises(TypeError, pgtx.linear_search,None,[1,2,3])
        self.assertRaises(TypeError,pgtx.linear_search,[1,2,3],[1,2,3])

    def test_input_type_L(self):
        self.assertRaises(TypeError, pgtx.linear_search,1,None)
        self.assertRaises(TypeError,pgtx.linear_search,1,1)
        self.assertRaises(TypeError,pgtx.linear_search,1,'test')
    def test_no_hit(self):
        self.assertEqual(pgtx.linear_search('aa',[1,2,3]),-1)
    def test_hit(self):
        self.assertEqual(pgtx.linear_search(1,[1,2,3]),0)        

class TestInputParsing(unittest.TestCase):
    def test_argparse(self):
        self.assertIsNotNone(pgtx.parse_arguments())        