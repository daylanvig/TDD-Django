from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # User goes to home page and accidentally tries to submit
        # She hits enter in the empty box

        # Page refereshes, and there is an error saying item can not be blank

        # User tries again with text

        # User tries again to submit an empty item

        # User sees warning again on list page

        # User corrects it by filling text in

        self.fail('TODO: Write this test')
