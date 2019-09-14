#! /usr/bin/python3

from distutils.core import setup

import os
from os import path

def find_packages():
    out = []
    for entry in os.scandir():
        if entry.is_dir():
            if entry.name.find('test') == -1:
                init = path.join(entry.path, '__init__.py')
                if path.isfile(init):
                    out.append(entry.name)

    return out


setup(name='magictag',
      version='0.1',
      description='Easly create new git tags',
      author='Filippo Ranza',
      author_email='filipporanza@gmail.com',
      url='https://github.com/FilippoRanza/magictag',
      packages=find_packages(),
      scripts=['magictag.py']
     )