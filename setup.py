# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in paystack_erpnext/__init__.py
from paystack_erpnext import __version__ as version

setup(
	name='paystack_erpnext',
	version=version,
	description='An App that integrates Paystack into Erpnext',
	author='Isaac Larbi',
	author_email='isaac.larbi@access89.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
