# -*- coding: utf-8 -*-

import pyemoji


class TestStatusCodeCommands(object):

    def test_encode(self):
        assert pyemoji.encode(u'笑脸表情：😄') == '\u7b11\u8138\u8868\u60c5\uff1a\U0001f604'

    def test_decode(self):
        assert pyemoji.decode('\\u7b11\\u8138\\u8868\\u60c5\\uff1a\\U0001f604') == u'笑脸表情：😄'
        assert pyemoji.decode(b'\\u7b11\\u8138\\u8868\\u60c5\\uff1a\\U0001f604') == u'笑脸表情：😄'

    def test_replace(self):
        assert pyemoji.replace(u'笑脸表情：😄') == u'笑脸表情：�'
        assert pyemoji.replace(u'笑脸表情：😄', '') == u'笑脸表情：'

    def test_entities(self):
        assert pyemoji.entities(u'笑脸表情：😄') == u'笑脸表情：&#128516;'

    def test_joiner(self):
        assert pyemoji.joiner(u'\U0001F468', u'\U0001F469', u'\U0001F467') == u'\U0001f468\u200d\U0001f469\u200d\U0001f467'
