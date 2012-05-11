#!/usr/bin/env python


class Nanotest(object):
    truth_table = {True: 'OK', False: 'NOK'}

    def __init__(self, arg=None):
        self.arg = arg

    def initialize(self, arg):
        self.arg = arg
        self.total += 1
        return Nanotest(self.arg)

    def comparison(self, other, relation):
        if isinstance(self.arg, int):
            result = getattr(float(self.arg), relation)(other)
        else:
            result = getattr(self.arg, relation)(other)
        return result

    def eq(self, other):
        result = self.comparison(other, '__eq__')
        print "be equal to %r... %s" % (other, self.truth_table[result])

    def ne(self, other):
        result = self.comparison(other, '__ne__')
        print "not be equal to %r... %s" % (other, self.truth_table[result])

    def gt(self, other):
        result = self.comparison(other, '__gt__')
        print "be greater than %r... %s" % (other, self.truth_table[result])

    def ge(self, other):
        result = self.comparison(other, '__ge__')
        print "be greater or equal to %r... %s" % (other, self.truth_table[result])

    def lt(self, other):
        result = self.comparison(other, '__lt__')
        print "be lower than %r... %s" % (other, self.truth_table[result])

    def le(self, other):
        result = self.comparison(other, '__le__')
        print "be lower or equal to %r... %s" % (other, self.truth_table[result])

    def is_(self, other):
        result = self.arg is other
        print "be %r... %s" % (other, self.truth_table[result])

    def is_not(self, other):
        result = self.arg is not other
        print "not be %r... %s" % (other, self.truth_table[result])

    def contains(self, other):
        result = other in self.arg 
        print "contain %r... %s" % (other, self.truth_table[result])

    def contains_no(self, other):
        result = other not in self.arg
        print "not contain %r... %s" % (other, self.truth_table[result])


def test(a):
    print "%r should" % a,
    return Nanotest(a)


