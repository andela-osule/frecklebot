import unittest
import frecklebot

class FrecklebotTestCase(unittest.TestCase):
    """Test Frecklebot """
def setUp(self):
    pass

def test_subscribe(self):
    res = frecklebot.app.get('/')
    self.assertEqual(res, 'Helvflo World')

if __name__ == '__main__':
    unittest.main()