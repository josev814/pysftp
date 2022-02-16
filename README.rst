pysftp
======

A simple interface to SFTP.  The module offers high level abstractions and
task based routines to handle your SFTP needs.  Checkout the Cook Book, in the
docs, to see what pysftp can do for you.

Running Tests
-------------

::

 pip3 install -U -r requirements-dev.txt
 pip3 install -U -r requirements-travis.txt
 python3 setup.py install
 pytest -v --cov -c pytest-travisci.ini tests
 codecov

Requirements
------------

paramiko >= 1.17

Example
-------

::

    import pysftp

    with pysftp.Connection('hostname', username='me', password='secret') as sftp:
        with sftp.cd('public'):             # temporarily chdir to public
            sftp.put('/my/local/filename')  # upload file to public/ on remote
            sftp.get('remote_file')         # get a remote file


Supports
--------

Drone-IO
________
Tested on Python 2.7, 3.2, 3.3, 3.4

.. image:: https://drone.io/bitbucket.org/dundeemt/pysftp/status.png
    :target: https://drone.io/bitbucket.org/dundeemt/pysftp/latest
    :alt: Build Status

Travis-CI
_________

Tested on Python 3.4, 3.5, 3.7, 3.8, 3.9, 3.10

.. image:: https://travis-ci.org/josev814/denyhosts.svg?branch=master
    :target: https://travis-ci.org/josev814/denyhosts.svg?branch=master
    :alt: Build Status

CodeCov
-------
.. image:: https://codecov.io/gh/josev814/pysftp/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/josev814/pysftp


Links
_____
* Project:  https://bitbucket.org/dundeemt/pysftp
* Download: https://pypi.python.org/pypi/pysftp
* Documentation: http://pysftp.rtfd.org/

