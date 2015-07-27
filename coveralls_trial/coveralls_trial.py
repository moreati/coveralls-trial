# -*- coding: utf-8 -*-

import re
import sys


if sys.version_info[:3] >= (3,0,0):
    text_type = str
else:
    text_type = unicode


def foo():
    return True


class jcconv:
    HIRA = 0
    KATA = 1

    hira = [u'が ぎ ぐ げ ご ざ じ ず ぜ ぞ だ ぢ づ で ど ば び ぶ べ ぼ ぱ ぴ ぷ ぺ ぽ',
            u'あ い う え お か き く け こ さ し す せ そ た ち つ て と ' +
            u'な に ぬ ね の は ひ ふ へ ほ ま み む め も や ゆ よ ら り る れ ろ ' +
            u'わ を ん ぁ ぃ ぅ ぇ ぉ ゃ ゅ ょ っ'
            ]
    kata = [u'ガ ギ グ ゲ ゴ ザ ジ ズ ゼ ゾ ダ ヂ ヅ デ ド バ ビ ブ ベ ボ パ ピ プ ペ ポ',
            u'ア イ ウ エ オ カ キ ク ケ コ サ シ ス セ ソ タ チ ツ テ ト ' +
            u'ナ ニ ヌ ネ ノ ハ ヒ フ ヘ ホ マ ミ ム メ モ ヤ ユ ヨ ラ リ ル レ ロ ' +
            u'ワ ヲ ン ァ ィ ゥ ェ ォ ャ ュ ョ ッ'
            ]
    char_sets = [hira, kata]


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


# convert hiragana to katakana
def hira2kata(text, reserved=()):
    return convert(text, jcconv.HIRA, jcconv.KATA, reserved)
