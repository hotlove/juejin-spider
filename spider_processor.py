import requests
import urllib3
import urllib.request
import urllib.parse
import json

headers = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'cookie': '_ga=GA1.2.360991426.1623156544; MONITOR_WEB_ID=0999e81c-2642-499a-8019-2731b77809ae; __tea_cookie_tokens_2608=%257B%2522web_id%2522%253A%25226971404364696356363%2522%252C%2522ssid%2522%253A%252219d32df5-c911-45fa-bd72-473ad62638fe%2522%252C%2522user_unique_id%2522%253A%25226971404364696356363%2522%252C%2522timestamp%2522%253A1626180142798%257D; n_mh=BV0owX9ixhphmaHMNVQVPonmbSBXtFmvd2f8rcwIUQo; sid_guard=a5d1690b11b175795ad0781137e45aa5%7C1652690627%7C31536000%7CTue%2C+16-May-2023+08%3A43%3A47+GMT; uid_tt=372262f5d6462eef2a4a09648c188301; uid_tt_ss=372262f5d6462eef2a4a09648c188301; sid_tt=a5d1690b11b175795ad0781137e45aa5; sessionid=a5d1690b11b175795ad0781137e45aa5; sessionid_ss=a5d1690b11b175795ad0781137e45aa5; sid_ucp_v1=1.0.0-KDFhMzIyMzg2OTczZjBhMmRmZmNjMWNmMDI3NWFiNWZiODIxZDkxOWQKFwiHq8C-_fXxBxDDnYiUBhiwFDgCQPEHGgJsZiIgYTVkMTY5MGIxMWIxNzU3OTVhZDA3ODExMzdlNDVhYTU; ssid_ucp_v1=1.0.0-KDFhMzIyMzg2OTczZjBhMmRmZmNjMWNmMDI3NWFiNWZiODIxZDkxOWQKFwiHq8C-_fXxBxDDnYiUBhiwFDgCQPEHGgJsZiIgYTVkMTY5MGIxMWIxNzU3OTVhZDA3ODExMzdlNDVhYTU; _tea_utm_cache_2608={%22utm_source%22:%22gold_browser_extension%22}; _gid=GA1.2.869846383.1658715430'
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
