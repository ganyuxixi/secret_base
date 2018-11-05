import requests


def paramsDemo():
    # 通过params组合链接

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    payload = {
        'app': 'forum',
        'mod': 'List',
        'act': 'index',
        'class': '462'
    }

    r = requests.get('http://xinsheng.huawei.com/cn/index/guest.html', headers=headers, params=payload)
    print r.url

def cookieDemo():
    # 通过在头传入cookie值模拟登陆

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Cookie': 'your cookie'
    }
    r = requests.get('url', headers=headers)
    print r.text

def dataDemo():
    '''
    使用表单登陆
    session保存登陆后的cookie，下次发请求到登陆后的界面去
    '''

    session = requests.Session()
    data = {
        'username': 'your username',
        'password': 'your password'
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    r = session.post('登陆界面url', data=data, headers=headers)

    rr = session.get('登陆后真正想访问的url', headers=headers)
    print rr.text

def CookieDemo():
    '''
    通过Cookie参数传入cookie
    '''

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    cookie = {
        'Cookie': 'your cookie'
    }
    r = requests.get('url', cookie=cookie, headers=headers)
    print r.text

    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print(r.text)

    # 查看响应内容，response.content返回的字节流数据
    print(r.content)

    # 查看完整url地址
    print(r.url)

    # 查看响应头部字符编码
    print(r.encoding)

    # 查看响应码
    print(r.status_code)

if __name__ == "__main__":
    paramsDemo()
    # cookieDemo()
    # dataDemo()
    # CookieDemo()