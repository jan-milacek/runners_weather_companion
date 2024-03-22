#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Jan Milacek",
    author_email='jan.milacek@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Program approximating weather forecast from different data sources and recommending appropriate running clothes.",
    entry_points={
        'console_scripts': [
            'runners_weather_companion=runners_weather_companion.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='runners_weather_companion',
    name='runners_weather_companion',
    packages=find_packages(include=['runners_weather_companion', 'runners_weather_companion.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jan-milacek/runners_weather_companion',
    version='0.1.0',
    zip_safe=False,
)
