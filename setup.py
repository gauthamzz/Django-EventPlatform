#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

with open('wsgi/stegolica/requirements.txt', 'r') as rq:
    requirements = rq.read()

setup(
    name='stegolica',
    version='0.1',
    description='Effe Quiz',
    author='Gautham Santosh',
    author_email='thabeatsz@gmail.com',
    install_requires=[requirements]
)
