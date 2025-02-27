#!/usr/bin/env python

from setuptools import setup

setup(name='tap-freshdesk',
      version='0.11.0',
      description='Singer.io tap for extracting data from the Freshdesk API',
      author='Stitch',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_freshdesk'],
      install_requires=[
          'singer-python @ git+https://github.com/peliqan-io/singer-python@master',
          'requests==2.20.0',
          'backoff==1.8.0'
      ],
      entry_points='''
          [console_scripts]
          tap-freshdesk=tap_freshdesk:main
      ''',
      packages=['tap_freshdesk'],
      package_data = {
          'tap_freshdesk/schemas': [
              'agents.json',
              'companies.json',
              'contacts.json',
              'conversations.json',
              'groups.json',
              'roles.json',
              'satisfaction_ratings.json',
              'tickets.json',
              'time_entries.json',
          ],
      },
      include_package_data=True,
)
