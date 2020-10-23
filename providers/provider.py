"""
    Base class for rom data providers ( databases)
"""


class BaseProvider(object):
    def ___init__(self, ):
        self.base_url = ''

    @staticmethod
    def get_categories(self):
        return {}

    def fetch_data(self, category):
        """
            Overrides in childs
        :param category: category of data ( monsters, items ...)
        :return:
        """
        None
