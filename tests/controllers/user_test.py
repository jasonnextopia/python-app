import unittest
import os
from app.controllers.user import add_user, get_user
from app.libs.db import get_db_engine

class TestUserController(unittest.TestCase):
    def test_add_user(self):
        data = {
            "user_name": 'admin',
            "password": "xxx"
        }
        res = add_user(data)
        self.assertNotEqual(res, 0)
        self.assertGreater(res, 0)
    

if __name__ == '__main__':
    unittest.main()