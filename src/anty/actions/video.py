import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from src.selectors.video_selectors import video_selectors

class Video:
    def __init__(self, action_url, browser: uc.Chrome):
        self.url = "https://youtube.com"
        self.action_url = action_url
        self.browser = browser

    def check_auth(self):
        self.browser.get(self.url)
        try:
            element = self.browser.find_element(By.CSS_SELECTOR, 'a[aria-label="Sign in"]')
            if element:
                return False
        except:
            pass
        return True

    def video_like(self):
        self.browser.get(self.action_url)
        time.sleep(1)
        self.click(video_selectors.like_button)
        time.sleep(1)
        self.browser.get(self.url)

    def video_comment(self, message):
        self.browser.get(self.action_url)
        time.sleep(2)
        self.browser.execute_script("""
        window.scroll({
              top: 500,
              behavior: "smooth",
            });
        """)
        time.sleep(3)
        comment_field = self.browser.find_element(By.CSS_SELECTOR, video_selectors.comment_input)
        comment_field.send_keys(message)
        time.sleep(0.5)
        self.click(video_selectors.comment_send_button)
        time.sleep(1)
        try:
            self.click(video_selectors.comment_remember_button)
            time.sleep(1)
            self.click(video_selectors.comment_send_button)
            time.sleep(1)
        except:
            pass
        self.browser.get(self.url)

    def video_comment_reply(self, message):
        self.browser.get(self.action_url)
        time.sleep(2)
        self.browser.execute_script("""
                window.scroll({
                      top: 500,
                      behavior: "smooth",
                    });
                """)
        time.sleep(3)
        self.click(video_selectors.comment_reply)
        time.sleep(0.5)
        comment_field = self.browser.find_element(By.CSS_SELECTOR, video_selectors.comment_reply_input)
        comment_field.send_keys(message)
        time.sleep(0.5)
        self.click(video_selectors.comment_reply_send)
        time.sleep(1)
        try:
            self.click(video_selectors.comment_remember_button)
            time.sleep(1)
            self.click(video_selectors.comment_reply_send)
            time.sleep(1)
        except:
            pass
        self.browser.get(self.url)

    def comment_like(self):
        self.browser.get(self.action_url)
        time.sleep(2)
        self.browser.execute_script("""
                        window.scroll({
                              top: 500,
                              behavior: "smooth",
                            });
                        """)
        time.sleep(3)
        self.click(video_selectors.comment_like_btn)
        time.sleep(1)
        self.browser.get(self.url)

    def shorts_like(self):
        self.browser.get(self.action_url)
        time.sleep(1)
        self.click(video_selectors.shorts_like)
        time.sleep(1)
        self.browser.get(self.url)

    def community_like(self):
        self.browser.get(self.action_url)
        time.sleep(2)
        self.click(video_selectors.community_like_btn)
        time.sleep(1)
        self.browser.get(self.url)

    def community_comment_like(self):
        self.browser.get(self.action_url)
        time.sleep(1)
        self.click(video_selectors.community_comment_like)
        time.sleep(1)
        self.browser.get(self.url)

    def community_comment(self, message):
        self.browser.get(self.action_url)
        time.sleep(2)
        comment_field = self.browser.find_element(By.CSS_SELECTOR, video_selectors.community_comment_btn)
        comment_field.send_keys(message)
        time.sleep(0.5)
        self.click(video_selectors.community_comment_send)
        time.sleep(2)
        try:
            self.click(video_selectors.comment_remember_button)
            time.sleep(1)
            self.click(video_selectors.community_comment_send)
            time.sleep(1)
        except:
            pass
        self.browser.get(self.url)

    def community_comment_reply(self, message):
        self.browser.get(self.action_url)
        time.sleep(2)
        self.click(video_selectors.community_comment_reply_btn)
        time.sleep(0.5)
        comment_field = self.browser.find_element(By.CSS_SELECTOR, video_selectors.community_comment_reply_input)
        comment_field.send_keys(message)
        time.sleep(0.5)
        self.click(video_selectors.community_comment_send)
        time.sleep(2)
        try:
            self.click(video_selectors.comment_remember_button)
            time.sleep(1)
            self.click(video_selectors.community_comment_send)
            time.sleep(2)
        except:
            pass
        self.browser.get(self.url)

    def community_vote(self, option):
        selector = f"tp-yt-paper-listbox a#sign-in:nth-child(n+{option})"
        self.browser.get(self.action_url)
        time.sleep(2)
        self.click(selector)
        time.sleep(1)
        self.browser.get(self.url)


    def click(self, selector):
        element = self.browser.find_element(By.CSS_SELECTOR, selector)
        element.click()

    def close(self):
        self.browser.close()
