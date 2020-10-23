"""
    Data provider from http://mobileragnarok.com/ы
"""
import requests
from http.cookies import SimpleCookie
from requests_toolbelt.utils import dump
from app import logger
from .provider import BaseProvider

API_CATEGORIES_URLS = {
    'monsters': '/api/monsters-data'
}


class MobileRagnarokProvider(BaseProvider):
    def __init__(self):
        self.base_url = 'http://mobileragnarok.com/'

    def get_categories(self):
        return API_CATEGORIES_URLS

    def fetch_data(self, category):
        """
        Try to fetch monsters data from database.
        To propertly work we need to get before and pass X-XSRF-TOKEN header
        :param category:
        :return:
        """
        payload = {
            "filters": {
                "star": "false",
                "future": "false",
                "nospawn": "false",
                "mvp": "true",
                "mini": "true",
                "size": [],
                "nature": [],
                "sort": ["Base exp"], "order": "false"
            },
            "page": 1
        }

        # init cookies to get XSRF-TOKEN
        logger.debug('# - Prepare Get %s Request', self.base_url)
        response = requests.get(url=self.base_url)
        data = dump.dump_all(response)
        logger.debug('# - Get %s Request dump /n%s', self.base_url, data.decode('UTF-8'))

        cookie = SimpleCookie()
        cookie.load(response.cookies)

        logger.debug('# - Get %s request Cookies', self.base_url)
        logger.debug(cookie)

        # prepere specific header
        spec_header_value_1 = cookie['XSRF-TOKEN'].key + '=' + cookie['XSRF-TOKEN'].value
        spec_header_value_2 = cookie['ragnarok_mobile_eternal_love_eu_session'].key + '=' \
                              + cookie['ragnarok_mobile_eternal_love_eu_session'].value

        headers = {
            'X-XSRF-TOKEN': cookie['XSRF-TOKEN'].value.replace('%3D', '='),
            'Content-Type': 'application/json;charset=UTF-8',
            'Host': 'mobileragnarok.com',
            'Cookie': spec_header_value_1 + '; ' + spec_header_value_2
        }

        logger.debug('# - Post %s Request Prepared Headers', API_CATEGORIES_URLS.get('monsters'))
        logger.debug(headers)

        response = requests.post(url=self.base_url + '/' + category, params=payload, headers=headers)
        data = dump.dump_all(response)

        logger.debug('# - Post Request %s Response dump', API_CATEGORIES_URLS.get('monsters'))
        logger.debug(data.decode('UTF-8'))
        return response
