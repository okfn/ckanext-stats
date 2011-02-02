from ckan.lib.base import BaseController, render
import ckan.lib.stats

class StatsController(BaseController):

    def index(self):
        from pylons import tmpl_context as c 
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
        from pylons import tmpl_context as c 
        c.solr_core_url = config.get('ckanext.stats.solr_core_url',
                'http://solr.okfn.org/solr/ckan')
        return render('ckanext/stats/leaderboard.html')

