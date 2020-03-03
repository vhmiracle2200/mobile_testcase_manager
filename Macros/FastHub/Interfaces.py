import unittest
from abc import ABC, abstractmethod


class TestScenarios(ABC):
    '''
    scenarios to have structure for test
    '''

    def __init__(self):
        self.appium_driver = None
        self.desired_caps = {}

    @abstractmethod
    def preparation(self):
        pass

    @abstractmethod
    def teststeps(self):
        pass

    @abstractmethod
    def finilizing(self):
        pass


class Subscenario(ABC):
    '''
    this is a sub scenarios that do a particular job,like login, logout ,etc
    '''

    def __init__(self):
        self.appium_driver = None
        self.timeout = 10
        super().__init__()

    @abstractmethod
    def do(self):
        pass

    def set_driver(self, _driver):
        """
        :type _driver: RemoteDriver for instance
        """
        self.appium_driver = _driver
