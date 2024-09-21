class VideoSelectors:
    def __init__(self):
        self.subscribe_button = "div.page-header-view-model-wiz__page-header-content yt-subscribe-button-view-model"
        self.like_button = "div#actions segmented-like-dislike-button-view-model.YtSegmentedLikeDislikeButtonViewModelHost"
        self.comment_remember_button = "tp-yt-paper-dialog div.yt-spec-touch-feedback-shape__fill"
        self.check_auth_selector = 'ytd-masthead yt-button-shape'
        self.comment_input = "ytd-comment-simplebox-renderer div.style-scope.ytd-comment-simplebox-renderer#placeholder-area yt-formatted-string"
        self.comment_send_button = "div.style-scope.ytd-commentbox div#buttons ytd-button-renderer#submit-button button.yt-spec-button-shape-next.yt-spec-button-shape-next--filled.yt-spec-button-shape-next--call-to-action.yt-spec-button-shape-next--size-m"

        self.shorts_like = "div#like-button label.yt-spec-button-shape-with-label div.yt-spec-touch-feedback-shape__fill"

        self.comment_reply = "ytd-comments#comments ytd-comment-thread-renderer ytd-button-renderer#reply-button-end button"
        self.comment_reply_input = "ytd-comments#comments ytd-comment-thread-renderer yt-formatted-string div#contenteditable-root"
        self.comment_reply_send = "ytd-comments#comments ytd-comment-thread-renderer div#buttons ytd-button-renderer#submit-button"

        self.comment_like_btn = "ytd-comments#comments ytd-comment-thread-renderer ytd-toggle-button-renderer#like-button button"

        self.community_like_btn = "ytd-toggle-button-renderer#like-button button"

        self.community_comment_btn = 'div#placeholder-area yt-formatted-string'

        self.community_comment_reply_btn = "ytd-button-renderer#reply-button-end yt-button-shape button"
        self.community_comment_reply_input = "div.input-wrapper.style-scope.tp-yt-paper-input-container yt-formatted-string div#contenteditable-root"
        self.community_comment_send = "ytd-button-renderer#submit-button button"

        self.community_comment_like = "ytd-comment-engagement-bar ytd-toggle-button-renderer#like-button button"





video_selectors = VideoSelectors()
