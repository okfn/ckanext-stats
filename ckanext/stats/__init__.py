'''Statistics (and visuals) about the datasets in a CKAN instance.

Provided information:

  * Package counts by facet
    * Interactive
  * Total new packages over time (TODO)
  * Total new revisions (TODO)
'''
__version__ = '0.1'
# this is a namespace package
try:
    import pkg_resources
    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)

import os
from logging import getLogger
from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IRoutes, IConfigurer

log = getLogger(__name__)

class StatsPlugin(SingletonPlugin):
    '''Stats plugin.
    '''

    implements(IRoutes, inherit=True)
    implements(IConfigurer, inherit=True)

    def after_map(self, map):
        map.connect('stats', '/stats',
            controller='ckanext.stats:StatsController',
            action='index')
        map.connect('stats_action', '/stats/{action}',
            controller='ckanext.stats:StatsController')
        return map

    def update_config(self, config):
        here = os.path.dirname(__file__)
        rootdir = os.path.dirname(os.path.dirname(here))
        our_public_dir = os.path.join(rootdir, 'public')
        template_dir = os.path.join(rootdir, 'templates')
        config['extra_public_paths'] = ','.join([our_public_dir,
                config.get('extra_public_paths', '')])
        config['extra_template_paths'] = ','.join([template_dir,
                config.get('extra_template_paths', '')])

from ckan.lib.base import BaseController, c, g, request, response, session, render, config
import ckan.lib.stats
class StatsController(BaseController):
    def index(self):
        stats = ckan.lib.stats.Stats()
        rev_stats = ckan.lib.stats.RevisionStats()
        c.top_rated_packages = stats.top_rated_packages()
        c.most_edited_packages = stats.most_edited_packages()
        c.largest_groups = stats.largest_groups()
        c.top_tags = stats.top_tags()
        c.top_package_owners = stats.top_package_owners()
        c.new_packages_by_week = rev_stats.get_by_week('new_packages')
        c.package_revisions_by_week = rev_stats.get_by_week('package_revisions')
        return render('ckanext/stats/index.html')
            
    def leaderboard(self, id=None):
        c.solr_core_url = config.get('ckanext.stats.solr_core_url',
                'http://solr.okfn.org/solr/ckan')
        return render('ckanext/stats/leaderboard.html')

