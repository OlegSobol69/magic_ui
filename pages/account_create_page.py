from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
from pages.locators import account_create_locators as loc


class AccountCreate(BasePage):
    page_url = "/customer/account/create/"

    def required_fields_present_account_form(self):
        assert self.find(loc.firstname_field_loc).is_displayed()
        assert self.find(loc.lastname_field_loc).is_displayed()
        assert self.find(loc.email_field_loc).is_displayed()
        assert self.find(loc.password_loc).is_displayed()
        assert self.find(loc.confirm_password_field_loc).is_displayed()

    def send_invalid_password(self, password):
        self.find(loc.password_loc).send_keys(password)
        self.find(loc.create_button_loc).click()

    def check_error_message(self, message):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(loc.error_message_validation_loc))
        error_message = self.driver.find_element(*loc.error_message_validation_loc)
        assert error_message.text == message, f"Ожидаемый сообщение {message}, но получен '{error_message.text}'"

    def click_create_button(self):
        self.find(loc.create_button_loc).click()

    def check_validation_messages(self):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(loc.firstname_error_message_loc))
        assert self.find(
            loc.firstname_error_message_loc).is_displayed(), "firstname message is not displayed"
        assert self.find(
            loc.lastname_error_message_loc).is_displayed(), "lastname message is not displayed"
        assert self.find(loc.email_error_message_loc).is_displayed(), "email message is not displayed"
        assert self.find(
            loc.password_error_message_loc).is_displayed(), "password message is not displayed"
        assert self.find(
            loc.confirm_password_error_message_loc).is_displayed(), "conf password message is not displayed"

    def check_fields_highlighted_red(self):
        assert "mage-error" in self.find(loc.firstname_field_loc).get_attribute("class")
        assert "mage-error" in self.find(loc.lastname_field_loc).get_attribute("class")
        assert "mage-error" in self.find(loc.email_field_loc).get_attribute("class")
        assert "mage-error" in self.find(loc.password_loc).get_attribute("class")
        assert "mage-error" in self.find(loc.confirm_password_field_loc).get_attribute("class")
