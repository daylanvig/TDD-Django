from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is invited to enter a to-do item
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        # User enters "Clean kitchen" into text box
        input_box.send_keys('Clean kitchen')

        # When user hits enter, page updates to show list
        # "1. Clean kitchen" as item in list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1. Clean kitchen' for row in rows))

        # User enters another todo list item in box ("Do laundry")

        # Page updates to show both items in list

        # User sees site generates unique URl to identify her/her list so it can be returned to.
        # There is some explanatory text for this.

        # User visits URL and sees list
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
