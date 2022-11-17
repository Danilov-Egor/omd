from one_hot_encoder import fit_transform
import pytest


@pytest.mark.parametrize(
    "arg1, result",
    [
        (['Moscow', 'New York', 'Moscow', 'London'], 
            [
                ('Moscow', [0, 0, 1]),
                ('New York', [0, 1, 0]),
                ('Moscow', [0, 0, 1]),
                ('London', [1, 0, 0]),
            ]),
        
        (['red', 'red', 'green'], [
                                    ('red', [0, 1]),
                                    ('red', [0, 1]),
                                    ('green', [1, 0]),
                                    ]),
    ],
)

def test_one_hot_encode_eql(arg1, result):
    assert fit_transform(arg1) == result


@pytest.mark.parametrize(
    "arg2, sub_in",
    [
        (['popcorn', 'hotdog', 'burger', 'fries', 'soda', 'popcorn', 'fries'], 
            ('burger', [0, 0, 1, 0, 0])),

        (['chick'], 
            ('chick', [1])),
    ],
)

def test_one_hot_encode_in(arg2, sub_in):
    assert sub_in in fit_transform(arg2)