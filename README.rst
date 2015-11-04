*****************************
 ldapcherry-ppolicy-cracklib
*****************************

Cracklib password policy plugin for LdapCherry

.. image:: https://travis-ci.org/kakwa/ldapcherry-ppolicy-cracklib.svg?branch=master
    :target: https://travis-ci.org/kakwa/ldapcherry-ppolicy-cracklib
    
.. image:: https://coveralls.io/repos/kakwa/ldapcherry-ppolicy-cracklib/badge.svg 
    :target: https://coveralls.io/r/kakwa/ldapcherry-ppolicy-cracklib

.. image:: https://img.shields.io/pypi/dm/ldapcherry-ppolicy-cracklib.svg
    :target: https://pypi.python.org/pypi/ldapcherry-ppolicy-cracklib
    :alt: Number of PyPI downloads
    
.. image:: https://img.shields.io/pypi/v/ldapcherry-ppolicy-cracklib.svg
    :target: https://pypi.python.org/pypi/ldapcherry-ppolicy-cracklib
    :alt: PyPI version

.. image:: https://readthedocs.org/projects/ldapcherry-ppolicy-cracklib/badge/?version=latest
    :target: http://ldapcherry-ppolicy-cracklib.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

Install
=======

From pypi:

.. sourcecode:: bash

    pip install lcppolicy_cracklib

From sources:

.. sourcecode:: bash

    $ python setup.py install

Configure
=========

Enable module
-------------

To enable this module, set **ppolicy.module** to **lcppolicy_cracklib** in section **[ppolicy]**
of *ldapcherry.ini*

Parameters
----------

This plugin takes the following parameters in *ldapcherry.ini* (all the parameters are optional):

+------------+---------+-----------------------------------------+---------+----------------------------------------------+
| Parameter  | Section |            Description                  | Values  |                Comment                       |
+============+=========+=========================================+=========+==============================================+
| min_length | ppolicy | Minimum length of password              | integer | Default: 0                                   |
+------------+---------+-----------------------------------------+---------+----------------------------------------------+
| min_upper  | ppolicy | Minimum number of upper case characters | Integer | Default: 0                                   |
+------------+---------+-----------------------------------------+---------+----------------------------------------------+
| min_digit  | ppolicy | Minimum number of digit characters      | Integer | Default: 0                                   |
+------------+---------+-----------------------------------------+---------+----------------------------------------------+
| min_lower  | ppolicy | Minimum number of lower case characters | Integer | Default: 0                                   |
+------------+---------+-----------------------------------------+---------+----------------------------------------------+
| min_other  | ppolicy | Minimum number of non alphanumeric      | Integer | Default: 0                                   |
|            |         | characters                              |         |                                              |
+------------+---------+-----------------------------------------+---------+----------------------------------------------+
| dict_path  | ppolicy | Path to dictionnary                     | Path    | Default: default cracklib dictionnary        |
|            |         |                                         |         | usually '/var/cache/cracklib/cracklib_dict'. |
|            |         |                                         |         |                                              |
|            |         |                                         |         | If pointing to for example to */path/dict*   |
|            |         |                                         |         | */path/dict.hwm*, */path/dict.pwd* and       |
|            |         |                                         |         | */path/dict.pwi* must exist.                 |
+------------+---------+-----------------------------------------+---------+----------------------------------------------+

Example
-------

.. sourcecode:: ini

    [ppolicy]

    # password policy module
    ppolicy.module = 'lcppolicy_cracklib'
    # minimum password length (optional default: 0)
    min_length = 10
    # minimum number of upper case characters (optional default: 0)
    min_upper = 1
    # minimum number of lower case characters (optional default: 0)
    min_lower = 2
    # minimum number of digits (optional default: 0)
    min_digit = 1
    # minimum number of non alphanumeric characters (optional default: 0)
    min_other = 1
    # path to dictionary (optional)
    dict_path = '/var/cache/cracklib/cracklib_dict'

Custom dictionary
=================

To build your own cracklib dictionary:
