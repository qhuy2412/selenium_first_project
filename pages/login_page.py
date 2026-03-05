from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    #1. Locators : declare all location of elements on the page
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.orangehrm-login-button") # if element does not have id or name, we can use css selector but it must be unique 
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p.oxd-alert-content-text") 
    REQUIRED_MESSAGE = (By.CSS_SELECTOR, "span.oxd-input-field-error-message")

    #2. Actions: declare all actions that can be performed on the page
    def open(self):
        self.open_url(self.URL)
    
    def login(self, username, password):
        #This function group all actions to perform login flow
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        #Return error message text if login fails
        error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return error_element.text
    def get_required_message(self):
        required_element = self.wait.until(EC.visibility_of_element_located(self.REQUIRED_MESSAGE))
        return required_element.text
    def get_all_required_messages(self):
        required_elements = self.wait.until(EC.visibility_of_all_elements_located(self.REQUIRED_MESSAGE))
        return [element.text for element in required_elements]