import unittest
from unittest.mock import Mock, MagicMock, patch

from pynindo.nindo import Milestones

from tests.utils import TEST_DATA, SKIP_REAL


class TestMilestones(unittest.TestCase):

    def _mock_response(self):
        mock_resp = Mock()
        mock_resp.json = MagicMock(side_effect=[TEST_DATA['milestones']['new'], TEST_DATA['milestones']['past']])
        return mock_resp

    def _test_milestones(self):
        milestones = Milestones()
        self.assertTrue(len(milestones.new.json()) > 0)
        self.assertTrue(len(milestones.past.json()) > 0)
        self.assertEqual(len(milestones.json()), len(milestones.new.json()) + len(milestones.past.json()))
        self.assertIsInstance(str(milestones), str)

    @unittest.skipIf(SKIP_REAL, 'real api server')
    def test_milestones_call(self):
        self._test_milestones()

    @patch('pynindo.nindo.requests.get')
    def test_milestones(self, mock_get):
        mock_get.return_value = self._mock_response()
        self._test_milestones()


if __name__ == '__main__':
    unittest.main()
