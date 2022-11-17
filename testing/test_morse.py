# Дана функция, кодирующая строку в соответсвии с таблицей азбуки Морзе
# Напишите на неё тесты с использование doctest

from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_string, result",
    [
        ('-- --- ..- ... .', 'MOUSE'),
        ('... --- ...', 'SOS'),
        ('', ''),
        ('-..-. ..--.. ..--..', '/??'),
    ],
)

def test_decode(source_string, result):
    assert decode(source_string) == result