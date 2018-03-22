# author: Rakk4403(rakk4403@gmail.com)
from pprint import pprint


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


# python 2
class TimeFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimeFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class GoodWay(TimeFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


# checking init function calling order
pprint(GoodWay.mro())


# python 3
class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)


assert Explicit(10).value == Implicit(10).value
