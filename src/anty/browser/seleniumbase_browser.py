from seleniumbase import Driver
from src.config import PATH_TO_PROFILES, PATH_TO_BROWSER_EXE
from src.models.proxy import Proxy
from src.selectors.login_selectors import login_selectors


class Browser:
    def __init__(self, profile_id: str, proxy: Proxy):
        self.profile_id = profile_id
        self.proxy = f"{proxy.scheme}://{proxy.host}:{proxy.port}"

    def get_browser(self):
        driver = Driver(
            browser="chrome",
            uc=True,
            user_data_dir=f"{PATH_TO_PROFILES}/{self.profile_id}",
            binary_location=PATH_TO_BROWSER_EXE,
            proxy=self.proxy
        )
        return driver


# b = Browser("1202140184012", Proxy(scheme="socks5", host="57.129.12.240", port="64021", country="Chinas"))
# browser= b.get_browser()
# browser.open("https://youtube.com")
# browser.save_screenshot()
# browser.click(login_selectors.accept_terms_usage)
# browser.quit()