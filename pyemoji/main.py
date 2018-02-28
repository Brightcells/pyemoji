# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import re

from .compat import str


# Refer: http://stackoverflow.com/questions/26568722/remove-unicode-emoji-using-re-in-python
# Refer: http://stackoverflow.com/questions/22706522/python-remove-ios-emoji-characters-in-a-unicode-str-to-avoid-databaseerror-in
# Refer: https://stackoverflow.com/questions/13729638/how-can-i-filter-emoji-characters-from-my-input-so-i-can-save-in-mysql-5-5
try:
    # Wide UCS-4 build
    highpoints = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
except re.error:
    # Narrow UCS-2 build
    highpoints = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')


class PyEmoji(object):
    def unic_func(self, text, unic):
        if unic:
            return unic(text)
        if isinstance(text, str):
            return text
        return text.decode('utf8')

    def repl_func(self, matched):
        #: .decode('utf8') for Python 3.x compatibility
        hex_num = '0x{0}'.format(matched.group().encode('unicode_escape').decode('utf8').lstrip('\\').lstrip('U').lstrip('0'))
        decimal_num = int(hex_num, 16)
        return '&#{0};'.format(decimal_num)

    def encode(self, emoji, unic=None):
        """
        Encode Emoji with unicode_escape
        Refer: http://stackoverflow.com/questions/2108824/mysql-incorrect-string-value-error-when-save-unicode-string-in-django
        :param emoji:
        :param unic:
        :return:
        """
        return self.unic_func(emoji, unic).encode('unicode_escape')

    def decode(self, text):
        """
        Decode Emoji with unicode_escape
        Refer: http://stackoverflow.com/questions/2108824/mysql-incorrect-string-value-error-when-save-unicode-string-in-django
        :param text:
        :return:
        """
        try:
            return text.decode('unicode_escape')
        except UnicodeEncodeError:
            return text
        except AttributeError:  #: Python 3.x
            return text.encode('utf8').decode('unicode_escape')

    def replace(self, emoji, placeholder='\uFFFD', unic=None):
        """
        Replace Emoji as Placeholder which default is u'\uFFFD' display as �
        Remove All Emojis by Setting Placeholder as ''
        Refer: http://stackoverflow.com/questions/3220031/how-to-filter-or-replace-unicode-characters-that-would-take-more-than-3-bytes
        :param emoji:
        :param placeholder:
        :param unic:
        :return:
        """
        return highpoints.sub(placeholder, self.unic_func(emoji, unic=unic))

    def entities(self, emoji, unic=None):
        """
        Replace Emoji as Entities such as &#128516; Which Can Directly Display in HTML
        Refer: http://www.bubuko.com/infodetail-1022211.html
        :param emoji:
        :param unic:
        :return:
        """
        return highpoints.sub(self.repl_func, self.unic_func(emoji, unic=unic))

    def joiner(self, *mojis):
        """
        ZERO WIDTH JOINER ``mojis``.
        """
        return '\u200D'.join(mojis)


_global_instance = PyEmoji()
encode = _global_instance.encode
decode = _global_instance.decode
replace = _global_instance.replace
entities = _global_instance.entities
joiner = _global_instance.joiner
