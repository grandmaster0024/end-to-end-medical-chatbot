from setuptools import find_packages, setup
import unittest

def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

setup(
    name='Generative AI Project',
    version='0.0.0',
    author='suraj kumar',
    author_email='surajwings12@gmail.com',
    packages=find_packages(),
    install_requires=[],
    test_suite='setup.my_test_suite',
)