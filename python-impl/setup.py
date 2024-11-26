#!/usr/bin/env python3

from setuptools import setup 

setup (
    name = 'novus_git',
    version = '1.0',
    packages = ['novus_git'],
    entry_points = {
        'console_scripts' : [
            'novus_git = novus_git.cli:main'
        ]
    }
)
