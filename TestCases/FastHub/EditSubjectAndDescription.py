import datetime
import os
import uuid

from Macros.FastHub.FastHub_Edit_Subject_Body import EditSubjectAndBody
from Macros.FastHub.FastHub_login_basic_authentication import LoginBasicAuthentication
from Macros.FastHub.FastHub_logout import Logout
from Macros.FastHub.Interfaces import TestScenarios
from appium import webdriver


class EditSubjectAndDescription(TestScenarios):

    def __init__(self):
        super().__init__()


    def preparation(self):
        """
        Setup and preparation for Test Environment like create Docker image or new Emulator
        """

        mPackages = "com.fastaccess.github"
        activity = "com.fastaccess.ui.modules.main.MainActivity"
        uid = str(uuid.uuid4())
        self.timeout = 30
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['full-reset'] = 'false'
        self.desired_caps['no-reset'] = 'true'
        # self.desired_caps['deviceName'] = 'R58M575Q2AW'
        self.desired_caps['deviceName'] = 'AVY9KA96A1402400'

        self.desired_caps['app'] = os.path.join(os.path.dirname(__file__),
                                                '/root/PycharmProjects/AUTDIV/apk/com.fastaccess.github_4.7.3.apk')
        self.desired_caps['appPackage'] = mPackages
        # Activity first page
        self.desired_caps['appActivity'] = activity
        self.appium_driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', self.desired_caps)
        self.appium_driver.implicitly_wait(time_to_wait=self.timeout)
        self.new_subject = "AUTDIV Subject ID-" + uid
        self.new_description = "new title change by AUTDIV,API level {}, from device model {} with unique id {} at {}".format(self.appium_driver.capabilities['deviceApiLevel'],self.appium_driver.capabilities['deviceModel'],uid,datetime.datetime.now().strftime(
                                                                                               "%I:%M%p on %B %d, %Y"))

    def teststeps(self):
        """
        test steps needs to reach our goal
        :return: None
        """
        sequentional = [
            LoginBasicAuthentication(),
            EditSubjectAndBody(self.timeout, self.new_subject, self.new_description),
            Logout()
        ]

        for sub in sequentional:
            sub.set_driver(self.appium_driver)
            sub.do()

    def finilizing(self):
        """
        Tear down the test

        :return: None
        """
        self.appium_driver.quit()
