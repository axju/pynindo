import unittest
from unittest.mock import Mock, patch

from pynindo.nindo import Viral

from tests.utils import TEST_DATA, SKIP_REAL


class TestMilestones(unittest.TestCase):

    def _mock_response(self):
        mock_resp = Mock()
        mock_resp.json = Mock(return_value=TEST_DATA['viral'])
        return mock_resp

    def _test_viral(self):
        viral = Viral()
        self.assertTrue(len(viral.json()) > 0)
        self.assertIsInstance(str(viral), str)

    @unittest.skipIf(SKIP_REAL, 'real api server')
    def test_viral_call(self):
        self._test_viral()

    @patch('pynindo.nindo.requests.get')
    def test_viral(self, mock_get):
        mock_get.return_value = self._mock_response()
        self._test_viral()


if __name__ == '__main__':
    unittest.main()
