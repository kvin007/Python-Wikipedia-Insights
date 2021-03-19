import unittest
from datetime import datetime, timedelta
from .context import wiki_insight
from requests.exceptions import Timeout
from unittest.mock import patch
from docs import conf


class TestFileHandler(unittest.TestCase):
    """Class that provides unit tests for FileHandler"""

    @patch('wiki_insight.file_handler.FileHandler.download_files')
    def test_download_files(self, mock_download_files):
        mock_download_files.return_value = ['pageviews-20210318-200000.gz','pageviews-20210318-190000.gz']
        file_name = 'pageviews-20210318-200000.gz'
        self.assertIn(file_name, mock_download_files())
