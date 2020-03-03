from selenium.webdriver.common.by import By
from Macros.FastHub import xpath
from Macros.FastHub.Interfaces import Subscenario
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EditSubjectAndBody(Subscenario):

    def __init__(self, _timeout, _new_subject, _new_description):
        self.timeout = _timeout
        self.new_subject = _new_subject
        self.new_description = _new_description
        self.old_subject = None
        self.old_description = None
        super().__init__()

    def do(self):
        print("******************************************************************")
        print("Editing Subject and Body started")

        if self.appium_driver.find_element(By.XPATH, xpath.MAIN_TAB_ISSUES):
            print("Main Menu Issue Tab Button Display")
            self.appium_driver.find_element(By.XPATH, xpath.MAIN_TAB_ISSUES).click()

            issue_elemets = self.appium_driver.find_elements(By.XPATH, xpath.ISSUES_RECYCLER_CHILDS)
            if len(issue_elemets) > 0:
                self.old_subject = issue_elemets[0].find_element(By.XPATH, xpath.ISSUE_SUBJECT_EXTRACT).get_attribute(
                    'text')
                self.old_description = issue_elemets[0].find_element(By.XPATH,
                                                                     xpath.ISSUE_DESCRIPTION_EXTRACT).get_attribute(
                    'text')
                print("Subject : {}".format(self.old_subject))
                print("Description : {}".format(self.old_description))
                issue_elemets[0].click()


                self.appium_driver.find_element(By.XPATH, xpath.COMMENT_MENU).click()
                self.appium_driver.find_element(By.XPATH, xpath.COMMENT_MENU_EDIT).click()

                print("Trying to Edit Subject and Description")
                self.appium_driver.find_element(By.XPATH, xpath.UPDATE_ISSUE_TITLE).clear()
                self.appium_driver.find_element(By.XPATH, xpath.UPDATE_ISSUE_TITLE).send_keys(self.new_subject)
                self.appium_driver.find_element(By.XPATH, xpath.UPDATE_ISSUE_DESCRIPTION_BUTTON).click()
                if self.appium_driver.find_element(By.XPATH, xpath.DESCRIPTION_MARKDOWN):
                    print("Markdown description page")
                    self.appium_driver.find_element(By.XPATH, xpath.DESCRIPTION_EDITTEXT).clear()
                    self.appium_driver.find_element(By.XPATH, xpath.DESCRIPTION_EDITTEXT).send_keys(self.new_description)
                else:
                    print("Editing Description Failed!")

                self.appium_driver.find_element(By.XPATH, xpath.DESCRIPTION_SUBMIT).click()

                # a sample of usage of explicitly to wait see element visible
                submit_element = WebDriverWait(self.appium_driver, self.timeout).until(
                    EC.visibility_of_element_located((By.XPATH, xpath.UPDATE_ISSUE_SUBMIT_BUTTON)))
                submit_element.click()
                if self.appium_driver.find_element(By.XPATH, xpath.DESCRIPTION_HEADER_TITLE):
                    self.appium_driver.find_element(By.XPATH, xpath.DESCRIPTION_HEADER_TITLE).get_attribute('text')
                    print("new Subject : {}".format(self.old_subject))
                    print("new Description : {}".format(self.old_description))
                    self.appium_driver.back()
                    print("backing to main menu.")


                else:
                    print("Update Failed!")
            else:
                print("no issue found in recycler!")

        else:
            print("Issues Tab Button doesnt display!")

        print("******************************************************************")
