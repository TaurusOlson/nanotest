#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.abspath("."))

from nanotest import test


# Test eq():
test(42).eq(42)

# Test ne():
test(42).ne(4)

# Test gt():
test(42).gt(41)

# Test ge():
test(42).ge(42)
test(42).ge(41)

# Test lt():
test(42).lt(43)

# Test le():
test(42).le(43)
test(42).le(42) 

# Test is_():
test(True).is_(True) 
test(False).is_(False) 
test(None).is_(None) 

# Test is_not():
test(True).is_not(False) 
test(False).is_not(True) 
test(None).is_not('something') 

# Test contains():
test([2, 3, 5, 7, 11]).contains(5)
test("nanotest").contains("test")

# Test contains_no():
test([2, 3, 5, 7, 11]).contains_no(1)
test("nanotest").contains_no("complicated")

