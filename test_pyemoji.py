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

from __future__ import division, absolute_import, print_function, unicode_literals

import pyemoji


def main():
    # Encode/Decode

    print(">> pyemoji.encode")
    print("    Exec: {0}".format("pyemoji.encode(u'笑脸表情：😄')"))
    print("    Result: {0}".format(pyemoji.encode('笑脸表情：😄')))
    print()
    print(">> pyemoji.decode")
    print("    Exec: {0}".format("pyemoji.decode('\\u7b11\\u8138\\u8868\\u60c5\\uff1a\\U0001f604')"))
    print("    Result: {0}".format(pyemoji.decode('\\u7b11\\u8138\\u8868\\u60c5\\uff1a\\U0001f604')))
    print()
    print("    Exec: {0}".format("pyemoji.decode(b'\\u7b11\\u8138\\u8868\\u60c5\\uff1a\\U0001f604')"))
    print("    Result: {0}".format(pyemoji.decode(b'\\u7b11\\u8138\\u8868\\u60c5\\uff1a\\U0001f604')))
    print()

    # Replace

    print(">> pyemoji.replace")
    print("    Exec: {0}".format("pyemoji.replace(u'笑脸表情：😄')"))
    print("    Result: {0}".format(pyemoji.replace('笑脸表情：😄')))
    print()
    print("    Exec: {0}".format("pyemoji.replace(u'笑脸表情：😄', '')"))
    print("    Result: {0}".format(pyemoji.replace('笑脸表情：😄', '')))
    print()

    # Entities

    print(">> pyemoji.entities")
    print("    Exec: {0}".format("pyemoji.entities(u'笑脸表情：😄')"))
    print("    Result: {0}".format(pyemoji.entities('笑脸表情：😄')))
    print()

if __name__ == '__main__':
    main()
