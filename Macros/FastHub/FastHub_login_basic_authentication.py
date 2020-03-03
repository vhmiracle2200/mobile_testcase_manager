from selenium.webdriver.common.by import By
from Macros.FastHub import xpath
from Macros.FastHub.Interfaces import Subscenario


class LoginBasicAuthentication(Subscenario):
    """
    one of three different type of login is Basic Authentication
    it`s User Pass Authentication one that automated
    """

    def do(self):
        print("******************************************************************")
        print("Login Basic Authentication started")

        if self.appium_driver.find_element(By.XPATH, xpath.CHANGELOG):
            self.appium_driver.back()
        if self.appium_driver.find_element(By.XPATH, xpath.BASIC_AUTHENTICATION_SIGNIN_TEXTVIEW):
            print("Ready to Sign in")
            self.appium_driver.find_element(By.XPATH, xpath.BASIC_AUTHENTICATION_SIGNIN_TEXTVIEW).click()

            self.appium_driver.find_element(By.XPATH, xpath.BASIC_AUTHENTICATION_SIGNIN_USERNAME_FIELD).send_keys(
                xpath.USERNAME)
            self.appium_driver.find_element(By.XPATH, xpath.BASIC_AUTHENTICATION_SIGNIN_PASSWORD_FIELD).send_keys(
                xpath.PASSWORD)
            self.appium_driver.find_element(By.XPATH, xpath.BASIC_AUTHENTICATION_SIGNIN_SIGNIN_BUTTON).click()
            print("Siging in ...")
            if self.appium_driver.find_element(By.XPATH, xpath.MAIN_TEXTVIEW_TOOLBAR):
                print("Main menu appeared,so Login successfully ")
            else:
                print("Login Failed!")

        else:
            print("Something wrong!")

        print("******************************************************************")




