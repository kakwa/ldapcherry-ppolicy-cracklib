#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from __future__ import unicode_literals

import pytest
import sys

def u(x):
    if sys.version < '3':
        import codecs
        return codecs.unicode_escape_decode(x)[0]
    else:
        return x

class TestLib(object):

        def test_password(self):
            password = 'toto'
            assert True == False
