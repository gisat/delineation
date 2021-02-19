#!/usr/bin/env python3
from setuptools import setup, find_packages
from delineation import __verison__


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='urban_delineation',
    version=__verison__,
    description='Urban delineation processor',
    author='Michal Opletal',
    author_email='michal.opletal@gisat.cz',
    long_description=readme(),
    packages=find_packages(),
    install_requires=[
        'xarray==0.15.0',
        'rioxarray==0.1.1',
        'numpy==1.18.1'

    ],
    zip_safe=False,
    package_data={"": ["*.json"]},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)