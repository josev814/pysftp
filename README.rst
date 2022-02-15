pysftp
======

A simple interface to SFTP.  The module offers high level abstractions and
task based routines to handle your SFTP needs.  Checkout the Cook Book, in the
docs, to see what pysftp can do for you.

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
Tested on Python 2.7, 3.6, 3.7, 3.8, 3.9, 3.10

.. image:: https://drone.io/bitbucket.org/dundeemt/pysftp/status.png
    :target: https://drone.io/bitbucket.org/dundeemt/pysftp/latest
    :alt: Build Status

.. image:: https://travis-ci.org/josev814/denyhosts.svg?branch=master
    :target: https://travis-ci.org/josev814/denyhosts.svg?branch=master
    :alt: Build Status



* Project:  https://bitbucket.org/dundeemt/pysftp
* Download: https://pypi.python.org/pypi/pysftp
* Documentation: http://pysftp.rtfd.org/

