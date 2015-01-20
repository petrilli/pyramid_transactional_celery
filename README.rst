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


Limitations
-----------

Currently, the code is designed around Celery v3.1, and it is unknown whether
it will work with previous versions.  I'm more than happy to integrate changes
that would make it work with other releases, but since I generally stay on
the latest release, it isn't a priority for my own development.


Usage
-----

Using the library is a relatively easy thing to do. First, you'll need to
integrate Celery into your Pyramid application, for which I recommend using
pyramid_celery_. Once that's done, you simply need to start creating your
tasks. The big difference is for function-based tasks, you use a different
decorator::

    from pyramid_transactional_celery import task_tm

    @task_tm
    def add(x, y):
        """Add two numbers together."""
        return x + y

That's all there is to it. For class-based tasks, you simply need to
subclass ``TransactionalTask`` instead of ``Task``::

    from pyramid_transactional_celery import TransactionalTask

    class SampleTask(TransactionalTask):
        """A sample task that is transactional."""
        def run(x, y):
            return x + y

That's it. Bob's your uncle.

.. _pyramid_celery: https://pypi.python.org/pypi/pyramid_celery/
