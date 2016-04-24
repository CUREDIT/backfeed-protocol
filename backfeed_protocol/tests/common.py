import unittest
from backfeed_protocol import utils


class TestCase(unittest.TestCase):
    """Base class for all tests"""

    def setUp(self):
        # set up the database
        utils.setup_database()

    def tearDown(self):
        utils.reset_database()
