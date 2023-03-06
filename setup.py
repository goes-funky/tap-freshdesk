#!/usr/bin/env python

from setuptools import setup

setup(name='tap-freshdesk',
      version='0.10.1',
      description='Singer.io tap for extracting data from the Freshdesk API',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_freshdesk'],
      install_requires=[
          'singer-python==5.9.0',
          'requests==2.26.0',
          'backoff==1.8.0'
      ],
      entry_points='''
          [console_scripts]
          tap-freshdesk=tap_freshdesk:main
      ''',
      packages=['tap_freshdesk'],
      package_data={
          "tap_freshdesk": ["tap_freshdesk/schemas/*.json"]
      },
      include_package_data=True,
)
