from pages.element_pages.calendar_picker_page import DatePickerPage
from utilities.teststatus import Status
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DatePickerTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.date = DatePickerPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_TodaysDate(self):
        title = self.date.verifyTitle()
        self.ts.mark(title, "Verify page Title")
        today = self.date.verifyTodaysDate()
        self.ts.mark(today, "Verify today's date button")

    @pytest.mark.run(order=2)
    def test_ClearDate(self):
        clear = self.date.verfiyClearDate()
        self.ts.mark(clear, "Verify clear date")

    @pytest.mark.run(order=3)
    def test_EnterDate(self):
        enter_date = self.date.verifyEnterDate()
        self.ts.mark(enter_date, "Verify manual enter")

    @pytest.mark.run(order=4)
    def test_SelectDate(self):
        date_select = self.date.verifySelectDate()
        self.ts.markFinal("testSelectDate", date_select, "Verify select date")

