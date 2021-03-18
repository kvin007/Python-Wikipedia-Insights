from datetime import datetime, timedelta
from docs import conf


class UrlBuilder:
    # Class that helps build the urls needed to download the files from wikipedia
    def __init__(self, hours_backwards):
        self._base_link = conf.base_link
        self._hours_backwards = hours_backwards

    def _get_base_url(self):
        year, month = datetime.now().strftime("%Y,%m").split(",")
        return f'{self._base_link}{year}/{year}-{month}/'

    def get_urls(self):
        hours_list = [(datetime.now() - timedelta(hours=x)).strftime("%Y,%m,%d,%H").split(",")
                      for x in range(self._hours_backwards)]
        urls = []
        for date in hours_list:
            file_name = f'pageviews-{date[0]}{date[1]}{date[2]}-{date[3]}0000'
            url = self._get_base_url() + file_name + conf.file_format
            urls.append((url, file_name))
        return urls
