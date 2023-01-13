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

class Akun(BaseModel):
    username: str
    password: str
    otp: str
    
class TokopediaDriver:
    driver = webdriver.Chrome
    def __init__(self) -> None:
        self.prepare_webdriver()
    
    def prepare_webdriver(self):
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
            
        # options.add_experimental_option("detach", True)
        options.add_argument("--incognito")
        # options.add_argument("start-maximized")
                
        options.add_argument("--disable-extensions")
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-features=ChromeWhatsNewUI")
        self.driver = webdriver.Chrome(service=service, options = options)
        
    async def login(self, username: str, password: str, otp: str):
        self.driver.get("https://www.tokopedia.com")
        wait = WebDriverWait(self.driver, 10)
        elem = wait.until(EC.visibility_of_element_located((By.XPATH, "//*/button[text()='Masuk']")))
        elem.click()
        
        
        elem = wait.until(EC.visibility_of_element_located((By.ID, 'email-phone')))
        elem.send_keys(username)
        elem = wait.until(EC.visibility_of_element_located((By.ID, 'email-phone-submit')))
        elem.click()
        
        elem = wait.until(EC.visibility_of_element_located((By.ID, 'password-input')))
        elem.send_keys(password)
        
        elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*/span[@aria-label="login-button"]')))
        elem.click()
        
        elem = wait.until(EC.visibility_of_element_located((By.XPATH, "//*/input[@aria-label='otp input']")))
        
        totp = pyotp.TOTP(otp)
        code = totp.now()
        
        elem.send_keys(code)
        
# def main(akuns: List[Akun]):
#     print(akuns)
#     service = Service(ChromeDriverManager().install())
#     options = webdriver.ChromeOptions()
#     # options.add_experimental_option("detach", True)
#     options.add_argument('--disable-blink-features=AutomationControlled')
        
#     options.add_argument("--incognito")
#     options.add_argument("start-maximized")
            
#     options.add_argument("--disable-extensions")
#     options.add_experimental_option('useAutomationExtension', False)
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_argument("--disable-features=ChromeWhatsNewUI")
#     driver = webdriver.Chrome(service=service, options = options)
#     # tasks  = []
#     for akun in akuns:
#         driver.get("https://www.tokopedia.com")
#         wait = WebDriverWait(driver, 10)
#         elem = wait.until(EC.visibility_of_element_located((By.XPATH, "//*/button[text()='Masuk']")))
#         elem.click()
        
        
#         elem = wait.until(EC.visibility_of_element_located((By.ID, 'email-phone')))
#         elem.send_keys(akun.username)
#         elem = wait.until(EC.visibility_of_element_located((By.ID, 'email-phone-submit')))
#         elem.click()
        
#         elem = wait.until(EC.visibility_of_element_located((By.ID, 'password-input')))
#         elem.send_keys(akun.password)
        
#         elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*/span[@aria-label="login-button"]')))
#         elem.click()
        
#         elem = wait.until(EC.visibility_of_element_located((By.XPATH, "//*/input[@aria-label='otp input']")))
        
#         totp = pyotp.TOTP(akun.otp)
#         code = totp.now()
        
#         elem.send_keys(code)
#     return "Success"
#     # return tasks

async def main(akuns: List[Akun]):
    tasks = []
    for akun in [akun1, akun2]:
        driver = TokopediaDriver()
        task = asyncio.create_task(driver.login(akun.username, akun.password, akun.otp))
        tasks.append(task)
    return asyncio.gather(tasks)


def main_thread():
    pass


if __name__ == "__main__":
    
    
    akun1 = Akun(**{
            "username": "muekidmall@tedhuwha.com",
            "password": "Denpasar123",
            "otp": "6MS2QV7X3WRYKISHM3MHVOISZUGVRMVZ"
        })
    akun2 = Akun(
        **{
            "username": "muekidmall@tedhuwha.com",
            "password": "Denpasar123",
            "otp": "6MS2QV7X3WRYKISHM3MHVOISZUGVRMVZ"
        }
    )
    # Parallel(n_jobs=2)(delayed(main(akun))(akun) for akun in [akun1, akun2])
    # tasks = []
    # for akun in [akun1, akun2]:
    #     driver = TokopediaDriver()
    #     task = driver.login(akun.username, akun.password, akun.otp)
    #     tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main([akun1, akun2]))
    # res = (asyncio.gather(main([akun1, akun2])))
    # print(res)