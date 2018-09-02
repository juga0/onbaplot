#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name='onbaplot',
    version='0.0.1',
    description='Create graphs from Tor bandwidth list files.',
    long_description='Create graphs from Tor bandwidth list files v1.0.0 and'
        'v1.1.0 or raw measurements files.',
    author='juga',
    author_email='juga@riseup.net',
    license='CC0',
    url="https://github.com/juga0/tor_bw_stats",
    classifiers=[
        'Development Status :: 4 - Beta',
        "Environment :: Console",
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Networking',
    ],
    packages=find_packages(),
    include_package_data=True,
    keywords='tor onion bandwidth measurements scanner relay circuit stats '
             'plot graphs',
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'onbaplot = onbaplot.onbaplot:main',
        ]
    },
    install_requires=[
        'matplotlib',
        'sbws',
    ],
    extras_require={
        'dev': ['flake8'],
        'test': ['tox', 'pytest', 'coverage'],
        'doc': ['sphinx', 'pylint'],
    },
)
