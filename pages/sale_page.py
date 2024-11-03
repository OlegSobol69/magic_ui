from pages.base_page import BasePage
from pages.locators import sale_locators as loc


class Sale(BasePage):
    page_url = "/sale.html"

    def check_page_title(self, expected_title):
        actual_title = self.find(loc.page_title_loc).text
        assert actual_title == expected_title, f"expected title '{expected_title}', but actual '{actual_title}'"

    def check_logo_displayed_on_page(self):
        logo = self.find(loc.logo_loc)
        assert logo.is_displayed(), "logo is not displayed"

    def check_menu_displayed(self):
        menu = self.find(loc.menu_loc)
        assert menu.is_displayed(), "menu is not displayed"
