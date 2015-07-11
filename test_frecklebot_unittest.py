import unittest
import frecklebot
from flask import json

class TestFrecklebot(unittest.TestCase):
    """Test Frecklebot """
    def setUp(self):
        self.app = frecklebot.app.test_client()
        pass

    def test_subscribe(self):
        resp = self.app.get('/')
        data = json.loads(resp.data)
        #assertEq 'Hello World' in res
        self.assertEqual(data['message'], "Hello World")
if __name__ == '__main__':
    unittest.main()