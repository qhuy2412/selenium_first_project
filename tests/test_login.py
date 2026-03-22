import csv
import pytest
from pages.login_page import LoginPage

def read_test_data():
    with open("login_user.csv") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

@pytest.mark.parametrize("data", read_test_data())
def test_login(driver, data):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(data["username"], data["password"])

    if data["expected"] == "success":
        assert "orangehrm" in login_page.get_title().lower()
    elif ";" in data["expected"]:  # trường hợp cả username và password rỗng
        errors = login_page.get_all_required_messages()
        for msg in errors:
            assert msg in ["Required", "Requis"]
    else:
        assert data["expected"] in login_page.get_error_message()
