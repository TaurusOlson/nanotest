# NANOTEST

nanotest is a simple unit testing framework for Python.


# MOTIVATION

I want a quick way of testing my code. Testing should be easy and fun. It
shouldn't get in your way.  Actually I think it should almost be as natural as
coding your main project.
There are many frameworks so why write another one?

Here are a few reasons:

* unittest is great but I find it long to setup. Most of the time, its rigidity
  frustrates me and I end up skipping the testing phase!

* nosetests is great and flexible but I need something else. A different kind
  of flexibility I guess.

* I was tempted to use `assert` sometimes as it is really fast to setup
  but the code stops the first time the assertion is not satisfied and that's definitely
  an unacceptable solution.


# USAGE

    from nanotest import test

## Test (in)equality

    test(42).eq(40 + 2)
    # 42 should be equal to 42... OK

    test(42).ne(40 + 2)
    # 42 should not be equal to 42... NOK


## Test superiority

    test(42).gt(41)
    # 42 should be greater than 41... OK

    test(42).ge(41)
    # 42 should be greater or equal to 41... OK


## Test inferiority

    test(42).lt(43)
    # 42 should be lower than 43... OK

    test(42).le(43)
    # 42 should be lower or equal to 43... OK


## Logical tests 

    test(True).is_(True)
    # True should be True... OK

    test(True).is_not(True)
    # True should not be True... NOK


## Test inclusion

    test("Spam, spam, spam and egg").contains("spam")
    # 'Spam, spam, spam and egg' should contain 'spam'... OK

    test("Spam, spam, spam and egg").contains_no("bacon")
    # 'Spam, spam, spam and egg' should not contain 'bacon'... OK


# THE NAME

I wanted a tiny testing framework. I like physics so nano sounds good. Hence nanotest ;)


