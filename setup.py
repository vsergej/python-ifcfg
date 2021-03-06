
from setuptools import setup, find_packages
import sys, os

setup(
    name='ifcfg',
    version='0.10',
    description="Python Ifconfig Wrapper for Unix/Linux/MacOSX",
    long_description="Python Ifconfig Wrapper for Unix/Linux/MacOSX",
    classifiers=[], 
    keywords='',
    author='Original author: BJ Dierkes',
    author_email='info@learningequality.org',
    url='https://github.com/learningequality/python-ifcfg',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ],
    setup_requires=[],
    entry_points="""
    """,
    namespace_packages=[],
)
