import requests
import urllib3
import urllib.request
import urllib.parse
import json

headers = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'cookie': '_ga=GA1.2.551302045.1605795899; MONITOR_WEB_ID=e13c8a50-1e38-485d-8613-1231cea2d348; __tea_cookie_tokens_2608=%257B%2522web_id%2522%253A%25226896840858072679944%2522%252C%2522ssid%2522%253A%252219d32df5-c911-45fa-bd72-473ad62638fe%2522%252C%2522user_unique_id%2522%253A%25226896840858072679944%2522%252C%2522timestamp%2522%253A1626618792231%257D; n_mh=BV0owX9ixhphmaHMNVQVPonmbSBXtFmvd2f8rcwIUQo; passport_csrf_token=e5ca6c47f2fb161a0af185ef00b59404; passport_csrf_token_default=e5ca6c47f2fb161a0af185ef00b59404; sid_guard=358c1a22b6a442089f69e9019f6b905c%7C1658159783%7C31536000%7CTue%2C+18-Jul-2023+15%3A56%3A23+GMT; uid_tt=322c4cdf7b38ab4af9c7bdcc56b4534b; uid_tt_ss=322c4cdf7b38ab4af9c7bdcc56b4534b; sid_tt=358c1a22b6a442089f69e9019f6b905c; sessionid=358c1a22b6a442089f69e9019f6b905c; sessionid_ss=358c1a22b6a442089f69e9019f6b905c; sid_ucp_v1=1.0.0-KDFmODUxZjAxYzA5MDc1MmE4Njc0NGNlMWRhYzVmNzM4MDAzYjgwYmMKFwiHq8C-_fXxBxCnhdaWBhiwFDgBQOoHGgJsZiIgMzU4YzFhMjJiNmE0NDIwODlmNjllOTAxOWY2YjkwNWM; ssid_ucp_v1=1.0.0-KDFmODUxZjAxYzA5MDc1MmE4Njc0NGNlMWRhYzVmNzM4MDAzYjgwYmMKFwiHq8C-_fXxBxCnhdaWBhiwFDgBQOoHGgJsZiIgMzU4YzFhMjJiNmE0NDIwODlmNjllOTAxOWY2YjkwNWM; _tea_utm_cache_2608={%22utm_source%22:%22gold_browser_extension%22}; _gid=GA1.2.1212901908.1658765932'
}

hljs_css = '''
<style>.img{max-width: 1400px;}</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.7.0/styles/github-gist.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.7.0/highlight.min.js"></script>
<script>console.log('hahha');hljs.initHighlightingOnLoad();</script>
'''

class SpiderProcessor:
    def __init__(self, aid, uuid, booklet_id, book_name, section_url, content_url):
        self.aid = aid
        self.uuid = uuid
        self.section_url = section_url
        self.content_url = content_url
        self.booklet_id = booklet_id
        self.book_name = book_name

    def send_post(self, url, data):
        urllib3.disable_warnings()
        res = requests.post(url=url, json=data, verify=False, headers=headers)
        return res.json()

    def run_proccessor(self):
        section_infos = self.get_sections()
        self.get_content(section_infos)

    # 获取所有目录id
    def get_sections(self):
        data = {
            'booklet_id': self.booklet_id
        }
        res_data = self.send_post(self.section_url, data)
        section_infos = res_data['data']['sections']

        return section_infos

    # 获取内容
    def get_content(self, section_infos):

        book_html_name = "./dist/html/%s.html" % self.book_name
        with open(book_html_name, 'a', encoding="utf-8") as html:
            html.writelines('<meta charset="UTF-8">')

        for idx, item in enumerate(section_infos):
            data = {
                'section_id': item['section_id']
            }

            # html文件
            file_html_name = './dist/html/%s.%s.html' % ((idx + 1), item['title'])

            # markdown 文件
            file_md_name = './dist/md/%s.%s.md' % ((idx + 1), item['title'])

            with open(file_html_name, 'a', encoding="utf-8") as html:
                html.writelines(hljs_css)
                html.writelines('<meta charset="UTF-8">')

            res_data = self.send_post(self.content_url, data)

            section_info = res_data['data']['section']

            html_content = section_info['content']

            md_content = section_info['markdown_show']

            with open(file_html_name, 'a', encoding="utf-8") as html_file:
                html_file.writelines(html_content)

            with open(file_md_name, 'a', encoding="utf-8") as md_file:
                md_file.writelines(md_content)

            with open(book_html_name, 'a', encoding="utf-8") as htmlf:
                htmlf.writelines(html_content)

            print(item['title'], '处理完毕')
