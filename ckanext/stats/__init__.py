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

from logging import getLogger
from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IRoutes

log = getLogger(__name__)

class StatsPlugin(SingletonPlugin):
    '''Stats plugin.
    '''

    implements(IRoutes, inherit=True)

    def after_map(self, map):
        # will rename once we have moved main stats code in here
        map.connect('/statsnew',
            controller='ckanext.stats:StatsController',
            action='index')
        map.connect('/statsnew/:action',
            controller='ckanext.stats:StatsController')
        return map

from ckan.lib.base import BaseController, c, g, request, response, session
class StatsController(BaseController):
    def index(self, id=None):
        return 'New stats plugin'

