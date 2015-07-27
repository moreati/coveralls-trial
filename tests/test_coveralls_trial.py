# -*- coding: utf-8 -*-

import unittest
from coveralls_trial import coveralls_trial

class Tests(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(True, coveralls_trial.foo())

    def test_bar(self):
        self.assertEqual(False, coveralls_trial.bar())

#    def test_baz(self):
#        self.assertEqual(4, coveralls_trial.baz())
