# coding=utf-8
import execjs
import json
import os
import re


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
    _str = 'cd subscribe && git add trojan.txt && git commit -m "update route~" && git push'
    os.system(_str)
