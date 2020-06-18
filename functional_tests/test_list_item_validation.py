from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # User goes to home page and accidentally tries to submit
        # She hits enter in the empty box
        self.browser.get(self.live_server_url)
        self.enter_new_item('')

        # Page refreshes, and there is an error saying item can not be blank
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # User tries again with text
        self.enter_new_item('Buy eggs')
        self.wait_for_row_in_list_table('1. Buy eggs')

        # User tries again to submit an empty item
        self.enter_new_item('')

        # User sees warning again on list page
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # User corrects it by filling text in
        self.enter_new_item('Clean car')

        self.wait_for_row_in_list_table('1. Buy eggs')
        self.wait_for_row_in_list_table('2. Clean car')
