import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By

class Test:
    
    def __init__(self, url):
        chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
    
    def get_screenshot_in_cart(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, "header-bottom-cart__button row items-center justify-center no-wrap cursor-pointer")
        cart_icon.click()
        time.sleep(2)  # wait for cart page to load
        self.driver.save_screenshot("cart_screenshot.png")
    
    def add_cookie_object(self, cookie_name, cookie_value):
        cookie_object = {"name": cookie_name, "value": cookie_value}
        self.driver.add_cookie(cookie_object)
    
    def replace_user_agent_on_random_value(self):
        user_agent = UserAgent().random
        print(f"Current User-Agent: {user_agent}")
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
        new_user_agent = self.driver.execute_script("return navigator.userAgent")
        print(f"New User-Agent: {new_user_agent}")
        
        
test = Test("https://comfy.ua/ua/")

# Get screenshot in cart
test.get_screenshot_in_cart()

# Add cookie object
test.add_cookie_object("test_cookie", "test_value")

# Replace user agent on random value
test.replace_user_agent_on_random_value()