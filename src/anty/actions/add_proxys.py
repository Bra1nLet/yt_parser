from src.models.proxy import Proxy
from requests.exceptions import ConnectTimeout
import requests
import datetime

def add_proxys(proxy_list: list):
    good_proxies_amount= 0
    for proxy in proxy_list:
        p = Proxy.model_validate(proxy)
        if validate_proxy(p):
            p.record_proxy()
            good_proxies_amount += 1
    return good_proxies_amount

def validate_proxy(proxy: Proxy):
    proxies = {
        'http': f'{proxy.scheme}://{proxy.host}:{proxy.port}',
        'https': f'{proxy.scheme}://{proxy.host}:{proxy.port}'
    }

    url = 'https://youtube.com'
    try:
        start_time = datetime.datetime.now()
        response = requests.get(url, proxies=proxies, timeout=8)
        ends = datetime.datetime.now() - start_time
        print(ends.seconds)
        print(response.status_code)
        if response.status_code == 200 and response.reason == "OK":
            return True
        return False
    except ConnectTimeout:
        return False
