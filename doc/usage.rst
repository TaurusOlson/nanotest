Usage
=====

::
    from nanotest import test

* Test (in)equality::

    test(42).eq(40 + 2)
    # Output: 42 should be equal to 42... OK

    test(42).ne(40 + 2)
    # Output: 42 should not be equal to 42... NOK


* Test superiority::

    test(42).gt(41)
    # Output: 42 should be greater than 41... OK

    test(42).ge(41)
    # Output: 42 should be greater or equal to 41... OK


* Test inferiority::

    test(42).lt(43)
    # Output: 42 should be lower than 43... OK

    test(42).le(43)
    # Output: 42 should be lower or equal to 43... OK


* Logical tests::

    test(True).is_(True)
    # Output: True should be True... OK

    test(True).is_not(True)
    # Output: True should not be True... NOK


* Test inclusion::

    test("Spam, spam, spam and egg").contains("spam")
    # Output: 'Spam, spam, spam and egg' should contain 'spam'... OK

    test("Spam, spam, spam and egg").contains_no("bacon")
    # Output: 'Spam, spam, spam and egg' should not contain 'bacon'... OK



