import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class FormsPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

#######################
#####  LOCATORS #######
#######################

    _enter_message = "//input[@id='user-message']"
    _show_message = "//button[contains(text(),'Show Message')]"
    _verify_message = "//span[text()='test1!']"
    _enter_a = "//input[@id='sum1']"
    _enter_b = "//input[@id='sum2']"
    _get_total = "//button[contains(text(),'Get Total')]"
    _verify_total = "//span[text()='13']"

#######################
#####  METHODS  #######
#######################

    def enterMessage(self, message="test1!"):
        self.sendKeys(message, locator=self._enter_message, locatorType= "xpath")

    def clickShowMessage(self):
        self.elementClick(locator=self._show_message, locatorType= "xpath")

    def enterA(self, textA=7):
        self.sendKeys(textA, locator=self._enter_a, locatorType= "xpath")

    def enterB(self, textB=6):
        self.sendKeys(textB, locator=self._enter_b, locatorType="xpath")

    def clickGetTotal(self):
        self.elementClick(locator=self._get_total, locatorType="xpath")

    def verifyTitle(self):
        self.nav.navigateToFormsPage()
        return self.verifyPageTitle("Selenium Easy Demo - Simple Form to Automate using Selenium")

    def verifyMessageText(self):
        self.enterMessage()
        self.clickShowMessage()
        result = self.isElementPresent(locator=self._verify_message, locatorType= "xpath")

        return result

    def verifyTotal(self):
        self.enterA()
        self.enterB()
        self.clickGetTotal()
        result = self.isElementPresent(locator=self._verify_total, locatorType= "xpath")

        return result