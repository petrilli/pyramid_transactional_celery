#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'transaction',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyramid_transactional_celery',
    version='0.1.1',
    description='A transaction-aware Celery job setup',
    long_description=readme + '\n\n' + history,
    author='Christopher Petrilli',
    author_email='petrilli@amber.org',
    url='https://github.com/petrilli/pyramid_transactional_celery',
    packages=[
        'pyramid_transactional_celery',
    ],
    package_dir={'pyramid_transactional_celery':
                 'pyramid_transactional_celery'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='pyramid_transactional_celery',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
