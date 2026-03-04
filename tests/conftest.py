import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # Tự động tải và cài đặt ChromeDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") # Mở toàn màn hình
    
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver # Trả driver về cho các file test sử dụng
    
    driver.quit() # Đóng trình duyệt sau khi test xong