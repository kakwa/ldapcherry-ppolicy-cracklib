# -*- coding: utf-8 -*-
# vim:set expandtab tabstop=4 shiftwidth=4:
#
# The MIT License (MIT)
# LdapCherry
# Copyright (c) 2014 Carpentier Pierre-Francois

import ldapcherry.ppolicy
import string
import cracklib
import sys
import re
from ldapcherry.exceptions import WrongParamValue

DIFF_OK = 0
MIN_LENGTH = 0
DIG_CREDIT = 0
UP_CREDIT = 0
LOW_CREDIT = 0
OTH_CREDIT = 0


def simple(new):

    digits = 0
    uppers = 0
    lowers = 0
    others = 0

    for character in new:
        if character in string.digits:
            digits = digits + 1
        elif character in cracklib.ASCII_UPPERCASE:
            uppers = uppers + 1
        elif character in cracklib.ASCII_LOWERCASE:
            lowers = lowers + 1
        else:
            others = others + 1
    if digits < cracklib.DIG_CREDIT:
        raise ValueError("has not enough digits")
    if uppers < cracklib.UP_CREDIT:
        raise ValueError("has not enough upper case characters")
    if lowers < cracklib.LOW_CREDIT:
        raise ValueError("has not enough lower case characters")
    if others < cracklib.OTH_CREDIT:
        raise ValueError("has not enough non alphanumeric characters")
    if len(new) < cracklib.MIN_LENGTH:
        raise ValueError("is too short")
    return 0


class PPolicy(ldapcherry.ppolicy.PPolicy):

    def __init__(self, config, logger):
        self.config = config
        self.min_length = self.get_param('min_length', 0)
        self.min_upper = self.get_param('min_upper', 0)
        self.min_lower = self.get_param('min_lower', 0)
        self.min_digit = self.get_param('min_digit', 0)
        self.min_other = self.get_param('min_other', 0)

        cracklib.OTH_CREDIT = self.min_other
        cracklib.MIN_LENGTH = self.min_length
        cracklib.UP_CREDIT = self.min_upper
        cracklib.LOW_CREDIT = self.min_lower
        cracklib.DIG_CREDIT = self.min_digit

        cracklib.simple = simple

        self.dict_path = self.get_param('dict_path', None)
        if self.dict_path is not None:
            try:
                cracklib.VeryFascistCheck('test', dictpath=self.dict_path)
            except ValueError as e:
                exstr = str(e)
                if exstr == 'second argument was not an absolute path!':
                    raise Exception(
                        'dict_path must be absolute, or not declared'
                        )
                else:
                    return
            except Exception as e:
                raise

    def check(self, password):
        try:
            cracklib.VeryFascistCheck(password, dictpath=self.dict_path)
        except ValueError as e:
            error = str(e)
            error = re.sub(r'^[iI][tT] ', '', error)
            return {'match': False, 'reason': 'Password ' + error}
        return {'match': True, 'reason': 'Password ok'}
