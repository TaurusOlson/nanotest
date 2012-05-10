#!/usr/bin/env python



class Nanotest(object):
    """docstring for Nanotest"""

    def __init__(self, arg, is_true=True):
        self.arg = arg
        self.is_true = is_true

    def comparison(self, other, relation):
        if isinstance(self.arg, int):
            result = getattr(float(self.arg), relation)(other)
        else:
            result = getattr(self.arg, relation)(other)

        if self.is_true:
            return result
        else:
            return not result

    def __eq__(self, other):
        return self.comparison(other, '__eq__')

    def eq(self, other):
        return self.comparison(other, '__eq__')

    def ne(self, other):
        return self.comparison(other, '__ne__')

    def gt(self, other):
        return self.comparison(other, '__gt__')

    def ge(self, other):
        return self.comparison(other, '__ge__')

    def lt(self, other):
        return self.comparison(other, '__lt__')

    def le(self, other):
        return self.comparison(other, '__le__')


def should_be(a):
    return Nanotest(a, True)

def should_not_be(a):
    return Nanotest(a, False)



       
