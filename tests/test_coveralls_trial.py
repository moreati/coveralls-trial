#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_coveralls_trial
----------------------------------

Tests for `coveralls_trial` module.
"""

import unittest

from coveralls_trial import coveralls_trial


class TestCoverallsTrial(unittest.TestCase):
    def setUp(self):
        pass

    def test_foo(self):
        self.assertEqual(coveralls_trial.foo(), u'ƒőő')

    def test_bar(self):
        self.assertFalse(coveralls_trial.bar())


if __name__ == '__main__':
    unittest.main()
