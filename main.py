from typing import List
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyotp
import asyncio

class Driver:
    
    driver: webdriver.Chrome
    
    def __init__(self) -> None:
        self.set_driver()
    
    def set_driver(self):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        options.add_argument('--disable-blink-features=AutomationControlled')
            
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        # options.add_argument("start-maximized")
                
        options.add_argument("--disable-extensions")
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-features=ChromeWhatsNewUI")
        self.driver = webdriver.Chrome(service=service, options=options)
        return self.driver
    
    def insert_username(self):
        url = "https://www.bhinneka.com"
        self.driver.get(url)
        login = self.driver.find_element(By.CLASS_NAME, "css-1avegbk")
        login.click()
        
    async def login(self):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.insert_username)
        # self.driver.get("https://www.bhinneka.com")
        # login = self.driver.find_element(By.CLASS_NAME, "css-1avegbk")
        # login.click()
        # wait = WebDriverWait(driver, 5)
        # login = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "css-1avegbk")))
    

    
    
async def main():
    tasks = []
    for i in range(0,2):
        driver = Driver()
        task = asyncio.create_task(driver.login())
        tasks.append(task)
    return asyncio.gather(tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())    
    
    
# def create_driver():
#     service = Service(ChromeDriverManager().install())
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     options.add_argument('--disable-blink-features=AutomationControlled')
        
#     options.add_argument("--incognito")
#     options.add_argument("--disable-notifications")
#     # options.add_argument("start-maximized")
            
#     options.add_argument("--disable-extensions")
#     options.add_experimental_option('useAutomationExtension', False)
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_argument("--disable-features=ChromeWhatsNewUI")
#     driver = webdriver.Chrome(service=service, options=options)
#     return driver    

# async def open_google():
#     driver = create_driver()
#     driver.get("https://www.bhinneka.com")
#     # wait = WebDriverWait(driver, 5)
#     login = driver.find_element(By.CLASS_NAME, "css-1avegbk")
#     # login = wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "css-1avegbk")))
#     login.click()
    