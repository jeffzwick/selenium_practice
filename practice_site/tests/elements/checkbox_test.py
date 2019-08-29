from pages.element_pages.checkbox_page import CheckboxPage
from utilities.teststatus import Status
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CheckboxTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.check = CheckboxPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_singleCheckbox(self):
        title = self.check.verifyTitle()
        self.ts.mark(title, "Verify page Title")
        message = self.check.verifySingleCheck()
        self.ts.mark(message, "Verify single check box is checked")
        message_removed = self.check.verfiySingleUncheck()
        self.ts.mark(message_removed, "Verify message removed on uncheck")

    @pytest.mark.run(order=2)
    def test_uncheck(self):
        uncheck = self.check.verifyUncheckButton()
        self.ts.mark( uncheck, "Verify uncheck")

    @pytest.mark.run(order=3)
    def test_check(self):
        check = self.check.verifyCheckButton()
        self.ts.markFinal("test_check", check, "Verify check")


