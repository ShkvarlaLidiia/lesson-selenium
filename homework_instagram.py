import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Test:
    def __init__(self):
        pass
    
    @staticmethod
    def driver_installer(url):
        try:
            options = Options()
            ua = UserAgent()
            user_agent = ua.random
            print(user_agent)
            options.add_argument(f"user-agent={user_agent}")
            driver = webdriver.Chrome(
                chrome_options=options, 
                service=ChromeService(ChromeDriverManager().install()))
            driver.get(url)
            driver.add_cookie({"name": "John", "value": "Doe"})            
            time.sleep(5)
            return driver
        except Exception as ex:
            print(ex)  
        
    @staticmethod
    def login(url, email_list, password_list):
        try:
            driver = Test.driver_installer(url)
            for i in range(len(email_list)):
                email_input = driver.find_element(By.CSS_SELECTOR, "input[name = username]")
                password_input = driver.find_element(By.CSS_SELECTOR, "input[name = password]")
                email_input.clear()
                password_input.clear()
                j = i+1
                email = email_list[i]
                password = password_list[i]
                email_input.send_keys(email)
                password_input.send_keys(password)
                driver.find_element(By.CSS_SELECTOR, "._acan").click()
                driver.save_screenshot(f"image_{j}.png")
                driver.refresh()
                time.sleep(2)   
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
        
test = Test()
test.login("https://www.instagram.com/", 
        [
        "email1", 
        "email2",
        "email3"
        ],
        [
        "password1", 
        "password2",
        "password3"
        ])