import unittest
from unittest.mock import patch

from what_is_year_now import what_is_year_now


class TestWhatYear(unittest.TestCase):
    
    @patch('what_is_year_now.urllib.request.urlopen')
    def test_what_year1(self, mock_what_year):
        mock_what_year.return_value = open('file1.txt', 'r')
        self.assertEqual(what_is_year_now(), 2019)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_what_year2(self, mock_what_year):
        mock_what_year.return_value = open('file2.txt', 'r')
        self.assertEqual(what_is_year_now(), 2021)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_what_year3(self, mock_what_year):
        mock_what_year.return_value = open('file3.txt', 'r')
        self.assertEqual(what_is_year_now(), 2015)

    @patch('what_is_year_now.urllib.request.urlopen')
    def test_what_year4(self, mock_what_year):
        mock_what_year.return_value = open('file4.txt', 'r')
        self.assertRaises(ValueError, what_is_year_now)

if __name__ == 'main':
    unittest.what_is_year_now()
