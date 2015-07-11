import unittest
import frecklebot

class FrecklebotTestCase(unittest.TestCase):
    """Test Frecklebot """
def setUp(self):
    self.app = frecklebot.app.test_client()

def test_subscribe(self):
    res = frecklebot.app.get('/')
    print 'res'
if __name__ == '__main__':
    unittest.main()