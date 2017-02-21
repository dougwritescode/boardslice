#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(name='boardslice',
	version='0.1.0',
	description='Slice operations for the clipboard\'s contents.',
	author='Doug Walter',
	author_email='dougwritescode@gmail.com',
	url='',
	download_url='',
	packages=find_packages(),
	license='MIT',
	classifiers=[],
	entry_points = {
		'console_scripts' : ['boardslice = boardslice.__init__:main'] 
	}
)
