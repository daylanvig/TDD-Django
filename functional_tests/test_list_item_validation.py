from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # User goes to home page and accidentally tries to submit
        # She hits enter in the empty box
        self.browser.get(self.live_server_url)
        self.enter_new_item('')

        # Browser intercepts invalid request, does not allow submission
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('#id_text:invalid'))

        # She types and error disappears
        input_box = self.get_item_input_box()
        input_box.send_keys('Buy eggs')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('#id_text:valid'))
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1. Buy eggs')

        # User tries again to submit an empty item
        self.enter_new_item('')
        # User sees warning again on list page
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('#id_text:invalid'))

        # User corrects it by filling text in
        self.get_item_input_box().send_keys('Clean car')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('#id_text:valid'))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1. Buy eggs')
        self.wait_for_row_in_list_table('2. Clean car')
