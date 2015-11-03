# -*- coding: utf-8 -*-
# vim:set expandtab tabstop=4 shiftwidth=4:
#
# The MIT License (MIT)
# LdapCherry
# Copyright (c) 2014 Carpentier Pierre-Francois

import ldapcherry.ppolicy
import cracklib
import sys
from ldapcherry.exceptions import WrongParamValue

DIFF_OK = 0
MIN_LENGTH = 0
DIG_CREDIT = 0
UP_CREDIT = 0
LOW_CREDIT = 0
OTH_CREDIT = 0


class PPolicy(ldapcherry.ppolicy.PPolicy):

    def __init__(self, config, logger):
        self.config = config
        self.min_length = self.get_param('min_length', 0)
        MIN_LENGTH = self.min_length
        self.min_upper = self.get_param('min_upper', 0)
        UP_CREDIT = self.min_upper
        self.min_lower = self.get_param('min_lower', 0)
        LOW_CREDIT = self.min_lower
        self.min_digit = self.get_param('min_digit', 0)
        DIG_CREDIT = self.min_digit
        self.min_other = self.get_param('min_other', 0)
        OTH_CREDIT = self.min_other
        self.dict_path = self.get_param('dict_path', None)
        if self.dict_path is not None:
            try:
                cracklib.VeryFascistCheck('test', dictpath=self.dict_path)
            except ValueError as e:
                return
            except:
                WrongParamValue(
                    'dict_path',
                    'ppolicy',
                    ['<path to valid dictionary file>'],
                    )

    def check(self, password):
        try:
            cracklib.VeryFascistCheck(password, dictpath=self.dict_path)
        except ValueError as e:
            return {'match': False, 'reason': str(e)}
        return {'match': True, 'reason': 'password ok'}

    def info(self):
        return ""
