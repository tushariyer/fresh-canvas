#!/usr/bin/env python

from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='fresh-canvas-prerelease',
      version='0.1.7',
      py_modules=['fresh-canvas'],
      description='Fresh Canvas [Pre-Release] | The Project Base',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Tushar Iyer',
      author_email='',
      url='https://github.com/tushariyer/fresh-canvas',
      project_urls={
              "Bug Tracker": "https://github.com/tushariyer/fresh-canvas/issues",
          }
      )
