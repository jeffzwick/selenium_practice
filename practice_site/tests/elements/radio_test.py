from pages.element_pages.radio_page import RadioPage
from utilities.teststatus import Status
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RadioTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.radio = RadioPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    # running test for male radio button
    def test_maleRadio(self):
        title = self.radio.verifyTitle()
        self.ts.mark(title, "Verify page Title")
        male_radio = self.radio.verifyRadioMale()
        self.ts.mark(male_radio, "Verify male radio button")

    @pytest.mark.run(order=2)
    # running test for female radio button
    def test_femaleRadio(self):
        female_radio = self.radio.verifyRadioFemale()
        self.ts.markFinal("Radio Button Tests", female_radio, "Verify female radio button")


