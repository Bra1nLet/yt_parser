import time
from selenium.webdriver.common.by import By
from undetected_chromedriver import Chrome

from src.selectors.login_selectors import login_selectors


class Login:
    def __init__(self, browser: Chrome, mail, password, recovery_mail):
        self.driver = browser
        self.mail = mail
        self.password = password
        self.recovery_mail = recovery_mail
        self.page = "https://youtube.com"

    def login(self):
        self.driver.save_screenshot("get_there.png")
        print("getting to yt")
        self.driver.get(self.page)
        print("accepting terms")
        self.driver.save_screenshot("get_there2.png")
        try:
            self.click(login_selectors.accept_terms_usage)
            time.sleep(3)
        except:
            pass
        try:
            self.click(login_selectors.open_login_page_button)
            time.sleep(3)

            mail_form = self.driver.find_element(By.CSS_SELECTOR, login_selectors.input_form)
            mail_form.send_keys(self.mail)

            self.click(login_selectors.login_button)
            time.sleep(5)
        except:
            pass

        captcha_solved = False
        while not captcha_solved:
            try:
                password_form = self.driver.find_element(By.CSS_SELECTOR, login_selectors.input_form)
                password_form.send_keys(self.password)
                captcha_solved = True
                self.click(login_selectors.login_button)
            except:
                return False

        time.sleep(4)
        try:
            self.click(login_selectors.submit_account)
            time.sleep(5)
            submit_form = self.driver.find_element(By.CSS_SELECTOR, login_selectors.input_form)
            submit_form.send_keys(self.recovery_mail)
            time.sleep(1)
            self.click(login_selectors.login_button)
            time.sleep(4)
        except:
            pass

        print("finally")
        try:
            print("trying to click")
            self.click(login_selectors.not_now)
        except:
            print("-------no-------")
            return False
        time.sleep(10)

        return True

    def click(self, selector):
        login_btn = self.driver.find_element(By.CSS_SELECTOR, selector)
        login_btn.click()
