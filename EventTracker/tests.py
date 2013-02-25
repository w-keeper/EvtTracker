'''
Created on Feb 22, 2013

@author: alekseynikiforov
'''

import unittest
from evt_manager import EventManager

class TestCase(unittest.TestCase):
    
    def test_wrong_id(self):
        """
        Should return None if id has wrong format
        """
        event = EventManager().get_event_by_id(123)
        self.assertEqual(event, None, "OK")
            
if __name__ == '__main__':
    unittest.main() 
