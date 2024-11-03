from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc


class EcoFriendly(BasePage):
    page_url = "/collections/eco-friendly.html"

    def check_page_title(self, expected_title):
        actual_title = self.find(loc.page_title_loc).text
        assert actual_title == expected_title, f"expected title '{expected_title}', but actual '{actual_title}'"

    def check_product_items_displayed(self):
        products = self.find_all(loc.product_items_loc)
        assert len(products) > 0, "not displayed items"

    def search_product_result(self, search_term):
        search_field = self.find(loc.search_field_loc)
        search_field.send_keys(search_term)
        search_field.send_keys(Keys.ENTER)
        product_items = self.find_all(loc.product_items_loc)
        assert any(search_term.lower() in item.text.lower() for item in product_items), \
            f"no have product name {search_term}"
