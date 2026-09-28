from pathlib import Path
import unittest


class SiteTest(unittest.TestCase):
    def test_site_has_visible_marker(self):
        page = (Path(__file__).resolve().parents[1] / 'site' / 'index.html').read_text()
        self.assertIn('<main>', page)
        self.assertIn('</main>', page)
        self.assertIn('<title>WorkBridge Web Test</title>', page)
