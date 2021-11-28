#!/usr/bin/env python

from distutils.core import setup

long_desc = 'Licensed under the generic MIT License.\"fresh-canvas\" can either be downloaded from the ' \
            'Releases page on GitHub and manually added to PATH or installed via \"pip\".'
prerelease_version = ''

with open("version.txt", "r", encoding="utf-8") as fh:
    prerelease_version = fh.read()
    fh.close()

setup(name='fresh-canvas-prerelease',
      version=prerelease_version,
      py_modules=['fresh-canvas'],
      description='Fresh Canvas [Pre-Release] | The Project Base',
      long_description=long_desc,
      long_description_content_type='text/markdown',
      author='Tushar Iyer',
      author_email='',
      url='https://github.com/tushariyer/fresh-canvas',
      project_urls={
              "Bug Tracker": "https://github.com/tushariyer/fresh-canvas/issues",
          }
      )
