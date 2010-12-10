from setuptools import setup, find_packages
import sys, os

version = '0.0'
from ckanext.stats import __version__, __doc__ as long_description

setup(
	name='ckanext-stats',
	version=__version__,
	description="Stats information about content of a CKAN instance",
	long_description=long_description,
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Open Knowledge Foundation',
	author_email='ckan@okfn.org',
	url='http://ckan.org/',
	license='mit',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.stats'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	stats=ckanext.stats:StatsPlugin
	""",
)
