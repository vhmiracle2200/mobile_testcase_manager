from selenium.webdriver.common.by import By
from Macros.FastHub import xpath
from Macros.FastHub.Interfaces import Subscenario


class Logout(Subscenario):

    def do(self):
        print("******************************************************************")
        print("Logout started")

        if self.appium_driver.find_element(By.XPATH, xpath.MAIN_TEXTVIEW_TOOLBAR):
            print("Open Drawer")
            if self.appium_driver.capabilities['deviceApiLevel'] >= 23:
                self.appium_driver.find_element(By.XPATH, xpath.MAIN_DRAWER_NAVIGATION_UP_23).click()
            else:
                self.appium_driver.find_element(By.XPATH, xpath.MAIN_DRAWER_NAVIGATION_UP).click()

            self.appium_driver.find_element(By.XPATH, xpath.DRAWER_PROFILE_TAB).click()
            self.appium_driver.find_element(By.XPATH, xpath.DRAWER_PROFILE_LOGOUT).click()
            if self.appium_driver.find_element(By.XPATH, xpath.LOGOUT_DIALOG):
                self.appium_driver.find_element(By.XPATH, xpath.LOGOUT_DIALOG_YES).click()
            else:
                print("Logout dialog doesnt show!")

            if self.appium_driver.find_element(By.XPATH, xpath.BASIC_AUTHENTICATION_SIGNIN_TEXTVIEW):
                print("Sign in menu appeared,so Logout successfully ")
            else:
                print("Logout failed!")

        else:
            print("Drawer doesnt Displayed!")
        print("******************************************************************")
