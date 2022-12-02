#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Jeremy Turner",
    author_email='jeremy@jeremymturner.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Advent of Code 2022 stuff",
    entry_points={
        'console_scripts': [
            'advent_of_code_2022=advent_of_code_2022.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='advent_of_code_2022',
    name='advent_of_code_2022',
    packages=find_packages(include=['advent_of_code_2022', 'advent_of_code_2022.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jeremymturner/advent_of_code_2022',
    version='0.1.0',
    zip_safe=False,
)
