# -*- coding: utf-8 -*-

def foo():
    return True

# convert hiragana to katakana
def hira2kata(text, reserved=()):
    return convert(text, jcconv.HIRA, jcconv.KATA, reserved)
