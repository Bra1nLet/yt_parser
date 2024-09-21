class LoginSelectors:
    def __init__(self):
        self.open_login_page_button = "div.style-scope.ytd-masthead a.yt-spec-button-shape-next.yt-spec-button-shape-next--outline.yt-spec-button-shape-next--call-to-action.yt-spec-button-shape-next--size-m.yt-spec-button-shape-next--icon-leading"
        self.cookies_form = "div#content.style-scope.ytd-consent-bump-v2-lightbox"
        self.accept_cookies_buttons = (
            self.cookies_form
            + " div.eom-button-row.style-scope.ytd-consent-bump-v2-lightbox ytd-button-renderer.style-scope.ytd-consent-bump-v2-lightbox button.yt-spec-button-shape-next.yt-spec-button-shape-next--filled.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m"
        )
        self.accept_terms_usage = "tp-yt-paper-dialog div.eom-button-row.style-scope.ytd-consent-bump-v2-lightbox yt-button-shape button"
        self.input_form = "input.whsOnd.zHQkBf"
        self.login_button = "button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.BqKGqe.Jskylb.TrZEUc.lw1w4b"
        self.submit_account = "ul.Dl08I li:nth-child(n+3) div"
        self.not_now = "span.VfPpkd-vQzf8d"


login_selectors = LoginSelectors()
