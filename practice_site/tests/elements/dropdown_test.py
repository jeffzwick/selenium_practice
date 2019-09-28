from pages.element_pages.dropdown_page import DropdownPage
from utilities.teststatus import Status
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DropdownTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.drop = DropdownPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    # running test for dropdown feature, using a single select dropdown
    def test_SingleDrop(self):
        title = self.drop.verifyTitle()
        self.ts.mark(title, "Verify page Title")
        single_message = self.drop.verifySingleDrop()
        self.ts.markFinal("Dropdown Test", single_message, "Verify single select dropdown")

    """
    Can't run test for multi-select, the page is not functioning properly
    
    @pytest.mark.run(order=2)
    def test_multi_first(self):
        multi_first = self.drop.verifyMultiFirstSelection()
        self.ts.mark( multi_first, "Verify first selected from multi-dropdown")

    @pytest.mark.run(order=3)
    def test_multi_all(self):
        multi_all = self.drop.verifyMultiAllSelections()
        self.ts.markFinal("Dropdown tests", multi_all, "Verify dropdown multi-select")
    """

