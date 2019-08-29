import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ######################
    ###### LOCATORS ######
    ######################

    _input_forms = "//li[@class='tree-branch']//a[contains(text(),'Input Forms')]"
    _form = "//li[@class='tree-branch']//ul//li//a[contains(text(),'Simple Form Demo')]"
    _checkbox = "//li[@class='tree-branch']//ul//li//a[contains(text(),'Checkbox Demo')]"
    _radio = "//li[@class='tree-branch']//ul//li//a[contains(text(),'Radio Buttons Demo')]"
    _dropdown = "//li[@class='tree-branch']//ul//li//a[contains(text(),'Select Dropdown List')] "
    _input = "//li[@class='tree-branch']//ul//li//a[contains(text(),'Input Form Submit')]"
    _date_pickers = "//a[@class='dropdown-toggle'][contains(text(),'Date pickers')]"#"//li[@class='tree-branch']//a[contains(text(),'Date pickers')]"
    _bootstrap_date_picker = "Bootstrap Date Picker"#"//li[@class='tree-branch']//ul//li//a[contains(text(),'Bootstrap Date Picker')"
    _table = "//a[@class='dropdown-toggle'][contains(text(),'Table')]"
    _pagination = "Table Pagination" #link text
    _data_search = "Table Data Search" #link text
    _filter = "Table Filter" #link text
    _progress_bars = "//a[@class='dropdown-toggle'][contains(text(),'Progress Bars')]"
    _jquery_download = "JQuery Download Progress bars" #link text
    _bootstrap_progress_bar = "Bootstrap Progress bar" #link text
    _drag_and_drop = "Drag & Drop Sliders" #link text
    _alerts = "//a[@class='dropdown-toggle'][contains(text(),'Alerts & Modals')]"
    _bootstrap_alert = "Bootstrap Alerts" #link text
    _bootstrap_modal = "Bootstrap Modals" #link text
    _javascript_alert = "Javascript Alerts" #link text
    _list_box = "//a[@class='dropdown-toggle'][contains(text(),'List Box')]"
    _bootstrap_list_box = "Bootstrap List Box" #link text
    _jquery_list_box = "JQuery List Box" #link text

    ###################
    ##### METHODS #####
    ###################

    def navigateToFormsPage(self):
        self.webScroll(direction="down")
        self.elementClick(locator=self._input_forms, locatorType="xpath")
        self.elementClick(locator=self._form, locatorType="xpath")

    def navigateToCheckBoxPage(self):
        self.webScroll(direction="down")
        self.elementClick(locator=self._input_forms, locatorType="xpath")
        self.elementClick(locator=self._checkbox, locatorType="xpath")

    def navigateToRadioPage(self):
        self.webScroll(direction="down")
        self.elementClick(locator=self._input_forms, locatorType="xpath")
        self.elementClick(locator=self._radio, locatorType="xpath")

    def navigateToDropdownPage(self):
        self.webScroll(direction="down")
        self.elementClick(locator=self._input_forms, locatorType="xpath")
        self.elementClick(locator=self._dropdown, locatorType="xpath")

    def navigateToDatePickerPage(self):
        #self.webScroll(direction="down")
        self.elementClick(locator=self._date_pickers, locatorType="xpath")
        self.elementClick(locator=self._bootstrap_date_picker, locatorType="link")

    def navigateToPaginationPage(self):
        self.elementClick(locator=self._table, locatorType="xpath")
        self.elementClick(locator=self._pagination, locatorType="xpath")

    def navigateToDataSearchPage(self):
        self.elementClick(locator=self._table, locatorType="xpath")
        self.elementClick(locator=self._data_search, locatorType="xpath")

    def navigateToFilterPage(self):
        self.elementClick(locator=self._table, locatorType="xpath")
        self.elementClick(locator=self._filter, locatorType="xpath")

    def navigateToDragAndDropPage(self):
        self.elementClick(locator=self._progress_bars, locatorType="xpath")
        self.elementClick(locator=self._drag_and_drop, locatorType="xpath")

    def navigateToBootstrapAlertPage(self):
        self.elementClick(locator=self._alerts, locatorType="xpath")
        self.elementClick(locator=self._bootstrap_alert, locatorType="xpath")

    def navigateToJQueryListBoxPage(self):
        self.elementClick(locator=self._list_box, locatorType="xpath")
        self.elementClick(locator=self._jquery_list_box, locatorType="xpath")

    """
    def navigateTo(self):
        userSettingsElement = self.waitForElement(locator=self._,
                                                  locatorType="", pollFrequency=1)
        #self.elementClick(element=userSettingsElement)
        self.elementClick(locator=self._,
                          locatorType="")
    """