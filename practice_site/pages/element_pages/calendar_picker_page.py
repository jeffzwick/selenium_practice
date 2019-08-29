import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class DatePickerPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

#######################
#####  LOCATORS #######
#######################

    _date_picker_icon = "//i[@class='glyphicon glyphicon-th']"
    _todays_date = "//div[@class='datepicker-days']//th[@class='today'][contains(text(),'Today')]"
    _clear_date = "//div[@class='datepicker-days']//th[@class='clear'][contains(text(),'Clear')]"
    _enter_date = "//input[@placeholder='dd/mm/yyyy']"
    _verify_enter_date = "//td[@class='active day' and contains(text(),'14')]"
    _pick_date = "//td[contains(text(),'15')]"
    _verify_pick_date = "//td[@class='active day' and contains(text(),'15')]"
    _disabled_date = "//td[@class='disabled disabled-date day' and contains(text(),'25')]"
    _active_day = "//td[@class='active day']"
    _todays_active_day = "//td[@class='today active day']"

    def clickDateIcon(self):
        self.elementClick(locator=self._date_picker_icon, locatorType= "xpath")

    def clickTodaysDate(self):
        self.elementClick(locator=self._todays_date, locatorType="xpath")

    def clickClearDate(self):
        self.elementClick(locator=self._clear_date, locatorType="xpath")

    def enterDate(self):
        self.elementClick(locator=self._enter_date, locatorType="xpath")
        self.sendKeys("14/08/2019", locator=self._enter_date, locatorType="xpath")

    def selectDate(self):
        self.elementClick(locator=self._pick_date, locatorType="xpath")
        self.clickDateIcon()

    def selectInvalidDate(self):
        self.elementClick(locator=self._enter_date, locatorType="xpath")
        self.sendKeys("25/08/2019", locator=self._enter_date, locatorType="xpath")

    def verifyTitle(self):
        self.nav.navigateToDatePickerPage()
        return self.verifyPageTitle("Selenium Easy - Best Demo website for Bootstrap Date picker")

    def verifyTodaysDate(self):
        self.clickDateIcon()
        self.clickTodaysDate()
        self.clickDateIcon()
        result = self.isElementPresent(locator=self._todays_active_day, locatorType= "xpath")

        return result

    def verfiyClearDate(self):
        self.clickClearDate()
        result = self.isElementPresent(locator= self._todays_active_day, locatorType="xpath")

        return not result

    def verifyEnterDate(self):
        self.enterDate()
        result = self.isElementPresent(locator=self._verify_enter_date, locatorType= "xpath")

        return result

    def verifySelectDate(self):
        self.selectDate()
        result = self.isElementPresent(locator=self._verify_pick_date, locatorType="xpath")

        return result

