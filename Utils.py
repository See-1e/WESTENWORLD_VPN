# coding=utf-8
import requests
import execjs
import json
import os
import re


def get_proxies():
    while True:
        try:
            proxy = requests.get("http://101.132.128.215:5010/get/").json().get("proxy")
            test = requests.get('https://xbsj6147.xyz/', proxies={"https": "https://{}".format(proxy)}, timeout=5)
            if test.status_code == 200:
                return proxy
            print(proxy, "Fail to connect")
        except Exception:
            requests.get("http://101.132.128.215:5010/delete/?proxy={}".format(proxy))


def get_csrftoken(init_text):
    with open('JavaScript/csrf.js', 'r') as f:
        code = f.read()
    ctx = execjs.compile(code)
    return ctx.call('get_token', init_text)


def get_fatest(node):
    node_dict = json.loads(node)
    for each in node_dict:
        if node_dict[each]['quick_url_raw']:
            if '<span class="fs-p85 op-p80">上海中转优化</span>' in node_dict[each]['name']:
                return re.findall(r'(.*?)\?.*?', node_dict[each]['quick_url_raw'])[0]


def git_push():
    _str = 'git add subscribe/trojan.txt && git commit -m "update route~" && git push'
    os.system(_str)