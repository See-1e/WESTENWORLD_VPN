# coding=utf-8
import requests
import base64
import time
from Utils import *
from config import *
from chaojiying import get_verify_code


class WestenWorld:
    def __init__(self, proxies):
        self.session = requests.session()
        self.proxies = proxies
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/65.0.3325.146 Safari/537.36 "
        }
        self.regist_data = {
            'email': email,
            'password': psd,
            'inviter_email': None,
            'agree_terms': 1,
            'device_id': None,
            'regist_is_app': 0
        }
        self.verify_data = {'email': email, 'csrf_token': '', 'verify_code': ''}
        self.trojan_url = str()

    def get_csrftoken(self):
        print("STEP_1——初始化")
        login_html = self.session.get(login_url, headers=self.headers, proxies=self.proxies).text
        self.verify_data['csrf_token'] = get_csrftoken(re.findall(r"window.init_text = '(.*?)'", login_html)[0])
        print("csrf_token:", self.verify_data['csrf_token'])
        return True

    def verify(self):
        print("STEP_2——开始验证")
        resp = self.session.get(verify_url, headers=self.headers, proxies=self.proxies)
        with open('verify.jpg', 'wb') as verify_img:
            verify_img.write(resp.content)
        self.verify_data['verify_code'] = get_verify_code('verify.jpg')
        # print("verify_code:", self.verify_data['verify_code'])
        resp = self.session.post(check_url, headers=self.headers, data=self.verify_data, proxies=self.proxies)
        print(resp.text)
        if resp.json()['data']['has_present']:
            return True

<<<<<<< HEAD
    def regist(self):
        print("STEP_3——开始注册")
        resp = self.session.post(url=regist_url, headers=self.headers, data=self.regist_data, proxies=self.proxies)
        print(resp.text)
        return True

    def get_route(self):
        print("STEP_4——取高速节点")
        resp = self.session.get(node_url)
        route_all = re.findall(r'node_data: (.*?),\n};', resp.text)[0]
        self.trojan_url = get_fatest(route_all) + "#" + time.strftime("%m-%d %H:%M:%S", time.localtime()) + "\n"
        print(self.trojan_url)
=======
# 第一步---打开网页，保存cookie
proxies = {
  "http": "http://58.220.95.30:10174",
  "https": "http://58.220.95.30:10174",
}
Login_Html = session.get(login_url, headers=headers, proxies=proxies).text
csrf_token = get_csrftoken(re.findall(r"window.init_text = '(.*?)'", Login_Html)[0])
print("csrf_token:", csrf_token)

# 第二步---请求验证码
verify = session.get(verify_url, headers=headers, proxies=proxies)
with open('verify.jpg', 'wb') as f:
    f.write(verify.content)
verify_code = get_verify_code('verify.jpg')
print("verify_code:", verify_code)
>>>>>>> ef8a91869cede7eec4290c1fe6b933991ddbe981

    def run(self):
        self.get_csrftoken()
        self.verify()
        self.regist()
        self.get_route()

<<<<<<< HEAD

if __name__ == "__main__":
    ip = get_proxies()
    proxies = {
        "http": "http://" + ip,
        "https": "http://" + ip,
    }
    VPN = WestenWorld(proxies)
    VPN.run()
    subscribe = base64.b64encode(VPN.trojan_url.encode('utf-8')).decode(encoding='utf-8')
    with open('subscribe/trojan.txt', 'w') as f:
        f.write(str(subscribe))
    git_push()
=======
# 第三步---打码验证，注册cookie
check = session.post(check_url, headers=headers, data=check_data, proxies=proxies)
print(check.text)


# 第四步----POST注册接口注册
regist = session.post(url=regist_url, headers=headers, data=regist_data, proxies=proxies)
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
git_push()
>>>>>>> ef8a91869cede7eec4290c1fe6b933991ddbe981
