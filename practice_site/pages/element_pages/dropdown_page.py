import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage
import time


class DropdownPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

#######################
#####  LOCATORS #######
#######################

    _single_select_drop = "//select[@id='select-demo']"
    _select_from_single_drop = "//option[contains(text(),'Tuesday')]"
    _single_select_message = "//p[@class='selected-value' and contains(text(), 'Day selected :- Tuesday')]"
    _select_nj = "//option[contains(text(),'New Jersey')]"
    _select_ohio = "//option[contains(text(),'Ohio')]"
    _first_selected_button = "//button[@id='printMe']"
    _all_selected_button = "//button[@id='printAll']"
    _first_selected_message = "//p[@class='getall-selected' and contains(text(), 'First selected option is : New Jersey')]"
    _all_selected_message = "//p[@class='getall-selected' and contains(text(), 'Options selected are : New Jersey,Ohio')]"

    def clickSingleDrop(self):
        self.elementClick(locator=self._single_select_drop, locatorType= "xpath")

    def selectSingleDropSelection(self):
        self.elementClick(locator=self._select_from_single_drop, locatorType="xpath")

    def selectMultiDropdown(self):
        self.elementClick(locator=self._select_nj, locatorType="xpath")
        self.elementMultiClick(locator=self._select_ohio, locatorType="xpath")

    def clickMultiFirstSelected(self):
        self.elementClick(locator=self._first_selected_button, locatorType="xpath")

    def clickMultiAllSelected(self):
        self.elementClick(locator=self._all_selected_button, locatorType="xpath")

    def verifyTitle(self):
        self.nav.navigateToDropdownPage()
        return self.verifyPageTitle("Selenium Easy Demo - Automate All Scenarios")

    def verifySingleDrop(self):
        self.clickSingleDrop()
        self.selectSingleDropSelection()
        result = self.isElementPresent(locator=self._single_select_message, locatorType= "xpath")

        return result

    def verifyMultiFirstSelection(self):
        self.selectMultiDropdown()
        self.clickMultiFirstSelected()
        result = self.isElementPresent(locator=self._first_selected_message, locatorType= "xpath")

        return result

    def verifyMultiAllSelections(self):
        self.clickMultiAllSelected()
        result = self.isElementPresent(locator=self._all_selected_message, locatorType= "xpath")

        return result
