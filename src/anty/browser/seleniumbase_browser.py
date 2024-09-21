from seleniumbase import Driver
from seleniumbase import undetected
from seleniumbase import webdriver
from src.config import PATH_TO_PROFILES, PATH_TO_PROXY_FOLDER, PATH_TO_BROWSER_EXE
from src.models.proxy import Proxy


class Browser:
    def __init__(self, profile_id: str, proxy: Proxy):
        self.profile_id = profile_id
        self.proxy = proxy

    def get_browser(self):
        driver = Driver(
            browser="chrome",
            headless=False,
            uc=True,
            user_data_dir=f"{PATH_TO_PROFILES}/{self.profile_id}",
            binary_location=PATH_TO_BROWSER_EXE
        )

        return driver
