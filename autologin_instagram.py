import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from time import sleep

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

class Test:
    def __init__(self, service, driver):
        self.service = service
        self.driver = driver

    def get(self, url):
        self.driver.get(url)

    def find_element(self, option, value):
        return self.driver.find_element(by=option, value=value)

    def click_on(self, element):
        try:
            element.click()
        except:
            print("Something went wrong")

    def send_keys(self, element, data):
        try:
            element.clear()
            element.send_keys(data)
        except:
            print("Something went wrong")

    def screen(self, name):
        try:
            driver.save_screenshot(name)
        except:
            print("Something went wrong")

chrome_test = Test(service, driver)

def login(option):
    screen_name = option["screen_name"]
    local_driver = option["driver"]
    local_driver.get(option["url"])
    try:
        email = local_driver.find_element(By.CSS_SELECTOR, option["email_selector"])
        password = local_driver.find_element(By.CSS_SELECTOR, option["password-selector"])
        local_driver.send_keys(email, "sly1712@gmail.com")
        local_driver.send_keys(password, "111")
        login_btn = driver.find_element(By.CSS_SELECTOR, option["btn_selector"])
        local_driver.click_on(login_btn)
        sleep(2)
        local_driver.screen(screen_name)
        driver.quit()
    except Exception as error_message:
        print(error_message)
        
login({
    "driver": chrome_test,
    "url": "https://www.instagram.com/",
    "btn_selector": "._acan",
    "email_selector": "input[name = username]",
    "password-selector": "input[name = password]",
    "screen_name": "image" + str(random.randint(1, 1000)) + ".png"
})
sleep(20)
