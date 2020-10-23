import unittest
import json
from dotted.utils import dot

from providers.mobrag_provider import *

PROVIDER = MobileRagnarokProvider()


class TestMobileRagnarokProvider(unittest.TestCase):

    def test_provider_fetch_data_monsters(self):
        """
            Test to load Monsters from MobileRagnarokProvider REST API
        :return:
        """
        result = PROVIDER.fetch_data(PROVIDER.get_categories().get('monsters'))
        items = dot(result.json()).result.items
        logger.info(items)
        self.assertTrue(items)


if __name__ == '__main__':
    unittest.main()
