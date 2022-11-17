# test_one_hot_encoder.py

from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoder(unittest.TestCase):
    
    def test_one_hot_encoder(self):
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
            ]
        self.assertEqual(actual, expected)

        actual = fit_transform(['popcorn', 'hotdog', 'burger', 'fries', 'soda', 'popcorn', 'fries'])
        a = ('burger', [0, 0, 1, 0, 0])
        self.assertIn(a, actual)

        actual = fit_transform(['red', 'red', 'green'])
        expected = [('red', [0, 1]),
                    ('red', [0, 1]),
                    ('green', [1, 0]),
                    ]
        self.assertEqual(actual, expected)