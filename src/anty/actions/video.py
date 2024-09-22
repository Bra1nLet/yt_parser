from seleniumbase import Driver
from src.selectors.video_selectors import video_selectors

class Video:
    def __init__(self, action_url, browser: Driver):
        self.url = "https://youtube.com"
        self.action_url = action_url
        self.browser = browser

    def check_auth(self):
        self.browser.open(self.url)
        try:
            element = self.browser.find_element('a[aria-label="Sign in"]')
            if element:
                return False
        except:
            pass
        return True

    def video_like(self):
        self.browser.open(self.action_url)
        self.browser.sleep(1)
        self.browser.click(video_selectors.like_button)
        self.browser.sleep(1)
        self.browser.open(self.url)

    def video_comment(self, message):
        self.browser.open(self.action_url)
        self.browser.sleep(2)
        self.browser.execute_script("""
        window.scroll({
              top: 500,
              behavior: "smooth",
            });
        """)
        self.browser.sleep(3)
        comment_field = self.browser.find_element(video_selectors.comment_input)
        comment_field.send_keys(message)
        self.browser.sleep(0.5)
        self.browser.click(video_selectors.comment_send_button)
        self.browser.sleep(1)
        try:
            self.browser.click(video_selectors.comment_remember_button)
            self.browser.sleep(1)
            self.browser.click(video_selectors.comment_send_button)
            self.browser.sleep(1)
        except:
            pass
        self.browser.open(self.url)

    def video_comment_reply(self, message):
        self.browser.open(self.action_url)
        self.browser.sleep(2)
        self.browser.execute_script("""
                window.scroll({
                      top: 500,
                      behavior: "smooth",
                    });
                """)
        self.browser.sleep(3)
        self.browser.click(video_selectors.comment_reply)
        self.browser.sleep(0.5)
        comment_field = self.browser.find_element(video_selectors.comment_reply_input)
        comment_field.send_keys(message)
        self.browser.sleep(0.5)
        self.browser.click(video_selectors.comment_reply_send)
        self.browser.sleep(1)
        try:
            self.browser.click(video_selectors.comment_remember_button)
            self.browser.sleep(1)
            self.browser.click(video_selectors.comment_reply_send)
            self.browser.sleep(1)
        except:
            pass
        self.browser.open(self.url)

    def comment_like(self):
        self.browser.open(self.action_url)
        self.browser.sleep(2)
        self.browser.execute_script("""
                        window.scroll({
                              top: 500,
                              behavior: "smooth",
                            });
                        """)
        self.browser.sleep(3)
        self.browser.click(video_selectors.comment_like_btn)
        self.browser.sleep(1)
        self.browser.open(self.url)

    def shorts_like(self):
        self.browser.open(self.action_url)
        self.browser.sleep(1)
        self.browser.click(video_selectors.shorts_like)
        self.browser.sleep(1)
        self.browser.open(self.url)

    def community_like(self):
        self.browser.open(self.action_url)
        self.browser.sleep(2)
        self.browser.click(video_selectors.community_like_btn)
        self.browser.sleep(1)
        self.browser.open(self.url)

    def community_comment_like(self):
        self.browser.open(self.action_url)
        self.browser.sleep(1)
        self.browser.click(video_selectors.community_comment_like)
        self.browser.sleep(1)
        self.browser.open(self.url)

    def community_comment(self, message):
        self.browser.open(self.action_url)
        self.browser.sleep(2)
        comment_field = self.browser.find_element(video_selectors.community_comment_btn)
        comment_field.send_keys(message)
        self.browser.sleep(0.5)
        self.browser.click(video_selectors.community_comment_send)
        self.browser.sleep(2)
        try:
            self.browser.click(video_selectors.comment_remember_button)
            self.browser.sleep(1)
            self.browser.click(video_selectors.community_comment_send)
            self.browser.sleep(1)
        except:
            pass
        self.browser.open(self.url)

    def community_comment_reply(self, message):
        self.browser.open(self.action_url)
        self.browser.sleep(2)
        self.browser.click(video_selectors.community_comment_reply_btn)
        self.browser.sleep(0.5)
        comment_field = self.browser.find_element(video_selectors.community_comment_reply_input)
        comment_field.send_keys(message)
        self.browser.sleep(0.5)
        self.browser.click(video_selectors.community_comment_send)
        self.browser.sleep(2)
        try:
            self.browser.click(video_selectors.comment_remember_button)
            self.browser.sleep(1)
            self.browser.click(video_selectors.community_comment_send)
            self.browser.sleep(2)
        except:
            pass
        self.browser.open(self.url)

    def community_vote(self, option):
        selector = f"tp-yt-paper-listbox a#sign-in:nth-child(n+{option})"
        self.browser.open(self.action_url)
        self.browser.sleep(2)
        self.browser.click(selector)
        self.browser.sleep(1)
        self.browser.open(self.url)

    def close(self):
        self.browser.close()
