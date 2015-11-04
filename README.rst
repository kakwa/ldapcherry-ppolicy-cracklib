*****************************
 ldapcherry-ppolicy-cracklib
*****************************

Cracklib password policy plugin for LdapCherry

.. image:: https://travis-ci.org/kakwa/ldapcherry-ppolicy-cracklib.svg?branch=master
    :target: https://travis-ci.org/kakwa/ldapcherry-ppolicy-cracklib
    
.. image:: https://coveralls.io/repos/kakwa/ldapcherry-ppolicy-cracklib/badge.svg 
    :target: https://coveralls.io/r/kakwa/ldapcherry-ppolicy-cracklib

.. image:: https://img.shields.io/pypi/dm/lcppolicy_cracklib.svg
    :target: https://pypi.python.org/pypi/lcppolicy_cracklib
    :alt: Number of PyPI downloads
    
.. image:: https://img.shields.io/pypi/v/lcppolicy_cracklib.svg
    :target: https://pypi.python.org/pypi/lcppolicy_cracklib
    :alt: PyPI version

.. image:: https://readthedocs.org/projects/ldapcherry-ppolicy-cracklib/badge/?version=latest
    :target: http://ldapcherry-ppolicy-cracklib.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

----

:Doc:    `Documentation on ReadTheDoc <http://ldapcherry-ppolicy-cracklib.readthedocs.org/en/latest/>`_
:Dev:    `Source code on GitHub <https://github.com/kakwa/ldapcherry-ppolicy-cracklib>`_
:PyPI:   `Package on Pypi <http://pypi.python.org/pypi/lcppolicy_cracklib>`_
:License: MIT
:Author:  Pierre-Francois Carpentier - copyright © 2015

----


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
| dict_path  | ppolicy | Path to dictionary                      | Path    | Default: default cracklib dictionary         |
|            |         |                                         |         | usually '/var/cache/cracklib/cracklib_dict'. |
|            |         |                                         |         |                                              |
|            |         |                                         |         | If pointing, for example, to */path/dict*,   |
|            |         |                                         |         | then */path/dict.hwm*, */path/dict.pwd* and  |
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

To build custom cracklib dictionaries:

* Get one or many word list files (for example here: http://www.winedt.org/Dict/).
* If necessary, encode it to UTF-8.
* Generate the cracklib dictionary.

example:

.. sourcecode:: bash
    
    # Just create a work directory
    $ mkdir dict/
    $ cd dict/

    # Recover and unzip the word list
    $ wget http://www.winedt.org/Dict/unicode/fr.zip
    $ unzip fr.zip

    # UTF-8 encoding
    $ file *
    fr.dic: Little-endian UTF-16 Unicode text
    fr.txt: ASCII text, with CRLF line terminators
    fr.zip: Zip archive data, at least v2.0 to extract
    $ iconv -f UTF-16 -t UTF-8 fr.dic >fr2.dic

    # Create the dictionary
    $ cat fr2.dic | cracklib-packer mydict

    # Result
    $ ls mydict*
    mydict.hwm  mydict.pwd  mydict.pwi

.. warning::

    Most distributions already provide dictionaries and a cron script
    to update cracklib dictionary (see '*apt-cache search 'dictionary' | egrep '^w'*' 
    and '*/etc/cron.daily/cracklib-runtime*' in Debian/Ubuntu for example)


