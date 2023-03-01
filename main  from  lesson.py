import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

class Test:
    def __init__(self):
        pass
    
    @staticmethod
    def driver_installer (url):
        try:
            ua = UserAgent()
            op = webdriver.ChromeOptions()
            op.add_argument(f"user-agent={ua}")
            op.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)" 
                            + "AppleWebKit/537.36 (KHTML, like Gecko)" 
                            + "Chrome/87.0.4280.141 Safari/537.36")            
            driver = webdriver.Chrome(options=op, service=ChromeService(ChromeDriverManager().install()))
            # driver.add_cookie({"name": "John", "surname": "Doe", "age": "20"})
            driver.get(url)
            time.sleep(20)
        except Exception as ex:
            print(ex)  
        finally:
            driver.close()
            driver.quit()

Test.driver_installer("https://www.whatsmybrowser.org/")              
            
#             driver.save_screenshot("image" + str(random.randint(1, 1000)) + ".png")
# Test.driver_installer("https://comfy.ua/ua/")

