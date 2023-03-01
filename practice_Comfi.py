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
    def driver_installer (url):
        try:
            options = Options()
            ua = UserAgent()
            user_agent = ua.random
            print(user_agent)
            options.add_argument(f'user-agent={user_agent}')
            driver = webdriver.Chrome(chrome_options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.get(url)
            driver.add_cookie({"name": "John", "value": "Doe"})            
            btn = driver.find_element(By.CSS_SELECTOR, ".header-bottom-cart")
            btn.click()
            time.sleep(5)
            driver.save_screenshot("screenshot.png")     
        except Exception as ex:
            print(ex)  
        finally:
            driver.close()
            driver.quit()
            
Test.driver_installer("https://comfy.ua/ua/")




