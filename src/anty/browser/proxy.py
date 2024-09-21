import os
from src.config import PATH_TO_PROXY_FOLDER

def add_proxy(scheme, host, port, username, password, proxy_id):
    manifest_json = """{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
    """

    background_js = """var config = {
    mode: "fixed_servers",
    rules: {
    singleProxy: {
        scheme: "%s",
        host: "%s",
        port: parseInt(%s)
    },
    bypassList: ["localhost"]
    }
};

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);""" % (scheme, host, port, username, password)
    os.mkdir(f"{PATH_TO_PROXY_FOLDER}/{proxy_id}")
    with open(f"{PATH_TO_PROXY_FOLDER}/{proxy_id}/manifest.json", "w") as f:
        f.write(manifest_json)
    with open(f"{PATH_TO_PROXY_FOLDER}/{proxy_id}/background.js", "w") as f:
        f.write(background_js)
