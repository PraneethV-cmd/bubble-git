#!/usr/bin/env python3
from setuptools import setup

setup (
    name = 'bubblegit',
    version = '1.0',
    packages = ['bubblegit'],
    entry_points = {
        'console_scripts': [
            'bubblegit = bubblegit.cli:main'
        ]
    }
)
