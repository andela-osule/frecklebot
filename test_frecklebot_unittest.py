import unittest
import frecklebot
from flask import json

class TestFrecklebot(unittest.TestCase):
    """Test Frecklebot """
    def setUp(self):
        frecklebot.app.testing = True
        self.config = frecklebot.app.config
        self.app = frecklebot.app.test_client()
        pass

    def test_subscribe(self):
        data = {'token':self.config['BOT_APP_OUTGOING_PAYLOAD_TOKEN'],\
        'user_id':'U07449TRN', 'user_name':'oluwafemi'}
        resp = self.app.post('incoming', data=data)
        data = json.loads(resp.data)
        #assertEq 'Hello World' in res
        self.assertEqual(data['Status'], "OK")
if __name__ == '__main__':
    unittest.main()