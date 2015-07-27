# -*- coding: utf-8 -*-

__all__ = ['hira2kata', 'kata2hira', 'half2hira', 'hira2half', 'kata2half',
           'half2kata', 'half2wide', 'wide2half', 'convert',
           'check_hira', 'check_kata', 'check_half']

import re
import sys

if sys.version_info[:2] >= (3, 0):
    text_type = str
else:
    text_type = unicode

# convert hiragana to katakana
def hira2kata(text, reserved=()):
    return convert(text, jcconv.HIRA, jcconv.KATA, reserved)

# convert katakana to hiragana
def kata2hira(text, reserved=()):
    return convert(text, jcconv.KATA, jcconv.HIRA, reserved)

# convert half-width kana to hiragana
def half2hira(text, reserved=()):
    return convert(text, jcconv.HALF, jcconv.HIRA, reserved)

# convert hiragana to half-width kana
def hira2half(text, reserved=()):
    return convert(text, jcconv.HIRA, jcconv.HALF, reserved)

# convert katakana to half-width kana
def kata2half(text, reserved=()):
    return convert(text, jcconv.KATA, jcconv.HALF, reserved)

# convert half-width kana to katakana
def half2kata(text, reserved=()):
    return convert(text, jcconv.HALF, jcconv.KATA, reserved)

# expand half width number and alphabet to wide width
def half2wide(text, reserved=()):
    text = convert(text, jcconv.HNUM, jcconv.WNUM, reserved)
    text = convert(text, jcconv.HALP, jcconv.WALP, reserved)
    return convert(text, jcconv.HSYM, jcconv.WSYM, reserved)

# shrink wide width number and alphabet to half width
def wide2half(text, reserved=()):
    text = convert(text, jcconv.WNUM, jcconv.HNUM, reserved)
    text = convert(text, jcconv.WALP, jcconv.HALP, reserved)
    return convert(text, jcconv.WSYM, jcconv.HSYM, reserved)

# check if 'text' consists of hiragana
def check_hira(text):
    return check(text, jcconv.HIRA)

# check if 'text' consists of katakana
def check_kata(text):
    return check(text, jcconv.KATA)

# check if 'text' consists of half-width kana
def check_half(text):
    return check(text, jcconv.HALF)

# convert 'frm' charset to 'to' charset
# input text must be unicode or str(utf-8)
# 'frm' and 'to' can be specified with (HIRA, KATA, HALF, WNUM, HNUM, WALP, HALP, WSYM, HSYM)
__regex_storage = {}
def convert(text, frm, to, reserved=()):
    def _multiple_replace(text, dic):
        key = '|'.join(map(re.escape, dic))
        if key in __regex_storage:
            rx = __regex_storage[key]
        else:
            rx = re.compile(key)
            __regex_storage[key] = rx
        def proc_one(match):
            return dic[match.group(0)]
        return rx.sub(proc_one, text)

    uflag = isinstance(text, text_type)
    f_set = jcconv.char_sets[frm]
    t_set = jcconv.char_sets[to]

    text = uflag and text or text.decode('utf-8')
    if len(f_set[0].split(' ')) == len(t_set[0].split(' ')):
        for i in range(len(f_set)):
            conv_table = dict(zip(f_set[i].split(' '), t_set[i].split(' ')))
            for r in reserved:
                try:
                    del(conv_table[r])
                except KeyError:
                    pass
            text = _multiple_replace(text, conv_table)
        return uflag and text or text.encode('utf-8')
    else:
        raise ValueError("Invalid Parameter")

def check(text, char_set_type):
    uflag = isinstance(text, text_type)
    text = uflag and text or text.decode('utf-8')
    char_set = []
    for cset in jcconv.char_sets[char_set_type]:
        char_set.extend(cset.split(' '))
    return all([text_char in char_set for text_char in text])

