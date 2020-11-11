# coding=utf-8
import random

login_url = 'https://xbsj6147.xyz/portal/account/login'
verify_url = 'https://xbsj6147.xyz/portal/account/get-verify-image'
check_url = 'https://xbsj6147.xyz/user/account/check-is-registed'
regist_url = 'https://xbsj6147.xyz/user/account/regist'
node_url = 'https://xbsj6147.xyz/portal/order/node'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}

email = str(int(random.random() * pow(10, 10))) + "@163.com"
psd = "MirageTest"
