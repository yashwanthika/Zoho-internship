import unittest
from addition import add

class Testing_add(unittest.TestCase):
    def test_list(self):
        data = [1,2,3,4,5]
        result = add(data)
        self.assertEqual(result,15)

if __name__=="__main__":
    unittest.main()
