========
pyemoji
========

When MySQL version greater than 5.5.3 have utf8mb4 CHARACTER SET which can store emoji.

But when MySQL version lower than 5.5.3 can't directly store emoji.

And can store emoji by using pyemoji's encode/decode & replace & entities function.

Similar: https://pypi.python.org/pypi/pymoji

Installation
============

::

    pip install pyemoji


Usage
=====

encode/decode::

    Python 2.7.5 (default, Mar  9 2014, 22:15:05)
    Type "copyright", "credits" or "license" for more information.

    IPython 4.0.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: import pyemoji

    In [2]: pyemoji.encode(u'笑脸表情：😄')
    Out[2]: '\\u7b11\\u8138\\u8868\\u60c5\\uff1a\\U0001f604'

    In [3]: print pyemoji.encode(u'笑脸表情：😄')
    \u7b11\u8138\u8868\u60c5\uff1a\U0001f604

    In [4]: pyemoji.decode('\\u7b11\\u8138\\u8868\\u60c5\\uff1a\\U0001f604')
    Out[4]: u'\u7b11\u8138\u8868\u60c5\uff1a\U0001f604'

    In [5]: print pyemoji.decode('\\u7b11\\u8138\\u8868\\u60c5\\uff1a\\U0001f604')
    笑脸表情：😄


replace::

    In [6]: pyemoji.replace(u'笑脸表情：😄')
    Out[6]: u'\u7b11\u8138\u8868\u60c5\uff1a\ufffd'

    In [7]: print pyemoji.replace(u'笑脸表情：😄')
    笑脸表情：�

    In [8]: pyemoji.replace(u'笑脸表情：😄', '')
    Out[8]: u'\u7b11\u8138\u8868\u60c5\uff1a'

    In [9]: print pyemoji.replace(u'笑脸表情：😄', '')
    笑脸表情：


entities::

    In [10]: pyemoji.entities(u'笑脸表情：😄')
    Out[10]: u'\u7b11\u8138\u8868\u60c5\uff1a&#128516;'

    In [11]: print pyemoji.entities(u'笑脸表情：😄')
    笑脸表情：&#128516;


Params
======

unic::

    In [4]: import pyemoji

    In [5]: pyemoji.encode('笑脸表情：😄')
    Out[5]: '\\u7b11\\u8138\\u8868\\u60c5\\uff1a\\U0001f604'

    In [6]: pyemoji.encode(u'笑脸表情：😄')
    Out[6]: '\\u7b11\\u8138\\u8868\\u60c5\\uff1a\\U0001f604'
