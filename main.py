# coding=utf-8
import requests
import base64
import time
from Utils import *
from config import *
from chaojiying import get_verify_code

session = requests.session()


# class WestenWorld:
#     def __init__(self):
#         self.session = requests.session()
#         self.csrftoken = str()
#         self.verify_code = str()
#         self.check_data = {'email': email, 'csrf_token': csrf_token, 'verify_code': verify_code}
#         self.regist_data = {
#             'email': email,
#             'password': psd,
#             'inviter_email': None,
#             'agree_terms': 1,
#             'device_id': None,
#             'regist_is_app': 0
#         }
#
#     def get_csrftoken(self):
#         login_html = session.get(login_url, headers=headers).text
#         self.csrftoken = get_csrftoken(re.findall(r"window.init_text = '(.*?)'", login_html)[0])
#         print("csrf_token:", self.csrf_token)
#
#     def verify(self):
#         resp = session.get(verify_url, headers=headers)
#         with open('verify.jpg', 'wb') as f:
#             f.write(resp.content)
#         self.verify_code = get_verify_code('verify.jpg')
#         print("verify_code:", self.verify_code)
#         resp = session.post(check_url, headers=headers, data=self.check_data)
#         print(resp.text)
#
#     def regist(self):
#         resp = session.post(url=regist_url, headers=headers, data=self.regist_data)
#         print(resp.text)


# 第一步---打开网页，保存cookie
Login_Html = session.get(login_url, headers=headers).text
csrf_token = get_csrftoken(re.findall(r"window.init_text = '(.*?)'", Login_Html)[0])
print("csrf_token:", csrf_token)

# 第二步---请求验证码
verify = session.get(verify_url, headers=headers)
with open('verify.jpg', 'wb') as f:
    f.write(verify.content)
verify_code = get_verify_code('verify.jpg')
print("verify_code:", verify_code)

""""-----------------------------------------------------------------------------------------------------------------"""
check_data = {'email': email, 'csrf_token': csrf_token, 'verify_code': verify_code}
regist_data = {
    'email': email,
    'password': psd,
    'inviter_email': None,
    'agree_terms': 1,
    'device_id': None,
    'regist_is_app': 0
}
"""------------------------------------------------------------------------------------------------------------------"""

# 第三步---打码验证，注册cookie
check = session.post(check_url, headers=headers, data=check_data)
print(check.text)

# 第四步----POST注册接口注册
regist = session.post(url=regist_url, headers=headers, data=regist_data)
print(regist.text)

# 第五步---节点HTML
node_html = session.get(node_url).text
# print(node_html)

# 取高速全部节点
node = re.findall(r'node_data: (.*?),\n};', node_html)[0]
Trojan_url = get_fatest(node) + "#" + time.strftime("%m-%d %H:%M:%S", time.localtime()) + "\n"
print(Trojan_url)

# 提交订阅
subscribe = base64.b64encode(Trojan_url.encode('utf-8')).decode(encoding='utf-8')
with open('subscribe/trojan.txt', 'w') as f:
    f.write(str(subscribe))
#git_push()
