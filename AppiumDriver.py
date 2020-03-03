from appium import webdriver
'''
this is appium driver Class that we use to  initiate driver to interact with appium server
'''

class AppiumDriver:

    def __init__(self,remote_url,desired_caps):
        '''
        Initilizing appium Remote Driver
        :param remote_url: IP , ID or address of device
        :param desired_caps: set of options that is required to define device
        '''
        self.driver = webdriver.Remote(remote_url, desired_caps)

    def get_driver(self):
        '''

        :return: Appium driver object
        '''
        return self.driver

