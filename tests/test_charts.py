import unittest
from unittest.mock import Mock, patch

from pynindo.const import CHARTS_URLS
from pynindo.nindo import Charts

from .utils import TEST_DATA, SKIP_REAL


class TestChartes(unittest.TestCase):

    def _mock_response(self, platform, action):
        mock_resp = Mock()
        mock_resp.json = Mock(return_value=TEST_DATA['charts'][platform][action])
        return mock_resp

    def _test_url(self, url, size=10):
        charts = Charts(url)
        self.assertEqual(len(charts), size)
        self.assertEqual(len(charts.json()), size)
        self.assertIsInstance(str(charts), str)

    @unittest.skipIf(SKIP_REAL, 'real api server')
    def test_charts_all_urls_call(self):
        for platform, urls in CHARTS_URLS.items():
            for action, url in urls.items():
                if action == 'small':
                    self._test_url(url, 10)
                else:
                    self._test_url(url, 100)

    @patch('pynindo.nindo.requests.get')
    def test_charts_all_urls(self, mock_get):
        for platform, urls in CHARTS_URLS.items():
            for action, url in urls.items():
                mock_get.return_value = self._mock_response(platform, action)
                if action == 'small':
                    self._test_url(url, 10)
                else:
                    self._test_url(url, 100)


if __name__ == '__main__':
    unittest.main()
