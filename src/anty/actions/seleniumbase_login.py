from src.selectors.login_selectors import login_selectors
from seleniumbase import Driver


class Login:
    def __init__(self, browser: Driver, mail, password, recovery_mail):
        self.driver = browser
        self.mail = mail
        self.password = password
        self.recovery_mail = recovery_mail
        self.url = "https://youtube.com"

    def login(self):
        self.driver.open(self.url)
        try:
            self.driver.click(login_selectors.accept_terms_usage)
            self.driver.sleep(2)
        except:
            pass
        try:
            self.driver.click(login_selectors.open_login_page_button)
            self.driver.sleep(2)

            mail_form = self.driver.find_element(login_selectors.input_form)
            mail_form.send_keys(self.mail)

            self.driver.click(login_selectors.login_button)
            self.driver.sleep(3)
        except:
            pass

        captcha_solved = False
        while not captcha_solved:
            try:
                password_form = self.driver.find_element(login_selectors.input_form)
                password_form.send_keys(self.password)
                captcha_solved = True
                self.driver.click(login_selectors.login_button)
            except:
                return False

        self.driver.sleep(3)
        try:
            self.driver.click(login_selectors.submit_account)
            self.driver.sleep(4)

            submit_form = self.driver.find_element(login_selectors.input_form)
            submit_form.send_keys("self.recovery_mail")
            self.driver.sleep(1)
            self.driver.click(login_selectors.login_button)
            self.driver.sleep(3)
        except:
            pass

        print("finally")
        try:
            print("trying to click")
            self.driver.click(login_selectors.not_now)
        except:
            print("-------no-------")
        self.driver.sleep(6)
        self.driver.open(self.url)
        return True