from pages.login_page import LoginPage

def test_successful_login(driver):

    #1. Arrange: Create an instance of LoginPage and open the login page
    login_page = LoginPage(driver)

    #2. Act: Perform login action with valid credentials
    login_page.open()
    login_page.login("Admin", "admin123")

    #3. Assert: Verify that the user is redirected to the dashboard page
    assert "orangehrm" in login_page.get_title().lower()
def test_wrong_password_login(driver):

    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("Admin", "admin1234")

    assert "Invalid credentials" in login_page.get_error_message()
def test_wrong_username_login(driver):

    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("Admin1", "admin123")

    assert "Invalid credentials" in login_page.get_error_message()
def test_empty_username_login(driver):

    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("", "admin123")

    assert "Requis" or "Required" in login_page.get_required_message()
def test_empty_password_login(driver):

    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("Admin", "")

    assert "Requis" or "Required" in login_page.get_required_message()
def test_empty_username_password_login(driver):

    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("", "")

    list_error_messages = login_page.get_all_required_messages()

    assert len(list_error_messages) == 2

    assert "Requis" or "Required" == list_error_messages[0] 
    assert "Requis" or "Required" == list_error_messages[1]
