import configparser
from configparser import ExtendedInterpolation

import requests
import urllib3

headers = {
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'cookie': ''
}

hljs_css = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.7.0/styles/github-gist.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.7.0/highlight.min.js"></script>
<script>console.log('hahha');hljs.initHighlightingOnLoad();</script>
'''


class SpiderProcessor:
    def __init__(self):
        self.aid = ''
        self.uuid = ''
        self.section_url = ''
        self.content_url = ''
        self.booklet_id = ''
        self.book_name = ''
        self.load_config()

    def load_config(self):
        cf = configparser.ConfigParser(interpolation=ExtendedInterpolation(),
                                       inline_comment_prefixes=['#', ';'],
                                       allow_no_value=True)
        cf.read('conf.ini')
        self.aid = cf.get("juejin", "aid")
        self.uuid = cf.get("juejin", "uuid")
        self.section_url = cf.get("juejin", "get_section_dir_url")
        self.content_url = cf.get("juejin", "get_section_content_url")
        self.booklet_id = cf.get("juejin", "booklet_id")
        self.book_name = cf.get("juejin", "book_name")
        cookie = cf.get("juejin", "cookie")
        headers['cookie'] = cookie

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

    def remove_special_character(self, file_name):
        if "|" in file_name:
            file_name = file_name.replace("|", "_")
        if "?" in file_name:
            file_name = file_name.replace("?", "")

        return file_name

    # 获取内容
    def get_content(self, section_infos):
        for idx, item in enumerate(section_infos):
            data = {
                'section_id': item['section_id']
            }

            file_name = item['title']
            file_name = file_name.replace('<', ' ')
            file_name = file_name.replace('>', ' ')

            # html文件
            file_html_name = './dist/html/%s.%s.html' % ((idx + 1), file_name)
            file_html_name = self.remove_special_character(file_html_name)

            # markdown 文件
            file_md_name = './dist/md/%s.%s.md' % ((idx + 1), file_name)
            file_md_name = self.remove_special_character(file_md_name)

            with open(file_html_name, 'a', encoding="utf-8") as html:
                html.writelines(hljs_css)
                html.writelines('<meta charset="UTF-8">')

            # 爬取内容
            res_data = self.send_post(self.content_url, data)

            section_info = res_data['data']['section']

            html_content = section_info['content']

            md_content = section_info['markdown_show']

            with open(file_html_name, 'a', encoding="utf-8") as html_file:
                html_file.writelines(html_content)

            # md不为空的情况下再去下载md文件
            if md_content and len(md_content) > 0:
                with open(file_md_name, 'a', encoding="utf-8") as md_file:
                    md_file.writelines(md_content)

            print(item['title'], '处理完毕')


if __name__ == '__main__':
    spider_proccessor = SpiderProcessor()
    spider_proccessor.run_proccessor()
