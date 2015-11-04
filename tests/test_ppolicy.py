#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
from __future__ import unicode_literals

import pytest
import sys
import lcppolicy_cracklib
import cherrypy
import logging
import os
from ldapcherry.exceptions import *
from disable import travis_disabled

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

config_dict = {
    'min_length': 0,
    'min_upper': 0,
    'min_lower': 0,
    'min_digit': 0,
    'min_other': 0,
    'dict_path': os.getcwd() + '/tests/resources/cracklib_dict',
}

config_falsedict = {
    'min_length': 0,
    'min_upper': 0,
    'min_lower': 0,
    'min_digit': 0,
    'min_other': 0,
    'dict_path': os.getcwd() + '/tests/resources/false_dict',
}

config_errordictpath = {
    'min_length': 0,
    'min_upper': 0,
    'min_lower': 0,
    'min_digit': 0,
    'min_other': 0,
    'dict_path': os.getcwd() + '/tests/resources/dict_not_exist',
}

config_errordictnotabspath = {
    'min_length': 0,
    'min_upper': 0,
    'min_lower': 0,
    'min_digit': 0,
    'min_other': 0,
    'dict_path': './tests/resources/dict_not_exist',
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
 
    def test_dictNotAbsPath(self):
        try:
            ppolicy = lcppolicy_cracklib.PPolicy(config_errordictnotabspath, cherrypy.log)
        except Exception as e:
            assert str(e) == 'dict_path must be absolute, or not declared'
        else:
            raise AssertionError("expected an exception")
 
    def test_dictDoesNotExist(self):
        try:
            ppolicy = lcppolicy_cracklib.PPolicy(config_errordictpath, cherrypy.log)
        except OSError:
            return
        else:
            raise AssertionError("expected an exception")
 
    def test_Dict(self):
        password = 'isaword'
        ppolicy = lcppolicy_cracklib.PPolicy(config_dict, cherrypy.log)
        ret = ppolicy.check(password)
        exp = {'match': False, 'reason': 'Password is based on a dictionary word'}
        assert exp == ret

    #@travis_disabled
    #def test_dictFalse(self):
    #    try:
    #        ppolicy = lcppolicy_cracklib.PPolicy(config_falsedict, cherrypy.log)
    #    except RuntimeError:
    #        return
    #    else:
    #        raise AssertionError("expected an exception")
