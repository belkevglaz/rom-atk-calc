"""
    Main core logic
"""
from core.log import log


class Calculator(object):

    def __init__(self, provider):
        self.provider = provider

    def calc(self):
        """
        Calculate
        :return:
        """
        log('Calculator activated')
