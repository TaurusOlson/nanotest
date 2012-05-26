#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

import nanotest
from nose.tools import *


def test_eq():
    nanotest.test(42).eq(42) == True

def test_ne():
    nanotest.test(42).ne(4) == True

def test_gt():
    nanotest.test(42).gt(41) == True

def test_ge():
    nanotest.test(42).ge(42) == True
    nanotest.test(42).ge(41) == True

def test_lt():
    nanotest.test(42).lt(43) == True

def test_le():
    nanotest.test(42).le(43) == True
    nanotest.test(42).le(42) == True

def test_is_():
    nanotest.test(True).is_(True) == True
    nanotest.test(False).is_(False) == True
    nanotest.test(None).is_(None) == True

def test_is_not():
    nanotest.test(True).is_not(False) == True
    nanotest.test(False).is_not(True) == True
    nanotest.test(None).is_not('something') == True

def test_contains():
    nanotest.test([2, 3, 5, 7, 11]).contains(5)
    nanotest.test("nanotest").contains("test")

def test_contains_no():
    nanotest.test([2, 3, 5, 7, 11]).contains_no(1)
    nanotest.test("nanotest").contains_no("complicated")

