import unittest
from datetime import datetime, timedelta
from .context import wiki_insight
from docs import conf


class TestUrlBuilder(unittest.TestCase):
    """Class that provides unit tests for UrlBuilder"""

    def test_number_of_urls(self):
        urls = wiki_insight.url_builder.UrlBuilder(5).get_urls()
        self.assertEqual(len(urls), 5)

    def test_side_urls(self):
        # Obtain how the first and last url would be
        hours = 5
        year, month = datetime.now().strftime("%Y,%m").split(",")
        base_link = f'{conf.base_link}{year}/{year}-{month}/'

        last_hour= (datetime.now() - timedelta(hours=0)).strftime("%Y,%m,%d,%H").split(",")
        first_hour = (datetime.now() - timedelta(hours=hours-1)).strftime("%Y,%m,%d,%H").split(",")

        format = conf.file_format
        last_url = base_link + f'pageviews-{last_hour[0]}{last_hour[1]}{last_hour[2]}-{last_hour[3]}0000' + format
        first_url = base_link + f'pageviews-{first_hour[0]}{first_hour[1]}{first_hour[2]}-{first_hour[3]}0000' + format

        # Obtain how the urls actually are
        urls = wiki_insight.url_builder.UrlBuilder(hours).get_urls()

        self.assertEqual(urls[0], last_url)
        self.assertEqual(urls[-1], first_url)

