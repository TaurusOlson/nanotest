# NANOTEST

nanotest is a simple unittest framework for Python.


# MOTIVATION

I want a quick way for testing my code. Testing should be easy and fun. It
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


# API

## Test (in)equality

    should_be(42).eq(40 + 2)
    should_not_be(42).eq(40 + 3)
    should_be(42).ne(40 + 2)
    should_not_be(42).ne(40 + 3)


## Test superiority

    should_be(42).gt(41)
    should_not_be(42).gt(43)
    should_be(42).ge(41)
    should_not_be(42).ge(43)


## Test inferiority

    should_be(42).lt(43)
    should_not_be(42).lt(41)
    should_be(42).le(43)
    should_not_be(42).le(41)


# THE NAME

I wanted a tiny testing framework. I like physics so nano sounds good. Hence nanotest ;)

