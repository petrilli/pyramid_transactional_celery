===============================
Transactional Celery for Pyramid
===============================

.. image:: https://badge.fury.io/py/pyramid_transactional_celery.png
    :target: http://badge.fury.io/py/pyramid_transactional_celery

.. image:: https://travis-ci.org/petrilli/pyramid_transactional_celery.png?branch=master
        :target: https://travis-ci.org/petrilli/pyramid_transactional_celery

.. image:: https://pypip.in/d/pyramid_transactional_celery/badge.png
        :target: https://pypi.python.org/pypi/pyramid_transactional_celery


A transaction-aware Celery job setup. This is integrated with the Zope
transaction_ package, which implements a full two-phase commit protocol.
While it is not designed for anything other than Pyramid, it also does not
use any component of Pyramid. It's simply not tested anywhere else.

* Free software: BSD license
* Documentation: https://pyramid_transactional_celery.readthedocs.org.

.. _transaction: https://pypi.python.org/pypi/transaction

Features
--------

* Queues tasks into a thread-local when they are called either using ``delay``
  or ``apply_async``.
* If the transaction is aborted, then the tasks will never be called.
* If the transaction is committed, the tasks will go through their normal
  ``apply_async`` process and be queued for processing.
