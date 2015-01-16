#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyramid_transactional_celery
----------------------------------

Tests for `pyramid_transactional_celery` module.  In the end, we don't need
to test anything more than whether it properly handles the transactions, and
queues things at the right time.
"""

import unittest
import transaction
from uuid import uuid4
from celery import Celery


# XXX: Globals are evil. Need to find a better way to do this
task_output = []


class TestPyramidTransactionalCelery(unittest.TestCase):
    def setUp(self):
        self.celery_app = Celery()
        self.celery_app.conf.CELERY_ALWAYS_EAGER = True

        from pyramid_transactional_celery import (TransactionalTask, task_tm)

        class TestTask(TransactionalTask):
            """A simple task that appends a sentinel object to a global."""

            def run(self, sentinel):
                task_output.append(sentinel)

        @task_tm
        def test_task(sentinel):
            task_output.append(sentinel)

        self.celery_app.tasks['test_task_class'] = TestTask
        self.celery_app.tasks['test_task_fun'] = test_task
        transaction.begin()

    def test_successful_transaction(self):
        """Ensure that a successful transaction fires the task."""
        sentinel = uuid4()
        self.celery_app.tasks['test_task_class']().delay(sentinel)
        transaction.commit()
        self.assertIn(sentinel, task_output)

    def test_multiple_tasks(self):
        sentinels = [uuid4() for i in range(10)]
        for sentinel in sentinels:
            self.celery_app.tasks['test_task_class']().delay(sentinel)
        transaction.commit()
        self.assertListEqual(sentinels, task_output)

    def test_aborted_transaction(self):
        """Ensure that an aborted transaction does not fire the task."""
        sentinel = uuid4()
        self.celery_app.tasks['test_task_class']().delay(sentinel)
        transaction.abort()
        self.assertNotIn(sentinel, task_output)

    def test_successful_function_task(self):
        """Ensure that a successful transaction fires the task, even when it
        is a function."""
        sentinel = uuid4()
        self.celery_app.tasks['test_task_fun'].delay(sentinel)
        transaction.commit()
        self.assertIn(sentinel, task_output)

    def tearDown(self):
        global task_output
        task_output[:] = []

if __name__ == '__main__':
    unittest.main()
