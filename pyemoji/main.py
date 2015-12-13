# -*- coding: utf-8 -*-

"""
Copyright (c) 2015 HQM <qiminis0801@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import re


# Refer: http://stackoverflow.com/questions/26568722/remove-unicode-emoji-using-re-in-python
# Refer: http://stackoverflow.com/questions/22706522/python-remove-ios-emoji-characters-in-a-unicode-str-to-avoid-databaseerror-in
try:
    # Wide UCS-4 build
    highpoints = re.compile(u'[\U00010000-\U0010ffff]')
except re.error:
    # Narrow UCS-2 build
    highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')

from .compat import str


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

    def replace(self, emoji, placeholder=u'\uFFFD', unic=None):
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


# For backwards compatibility
_global_instance = PyEmoji()
encode = _global_instance.encode
decode = _global_instance.decode
replace = _global_instance.replace
entities = _global_instance.entities
