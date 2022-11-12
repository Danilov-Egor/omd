import json
from typing import Dict
from collections import namedtuple
import keyword


class ColorizeMixin:
    def __str__(self):
        return f"\033[1;{Advert.repr_color_code};40m"


class DotDict(dict):

    def __getattr__(self, item):
        if item in self:
            return self.get(item)
        else:
            return 0


class Advert(ColorizeMixin, DotDict):
    repr_color_code = 32

    def __init__(self, mapping):
        self.title = mapping.title
        self.price = 0
        Advert.extract_dict(self, mapping)

    def extract_dict(self, mapping):
        def extract(self, mapping):
            """Recursive func"""
            if isinstance(mapping, DotDict):
                for k, v in mapping.items():
                    if isinstance(v, DotDict):
                        extract(self, v)
                    else:
                        if keyword.iskeyword(k):
                            k += '_'
                        setattr(self, k, v)
        extract(self, mapping)

    def __setattr__(self, name, value):
        if name == 'price' and value < 0:
            raise ValueError("must be >= 0")
        self.__dict__[name] = str(value)

    def __str__(self):
        out_dict = self.__dict__.copy()
        out_dict['price'] += ' ₽'
        return super().__str__() + ' | '.join(list(map(str, out_dict.values())))


# JSON
lesson_str = """{
    "title": "python",
    "price": 1,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
}"""

lesson = json.loads(lesson_str, object_hook=DotDict)
a = Advert(lesson)
print(a)

