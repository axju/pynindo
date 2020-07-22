import io
import unittest
from unittest.mock import Mock, patch

from pynindo.cli import main

from tests.utils import TEST_DATA


class TestCli(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('pynindo.nindo.requests.get')
    def call_test(self, args, data, result, mock_requests, mock_stdout):
        mock_requests.return_value = Mock()
        mock_requests.return_value.json = Mock(return_value=data)
        main(args)
        self.assertEqual(len(mock_stdout.getvalue().split('\n')), result)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('pynindo.nindo.requests.get')
    def call_test_multi_data(self, args, data, result, mock_requests, mock_stdout):
        mock_requests.return_value = Mock()
        mock_requests.return_value.json = Mock(side_effect=data)
        main(args)
        self.assertEqual(len(mock_stdout.getvalue().split('\n')), result)

    def test_cli_charts_youtube(self):
        self.call_test(['charts', 'youtube'], TEST_DATA['charts']['youtube']['small'], 12)

    def test_cli_charts(self):
        self.call_test_multi_data(['charts'], TEST_DATA['charts']['youtube'].values(), 412)


if __name__ == '__main__':
    unittest.main()
