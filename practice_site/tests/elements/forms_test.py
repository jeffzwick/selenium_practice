from pages.home.navigation_page import NavigationPage
from pages.element_pages.forms_page import FormsPage
from utilities.teststatus import Status
import time
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class FormsTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.forms = FormsPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run()
    def test_message(self):
        self.forms.verifyTitle()
        title = self.forms.verifyTitle()
        self.ts.mark(title, "Verify page Title")
        message = self.forms.verifyMessageText()
        self.ts.mark(message, "Verify message entered in form box 1")

    @pytest.mark.run()
    def test_total(self):
        total = self.forms.verifyTotal()
        self.ts.markFinal("test_total", total, "Verify total entered in form box 2")




