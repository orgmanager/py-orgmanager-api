from setuptools import setup

setup(
	name='py-orgmanager-api',
	version='1.0.0',
	description='A Python client for the OrgManager API',
	packages=['orgmanager']
	author = 'OrgManager',
	license = 'MPL',
	url = 'https://github.com/orgmanager/py-orgmanager-api',
	install_requires= [
		'requests'
	],
	classifiers = [
		'Natural Language :: English',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6'
	],
	keywords = 'orgmanager'
)
