#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from __future__ import unicode_literals

import pytest
import sys
import lcppolicy_cracklib
import cherrypy
import logging

def syslog_error(msg='', context='',
        severity=logging.INFO, traceback=False):
    pass

cherrypy.log.error = syslog_error

def u(x):
    if sys.version < '3':
        import codecs
        return codecs.unicode_escape_decode(x)[0]
    else:
        return x

config = {
    'min_length': 14,
    'min_upper': 3,
    'min_lower': 5,
    'min_digit': 2,
    'min_other': 2,
    'dict_path': None,
}

password = 'MzgzMDQw,NDgK3830.'

class TestLib(object):

        def test_base(self):
            ppolicy = lcppolicy_cracklib.PPolicy(config, cherrypy.log)
            ret = ppolicy.check(password)
            exp = {'match': True, 'reason': 'Password ok'}
            assert exp == ret

        def test_upper(self):
            password = 'mzgzmdqw,NDgk3830.'
            ppolicy = lcppolicy_cracklib.PPolicy(config, cherrypy.log)
            ret = ppolicy.check(password)
            exp = {'match': False, 'reason': 'Password has not enough upper case characters'}
            assert exp == ret

        def test_lower(self):
            password = 'QWENIHSYT,NDgk3830.'
            ppolicy = lcppolicy_cracklib.PPolicy(config, cherrypy.log)
            ret = ppolicy.check(password)
            exp = {'match': False, 'reason': 'Password has not enough lower case characters'}
            assert exp == ret

        def test_digits(self):
            password = 'QWENIHSYT,NDgkqa3p.'
            ppolicy = lcppolicy_cracklib.PPolicy(config, cherrypy.log)
            ret = ppolicy.check(password)
            exp = {'match': False, 'reason': 'Password has not enough digits'}
            assert exp == ret

        def test_other(self):
            password = 'MzgzMDQw,NDgK3830p'
            ppolicy = lcppolicy_cracklib.PPolicy(config, cherrypy.log)
            ret = ppolicy.check(password)
            exp = {'match': False, 'reason': 'Password has not enough non alphanumeric characters'}
            assert exp == ret

        def test_other(self):
            password = 'Mzaw,NDgK38p,'
            ppolicy = lcppolicy_cracklib.PPolicy(config, cherrypy.log)
            ret = ppolicy.check(password)
            exp = {'match': False, 'reason': 'Password is too short'}
            assert exp == ret


