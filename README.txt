ckanext-stats
+++++++++++++

Provides CKAN with web pages showing statistics about its use and metadata stored.

This is a CKAN extension - http://ckan.org/wiki/Extensions.


Enabling
========

Enable by adding to your ckan.plugins line in CKAN config::

  ckan.plugins = stats


Tests
=====

To run tests written for this extension::

  pip -E pyenv install nose
  nosetests --ckan ckanext/stats/tests/