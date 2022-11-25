"""
网上有位同学总结的资源很好，这里爬取下本地保存，不传播
https://learn.lianglianglee.com/
"""
import requests
import html2text
import misaka
import os
from bs4 import BeautifulSoup
from urllib.parse import unquote

base_url = 'https://learn.lianglianglee.com'
headers = {
    'cookie': '_ga=GA1.1.1142663693.1669259949; __gads=ID=05519a927d0b2d15-22758b889fd80099:T=1669259987:RT=1669259987:S=ALNI_MZe1W23-3MMgHAJqhKq6GWUVMHUrA; __gpi=UID=00000b823fa5e98a:T=1669259987:RT=1669354802:S=ALNI_MbG-8BrUV1edPu4i-ZO836XYhs-Ow; _ga_NPSEEVD756=GS1.1.1669354763.4.1.1669355612.10.0.0; lastPath=/%E4%B8%93%E6%A0%8F/Redis%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%98'
}


class Spider:
    def __init__(self):
        pass

    def exec(self, url, filename):

        self.mkdir(filename)

        # 请求获取导航内容
        res = requests.get(url=url, verify=False, headers=headers)
        content = res.content.decode("utf-8")
        # 将导航内容转为md内容
        markdown = html2text.html2text(content)
        print(markdown)

        # 解析获取md导航目录
        dir_name_list = self.get_index_dir(markdown)

    def download_md(self, dir_name, top_dir_name):
        url = base_url + dir_name
        res = requests.get(url=url, verify=False, headers=headers)
        content = res.content.decode("utf-8")
        markdown = html2text.html2text(content)


        md_file_name = "%s.md" % (dir_name[:dir_name.rindex("/")])
        file_name = top_dir_name + "/" +md_file_name
        with open(file_name, 'a', encoding="utf-8") as md_file:
            md_file.writelines(markdown)


    def get_index_dir(self, md_content):
        md_render = misaka.Markdown(misaka.HtmlRenderer())
        html = md_render(md_content)
        soup = BeautifulSoup(html, features='html.parser')
        dir_name_list = []
        for dir_item in soup.find_all('a'):
            dir_url = dir_item.get('href')
            dir_name = unquote(dir_url)
            print(dir_name)
            dir_name_list.append(dir_name)

    def mkdir(self, dir_name):
        folder = os.path.exists(dir_name)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(dir_name)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print("创建目录成功")
        else:
            print("---  There is this folder!  ---")


if __name__ == '__main__':
    spider = Spider()
    url = "https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Redis%20%E6%A0%B8%E5%BF%83%E5%8E%9F%E7%90%86%E4%B8%8E%E5%AE%9E%E6%88%98"
    filename = "Redis核心原理与实战"
    spider.exec(url, filename)
