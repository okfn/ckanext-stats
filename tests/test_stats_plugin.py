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

    def test_01_index(self):
        url = url_for('/statsnew', action='index')
        out = self.app.get(url)
        assert 'New stats plugin' in out, out

    def test_02_config(self):
        from pylons import config
        paths = config['extra_public_paths']
        rootdir = os.path.dirname(os.path.dirname(__file__))
        assert rootdir in paths, (rootdir, paths)

