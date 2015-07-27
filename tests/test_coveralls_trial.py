# -*- coding: utf-8 -*-

import unittest
from coveralls_trial.coveralls_trial import *

class Tests(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(True, foo())

    def test_bar(self):
        self.assertEqual(False, bar())

    def test_baz(self):
        self.assertEqual(4, baz())
