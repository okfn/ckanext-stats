import os
from paste.deploy import appconfig
import paste.fixture
from ckan.config.middleware import make_app
from ckan.tests import conf_dir, url_for

class TestStatsPlugin:

    @classmethod
    def setup_class(cls):
        config = appconfig('config:test.ini', relative_to=conf_dir)
        config.local_conf['ckan.plugins'] = 'stats'
        wsgiapp = make_app(config.global_conf, **config.local_conf)
        cls.app = paste.fixture.TestApp(wsgiapp)

    def test_01_config(self):
        from pylons import config
        paths = config['extra_public_paths']
        publicdir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
            'public')
        assert paths.startswith(publicdir), (publicdir, paths)

    def test_02_index(self):
        url = url_for('/statsnew', action='index')
        out = self.app.get(url)
        assert 'Total number of packages' in out, out
        assert 'Most Edited Packages' in out, out

    def test_03_leaderboard(self):
        url = url_for(controller='statsnew', action='leaderboard')
        out = self.app.get(url)
        assert 'Leaderboard' in out, out

