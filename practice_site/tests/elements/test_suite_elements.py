import unittest
from tests.elements.forms_test import FormsTest
from tests.elements.checkbox_test import CheckboxTest
from tests.elements.dropdown_test import DropdownTest
from tests.elements.radio_test import RadioTest
from tests.elements.calendar_picker_test import DatePickerTest

#Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(FormsTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CheckboxTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(DropdownTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(RadioTest)
tc5 = unittest.TestLoader().loadTestsFromTestCase(DatePickerTest)

#Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])

unittest.TextTestRunner(verbosity=2).run(smokeTest)