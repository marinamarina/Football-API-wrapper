#! usr/bin/python

import unittest
from football_api_wrapper import FootballAPIWrapper

class TestFootballAPIWrapper(unittest.TestCase):
    def setUp(self):
        self.faw = FootballAPIWrapper()
        self.faw.api_key = ''
        self.data_dir = '/data/'

    @unittest.skip("To do")
    def test_get_beginning_year(self):
        pass

    def test_unplayed_matches_tuple(self):
        from datetime import datetime
        matches = self.faw.unplayed_matches
        for m in matches:
            self.assertTrue(datetime.strptime(m.date, "%d.%m.%Y").date() >= datetime.now().date(),
                            "All the matches dates should be IN THE FUTURE compared to today")

    def test_played_matches_tuple(self):
        from datetime import datetime
        matches = self.faw.played_matches
        for m in matches:
            self.assertTrue(datetime.strptime(m.date, "%d.%m.%Y").date() <= datetime.now().date(),
                            "All the matches dates should be IN THE PAST compared to today")


