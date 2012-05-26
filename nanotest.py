#!/usr/bin/env python


class Nanotest(object):
    """This class allows to create a test for the value to be tested.
    
    :Usage:

        test = Nanotest(x)

        test.eq(y)
    
    """
    truth_table = {True: 'OK', False: 'NOK'}

    def __init__(self, arg=None):
        self.arg = arg

    def initialize(self, arg):
        self.arg = arg
        self.total += 1
        return Nanotest(self.arg)

    def comparison(self, other, relation):
        """This function applies the necessary comparison relations"""
        if isinstance(self.arg, int):
            result = getattr(float(self.arg), relation)(other)
        else:
            result = getattr(self.arg, relation)(other)
        return result

    def eq(self, other):
        """Test that both values are equal """
        result = self.comparison(other, '__eq__')
        print "be equal to %r... %s" % (other, self.truth_table[result])

    def ne(self, other):
        """Test that the current value is not equal to the given one."""
        result = self.comparison(other, '__ne__')
        print "not be equal to %r... %s" % (other, self.truth_table[result])

    def gt(self, other):
        """Test that the current value is greater than the given one."""
        result = self.comparison(other, '__gt__')
        print "be greater than %r... %s" % (other, self.truth_table[result])

    def ge(self, other):
        """Test that the current value is greater or equal to the given one."""
        result = self.comparison(other, '__ge__')
        print "be greater or equal to %r... %s" % (other, self.truth_table[result])

    def lt(self, other):
        """Test that the current value is lower than the given one."""
        result = self.comparison(other, '__lt__')
        print "be lower than %r... %s" % (other, self.truth_table[result])

    def le(self, other):
        """Test that the current value is lower or equal to the given one."""
        result = self.comparison(other, '__le__')
        print "be lower or equal to %r... %s" % (other, self.truth_table[result])

    def is_(self, other):
        """Test that the current value corresponds to the given one."""
        result = self.arg is other
        print "be %r... %s" % (other, self.truth_table[result])

    def is_not(self, other):
        """Test that the current value does not correspond to the given one."""
        result = self.arg is not other
        print "not be %r... %s" % (other, self.truth_table[result])

    def contains(self, other):
        """Test that the current value contains the given one."""
        result = other in self.arg 
        print "contain %r... %s" % (other, self.truth_table[result])

    def contains_no(self, other):
        """Test that the current value does not contain the given one."""
        result = other not in self.arg
        print "not contain %r... %s" % (other, self.truth_table[result])


def test(a):
    print "%r should" % a,
    return Nanotest(a)


