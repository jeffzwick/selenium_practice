import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class CheckboxPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

#######################
#####  LOCATORS #######
#######################

    _single_checkbox = "//input[@id='isAgeSelected']"
    _single_check_confirmed = "//div[contains(text(), 'Success - Check box is checked')]"
    _single_check_unchecked = "//div[@style='display: none;']"
    _option1 = "//label[text()='Option 1']"
    _option2 = "//label[text()='Option 2']"
    _option3 = "//label[text()='Option 3']"
    _option4 = "//label[text()='Option 4']"
    _check_all = "//input[@value='Check All']"
    _uncheck_all = "//input[@value='Uncheck All']"

    def clickSingleCheckBox(self):
        self.elementClick(locator=self._single_checkbox, locatorType= "xpath")

    def clickoption1(self):
        self.elementClick(locator=self._option1, locatorType="xpath")

    def clickoption2(self):
        self.elementClick(locator=self._option2, locatorType="xpath")

    def clickoption3(self):
        self.elementClick(locator=self._option3, locatorType="xpath")

    def clickoption4(self):
        self.elementClick(locator=self._option4, locatorType="xpath")

    def verifyTitle(self):
        self.nav.navigateToCheckBoxPage()
        return self.verifyPageTitle("Selenium Easy - Checkbox Demo for automation using selenium")

    def verifySingleCheck(self):
        self.clickSingleCheckBox()
        result = self.isElementPresent(locator=self._single_check_confirmed, locatorType= "xpath")

        return result

    def verfiySingleUncheck(self):
        self.clickSingleCheckBox()
        result = self.isElementPresent(locator= self._single_check_unchecked, locatorType="xpath")

        return result

    def verifyUncheckButton(self):
        self.clickoption1()
        self.clickoption2()
        self.clickoption3()
        self.clickoption4()
        result = self.isElementPresent(locator=self._uncheck_all, locatorType= "xpath")

        return result

    def verifyCheckButton(self):
        self.clickoption1()
        self.clickoption2()
        result = self.isElementPresent(locator=self._check_all, locatorType="xpath")

        return result

