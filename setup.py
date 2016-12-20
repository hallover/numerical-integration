#!/usr/bin/env python
# This module will allow you to pip install the package.
try:
    from setuptools import setup
    args = {}
except ImportError:
    from distutils.core import setup
    print("""\
*** WARNING: setuptools is not found.  Using distutils...
""")

from setuptools import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print(
        "warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

from os import path
setup(
    name='Integration',
    version='0.0.1',
    description='Numerical integration and convergence.',
    long_description=""
    if not path.isfile("README.md") else read_md('README.md'),
    author='Hayden Oliver',
    author_email='haydenoliver@physics.byu.edu',
    url='https://github.com/hallover/numerical-integration',
    license='MIT',
    setup_requires=['pytest-runner', ],
    tests_require=['pytest', 'python-coveralls'],
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    packages=['Integration'],
    package_data={'Integration': []},
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: Ubuntu',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ], )
