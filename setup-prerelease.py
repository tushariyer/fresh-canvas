#!/usr/bin/env python

from distutils.core import setup

long_desc = ''
prerelease_version = ''

with open("README.md", "r", encoding="utf-8") as fh:
    long_desc = fh.read()
    fh.close()

with open("version.txt", "r", encoding="utf-8") as fh:
    prerelease_version = fh.read()
    fh.close()

setup(name='fresh-canvas-prerelease',
      version=prerelease_version,
      py_modules=['fresh-canvas'],
      description='Fresh Canvas [Pre-Release] | The Project Base',
      long_description=long_desc,
      long_description_content_type="text/markdown",
      author='Tushar Iyer',
      author_email='',
      url='https://github.com/tushariyer/fresh-canvas',
      project_urls={
              "Bug Tracker": "https://github.com/tushariyer/fresh-canvas/issues",
          }
      )
