try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Jessica Appelbaum',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'jess.appelbaum@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': [''],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)