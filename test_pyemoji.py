# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

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
