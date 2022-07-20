import requests
from hyper.contrib import HTTP20Adapter
import urllib.request
import urllib.parse
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Accept':' */*',
    # 'Accept-Encoding':' gzip, deflate, br', # 爬虫时需要注释掉 否则解析不了
    # 'Accept-Language':' zh-CN,zh;q=0.9',
    # 'Connection':' keep-alive',
    # 'Content-Length':' 132',
    # 'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
    # 这里面有个反爬机制就是cookie
    # 'Host':' fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Referer': 'https://fanyi.baidu.com/',
    # 'Sec-Fetch-Dest':' empty',
    # 'Sec-Fetch-Mode':' cors',
    # 'Sec-Fetch-Site':' same-origin',
    # 'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    # 'X-Requested-With':' XMLHttpRequest',
    'cookie': '_ga=GA1.2.551302045.1605795899; MONITOR_WEB_ID=e13c8a50-1e38-485d-8613-1231cea2d348; __tea_cookie_tokens_2608=%257B%2522web_id%2522%253A%25226896840858072679944%2522%252C%2522ssid%2522%253A%252219d32df5-c911-45fa-bd72-473ad62638fe%2522%252C%2522user_unique_id%2522%253A%25226896840858072679944%2522%252C%2522timestamp%2522%253A1626618792231%257D; n_mh=BV0owX9ixhphmaHMNVQVPonmbSBXtFmvd2f8rcwIUQo; _gid=GA1.2.491979819.1658156701; passport_csrf_token=e5ca6c47f2fb161a0af185ef00b59404; passport_csrf_token_default=e5ca6c47f2fb161a0af185ef00b59404; _tea_utm_cache_2018=undefined; sid_guard=358c1a22b6a442089f69e9019f6b905c%7C1658159783%7C31536000%7CTue%2C+18-Jul-2023+15%3A56%3A23+GMT; uid_tt=322c4cdf7b38ab4af9c7bdcc56b4534b; uid_tt_ss=322c4cdf7b38ab4af9c7bdcc56b4534b; sid_tt=358c1a22b6a442089f69e9019f6b905c; sessionid=358c1a22b6a442089f69e9019f6b905c; sessionid_ss=358c1a22b6a442089f69e9019f6b905c; sid_ucp_v1=1.0.0-KDFmODUxZjAxYzA5MDc1MmE4Njc0NGNlMWRhYzVmNzM4MDAzYjgwYmMKFwiHq8C-_fXxBxCnhdaWBhiwFDgBQOoHGgJsZiIgMzU4YzFhMjJiNmE0NDIwODlmNjllOTAxOWY2YjkwNWM; ssid_ucp_v1=1.0.0-KDFmODUxZjAxYzA5MDc1MmE4Njc0NGNlMWRhYzVmNzM4MDAzYjgwYmMKFwiHq8C-_fXxBxCnhdaWBhiwFDgBQOoHGgJsZiIgMzU4YzFhMjJiNmE0NDIwODlmNjllOTAxOWY2YjkwNWM; _tea_utm_cache_2608={%22utm_source%22:%22gold_browser_extension%22}'
}

class SpiderProcessor:
    def __init__(self, aid, uuid, section_url, content_url):
        self.aid = aid
        self.uuid = uuid
        self.section_url = section_url
        self.content_url = content_url
        self.book_name = 'test'

    def send_post(self, url, data):

        data = urllib.parse.urlencode(data).encode("utf-8")

        request = urllib.request.Request(url=url, data=data, headers=headers)

        response = urllib.request.urlopen(request)

        content = response.read().decode('utf-8')

        res_data = json.loads(content)

        return res_data

    def run_proccessor(self):
        section_infos = self.get_sections()
        self.get_content(section_infos)

    # 获取所有目录id
    def get_sections(self):
        data = {
            'booklet_id': '7069596046602534919'
        }
        res_data = self.send_post(self.section_url, data)
        section_infos = res_data['data']['sections']
        print(section_infos)
        return section_infos

    def get_content_post(self, url, data):
        h = {
                'authority': 'api.juejin.cn',
                'method': 'POST',
                'path': '/booklet_api/v1/section/get?aid=2608&uuid=6971404364696356363',
                'referer': 'https://juejin.cn/book/7069596046602534919/section/7070419009790803976',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                'Accept': '*/*',
                'cookie': '_ga=GA1.2.360991426.1623156544;MONITOR_WEB_ID=0999e81c-2642-499a-8019-2731b77809ae; __tea_cookie_tokens_2608=%257B%2522web_id%2522%253A%25226971404364696356363%2522%252C%2522ssid%2522%253A%252219d32df5-c911-45fa-bd72-473ad62638fe%2522%252C%2522user_unique_id%2522%253A%25226971404364696356363%2522%252C%2522timestamp%2522%253A1626180142798%257D; n_mh=BV0owX9ixhphmaHMNVQVPonmbSBXtFmvd2f8rcwIUQo; sid_guard=a5d1690b11b175795ad0781137e45aa5%7C1652690627%7C31536000%7CTue%2C+16-May-2023+08%3A43%3A47+GMT; uid_tt=372262f5d6462eef2a4a09648c188301; uid_tt_ss=372262f5d6462eef2a4a09648c188301; sid_tt=a5d1690b11b175795ad0781137e45aa5; sessionid=a5d1690b11b175795ad0781137e45aa5; sessionid_ss=a5d1690b11b175795ad0781137e45aa5; sid_ucp_v1=1.0.0-KDFhMzIyMzg2OTczZjBhMmRmZmNjMWNmMDI3NWFiNWZiODIxZDkxOWQKFwiHq8C-_fXxBxDDnYiUBhiwFDgCQPEHGgJsZiIgYTVkMTY5MGIxMWIxNzU3OTVhZDA3ODExMzdlNDVhYTU; ssid_ucp_v1=1.0.0-KDFhMzIyMzg2OTczZjBhMmRmZmNjMWNmMDI3NWFiNWZiODIxZDkxOWQKFwiHq8C-_fXxBxDDnYiUBhiwFDgCQPEHGgJsZiIgYTVkMTY5MGIxMWIxNzU3OTVhZDA3ODExMzdlNDVhYTU; _tea_utm_cache_6587={%22utm_source%22:%22jj_nav%22}; _gid=GA1.2.1656713202.1658108910; _tea_utm_cache_2608={%22utm_source%22:%22gold_browser_extension%22}'
            }

        data = urllib.parse.urlencode(data).encode("utf-8")

        request = urllib.request.Request(url=url, data=data, headers=h)

        response = urllib.request.urlopen(request)

        content = response.read().decode('utf-8')
        print(content)

        res_data = json.loads(content)

        return res_data

    # 获取内容
    def get_content(self, section_infos):
        with open(self.book_name.strip('"') + ".html", 'a', encoding="utf-8") as html:
            html.writelines('<meta charset="UTF-8">')

        # headers['content-type'] = 'application/json'
        # headers['referer'] = 'https://juejin.cn/book/7069596046602534919/section/7070419009790803976'
        for item in section_infos:
            data = {
                'section_id': item['section_id']
            }
            # res_data = self.send_post(self.content_url, data)
            res_data = self.get_content_post(self.content_url, data)
            print(item['title'], res_data)
            section_info = res_data['data']['section']

            html_content = section_info['content']
            md_content = section_info['markdown_show']
            # file_html_name = '%s.html'%(item['title'])
            # with open(file_html_name, 'w') as file:
            #     file.write(html_content)

            with open(self.book_name.strip('"')+".html", 'a', encoding="utf-8") as file:
                file.writelines(html_content)