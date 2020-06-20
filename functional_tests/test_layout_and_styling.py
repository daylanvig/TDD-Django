from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Smoke test
        # User goes to home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width']/2, 512, delta=10)
