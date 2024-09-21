import undetected_chromedriver as uc
from src.config import PATH_TO_PROFILES, PATH_TO_BROWSER_EXE, PATH_TO_DRIVER, PATH_TO_PROXY_FOLDER
from src.models.proxy import Proxy

class Browser:
    def __init__(self, profile_id: str, proxy: Proxy):
        self.profile_id = profile_id
        self.proxy = proxy

    def get_browser(self):
        options = uc.ChromeOptions()

        if self.proxy.username and self.proxy.password:
            options.add_argument(f"--load-extension={PATH_TO_PROXY_FOLDER}/{self.proxy.id}")
        else:
            options.add_argument(f'--proxy-server={self.proxy.scheme}://{self.proxy.host}:{self.proxy.port}')

        driver = uc.Chrome(
            driver_executable_path=PATH_TO_DRIVER,
            browser_executable_path=PATH_TO_BROWSER_EXE,
            user_data_dir=f"{PATH_TO_PROFILES}/{self.profile_id}",
            options=options,
            headless=True
        )
        return driver
