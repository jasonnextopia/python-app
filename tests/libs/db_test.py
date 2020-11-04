import unittest
import os
from app.libs.db import get_db_engine, get_conn_str

class TestDB(unittest.TestCase):
    def test_get_conn_str(self):
        self.assertIsNot(get_conn_str(), None)

if __name__ == '__main__':
    unittest.main()