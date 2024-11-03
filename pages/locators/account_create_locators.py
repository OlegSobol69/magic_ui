from selenium.webdriver.common.by import By

firstname_field_loc = (By.ID, "firstname")
lastname_field_loc = (By.ID, "lastname")
email_field_loc = (By.ID, "email_address")
password_loc = (By.ID, "password")
confirm_password_field_loc = (By.ID, "password-confirmation")
create_button_loc = (By.CSS_SELECTOR, "button.action.submit.primary")

error_message_validation_loc = (By.XPATH, "//*[@id='password-error']")

firstname_error_message_loc = (By.ID, "firstname-error")
lastname_error_message_loc = (By.ID, "lastname-error")
email_error_message_loc = (By.ID, "email_address-error")
password_error_message_loc = (By.ID, "password-error")
confirm_password_error_message_loc = (By.ID, "password-confirmation-error")
