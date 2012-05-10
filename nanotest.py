#!/usr/bin/env python



class Nanotest(object):
    def __init__(self, arg):
        self.arg = arg

    def comparison(self, other, relation):
        if isinstance(self.arg, int):
            result = getattr(float(self.arg), relation)(other)
        else:
            result = getattr(self.arg, relation)(other)
        return result

    def __eq__(self, other):
        return self.comparison(other, '__eq__')

    def eq(self, other):
        print "be equal to %r..." % other
        return self.comparison(other, '__eq__')

    def ne(self, other):
        print "not be equal to %r..." % other
        return self.comparison(other, '__ne__')

    def gt(self, other):
        print "be greater than %r..." % other
        return self.comparison(other, '__gt__')

    def ge(self, other):
        print "be greater or equal to %r..." % other
        return self.comparison(other, '__ge__')

    def lt(self, other):
        print "be lower than %r..." % other
        return self.comparison(other, '__lt__')

    def le(self, other):
        print "be lower or equal to %r..." % other
        return self.comparison(other, '__le__')

    def is_(self, other):
        print "be %r" % other
        return self.arg is other

    def is_not(self, other):
        print "not be %r..." % other
        return self.arg is not other

    def contains(self, other):
        print "contain %r..." % other
        return other in self.arg 

    def contains_no(self, other):
        print "not contain %r..." % other
        return other not in self.arg

def test(a):
    print "%r should" % a,
    return Nanotest(a)


