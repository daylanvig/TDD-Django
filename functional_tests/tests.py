from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 2


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        # User leaves website
        # refresh stops a page forced exit error
        self.browser.refresh()
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.25)

    def enter_new_item(self, item_text):
        """ Enter value into input box and submit form """
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys(item_text)
        input_box.send_keys(Keys.ENTER)

    def test_can_start_a_list_for_one_user(self):
        # User opens browser and navigates to homepage
        self.browser.get(self.live_server_url)
        # User notices page title + header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is invited to enter a to-do item
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute(
            'placeholder'), 'Enter a to-do item')

        # User enters "Clean kitchen" into text box
        # When user hits enter, page updates to show list
        self.enter_new_item('Clean kitchen')

        # "1. Clean kitchen" as item in list
        self.wait_for_row_in_list_table('1. Clean kitchen')

        # User enters another todo list item in box ("Do laundry")
        self.enter_new_item('Do laundry')
        self.wait_for_row_in_list_table('1. Clean kitchen')
        self.wait_for_row_in_list_table('2. Do laundry')

        self.fail('Finish the test!')

    def test_can_start_start_lists_at_different_urls(self):
        # User starts new todo list
        self.browser.get(self.live_server_url)
        self.enter_new_item('Clean kitchen')
        self.wait_for_row_in_list_table('1. Clean kitchen')
        # User sees site generates unique URl to identify her/her list so it can be returned to.
        user_list_url = self.browser.current_url
        self.assertRegex(user_list_url, '/lists/.+')
        # There is some explanatory text for this.

        # Begin new user session, clearing cookies so first user doesnt impact
        self.browser.refresh()
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # OtherUser visits home page
        self.browser.get(self.live_server_url)

        # OtherUser does not see user's items
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Clean kitchen', page_text)
        self.assertNotIn('Do laundry', page_text)

        # OtherUser enters todo item
        self.enter_new_item('Mow lawn')
        self.wait_for_row_in_list_table('1. Mow lawn')

        # OtherUser gets unique URL
        other_user_list_url = self.browser.current_url
        self.assertRegex(other_user_list_url, '/lists/.+')
        self.assertNotEqual(other_user_list_url, user_list_url)

        # OtherUser still does not see user's items
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Clean kitchen', page_text)
        self.assertNotIn('Do laundry', page_text)

    def test_layout_and_styling(self):
        # User goes to home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width']/2, 512, delta=10)
