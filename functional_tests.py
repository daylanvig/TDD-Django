from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        # User leaves website
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it(self):
        # User opens browser and navigates to homepage
        self.browser.get('http://localhost:8000')
        # User notices page title + header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # User is invited to enter a to-do item

        # User enters "Clean kitchen" into text box

        # When user hits enter, page updates to show list
        # "1. Clean kitchen" as item in list

        # User enters another todo list item in box ("Do laundry")

        # Page updates to show both items in list

        # User sees site generates unique URl to identify her/her list so it can be returned to.
        # There is some explanatory text for this.

        # User visits URL and sees list

if __name__ == '__main__':
    unittest.main(warnings='ignore')
