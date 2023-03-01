import time
import random
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
            options.add_argument(f'user-agent={user_agent}')
            driver = webdriver.Chrome(chrome_options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.get(url)
            time.sleep(10)
            
            return driver
            
        except Exception as ex:
            print(ex)  
            return None
        
    @staticmethod
    def login(driver, email, password):
        try:
            email_input = driver.find_element(By.CSS_SELECTOR, "input[name = username]")
            password_input = driver.find_element(By.CSS_SELECTOR, "input[name = password]")
            
            email_input.send_keys(email)
            password_input.send_keys(password)

            login_button = driver.find_element(By.CSS_SELECTOR, "._acan")

            login_button.click()
            time.sleep(10)

            return True
            
        except Exception as ex:
            print(ex)
            return False
        
    @staticmethod
    def login_cycle(url, email_list, password_list):
        driver = Test.driver_installer(url)
        if driver is None:
            return
        
        for i in range(len(email_list)):
            email = email_list[i]
            password = password_list[i]
            
            if Test.login(driver, email, password):
                
                driver.save_screenshot("image" + str(random.randint(1, 1000)) + ".png")
                
                print(f'Successful login with email {email} and password {password}')
                # driver.save_screenshot(f'successful_login_{email}.png')
                driver.refresh()
                break
            else:
                driver.save_screenshot("image" + str(random.randint(1, 1000)) + ".png")
                
                print(f'Login failed with email {email} and password {password}')
                driver.refresh()
        
        driver.close()
        driver.quit()
        
test = Test()
test.login_cycle("https://www.instagram.com/", 
        [
        "lidashkvarla", 
        "email2"
        ],
        [
        "idi1712", 
        "password2"
        ])
