from pages.login_page import LoginPage

def test_successful_login(driver):
    # Arrange
    login_page = LoginPage(driver)

    # Act
    login_page.open()
    login_page.login("Admin", "admin123")

    # Assert
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

    msg = login_page.get_required_message()
    assert msg in ["Requis", "Required"]


def test_empty_password_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("Admin", "")

    msg = login_page.get_required_message()
    assert msg in ["Requis", "Required"]


def test_empty_username_password_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("", "")

    list_error_messages = login_page.get_all_required_messages()

    assert len(list_error_messages) == 2
    assert list_error_messages[0] in ["Requis", "Required"]
    assert list_error_messages[1] in ["Requis", "Required"]
