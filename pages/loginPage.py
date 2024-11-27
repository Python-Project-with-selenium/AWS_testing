from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.utils import Util_Test


class Login_Page:
    def __init__(self, driver):
        self.driver = driver
        self.utils = Util_Test(driver)
        self.user_name = "//input[@data-qa='username']"
        self.submit_userName = "button[data-qa='submit-username']"
        self.password = "input[data-qa='password']"
        self.submit_password = "button[data-qa='submit-password']"
        self.home_page_title = "header-home-desktop"
        self.start_button = "button[data-qa='manage-sidebar-actions-ndse-trigger']"

    def login_page(self, userName, password, screenshot=False):
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name))).send_keys(userName)
        self.driver.find_element(By.CSS_SELECTOR, self.submit_userName).click()
        password = Util_Test.password_decrypt(password)
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.password))).send_keys(password)
        if screenshot:
            self.utils.getscreenshot('/3.2.Authentication_required.png')
        self.driver.find_element(By.CSS_SELECTOR, self.submit_password).click()