import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class RadioPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

#######################
#####  LOCATORS #######
#######################

    _male_radio1 = "//input[@value='Male' and @name ='optradio']"
    _female_radio1 = "//input[@value='Female' and @name ='optradio']"
    _check_value1 = "//button[@id='buttoncheck']"
    _male_radio1_confirm = "//p[contains(text(), \"Radio button 'Male' is checked\")]"
    _female_radio1_confirm = "//p[contains(text(), \"Radio button 'Female' is checked\")]"

    def clickMaleRadio1(self):
        self.elementClick(locator=self._male_radio1, locatorType= "xpath")

    def clickFemaleRadio1(self):
        self.elementClick(locator=self._female_radio1, locatorType="xpath")

    def clickCheckValue1(self):
        self.elementClick(locator=self._check_value1, locatorType="xpath")


    def verifyTitle(self):
        self.nav.navigateToRadioPage()
        return self.verifyPageTitle("Selenium Easy Demo - Radio buttons demo for Automation")

    def verifyRadioMale(self):
        self.clickMaleRadio1()
        self.clickCheckValue1()
        result = self.isElementPresent(locator=self._male_radio1_confirm, locatorType= "xpath")

        return result

    def verifyRadioFemale(self):
        self.clickFemaleRadio1()
        self.clickCheckValue1()
        result = self.isElementPresent(locator=self._female_radio1_confirm, locatorType= "xpath")

        return result


