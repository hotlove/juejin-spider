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

from md2local import get_all_pic_path, download_pic

base_url = 'https://learn.lianglianglee.com'
headers = {
    'cookie': '__gads=ID=dd378d24759b9527-22542cc8c2d80010:T=1670508864:RT=1670508864:S=ALNI_MaY5T9YM8xZvzLSq5O3ALZGZHt6mw; _ga=GA1.1.1933927052.1670508873; __gpi=UID=00000b8c97bf6144:T=1670508864:RT=1670651940:S=ALNI_MZ33U796aHoCKXbJ8nJniZUp7261A; _ga_NPSEEVD756=GS1.1.1670673166.5.1.1670673236.60.0.0; lastPath=/%E4%B8%93%E6%A0%8F/'
}

requests.packages.urllib3.disable_warnings()


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

        # 解析获取md导航目录
        dir_name_list = self.get_index_dir(markdown)

        # 开始下载各个目录的md文件内容
        for item in dir_name_list:
            self.download_md(item, filename)

    # 开始下载md
    def download_md(self, dir_name, top_dir_name):
        print('处理目录：', dir_name)
        url = base_url + dir_name

        res = requests.get(url=url, verify='../certs.pem', headers=headers)
        content = res.content.decode("utf-8")

        # 获取到的文章内容

        #删除html中的导航栏
        soup = BeautifulSoup(content, features='html.parser')
        tag = soup.find('div', class_='book-sidebar')
        if tag != None:
            tag.decompose()
        markdown = html2text.html2text(str(soup))

        markdown = self.hande_md(dir_name, markdown, top_dir_name)

        md_file_name = "%s" % (dir_name[dir_name.rindex("/") + 1:])

        file_path = top_dir_name + "/" + md_file_name
        with open(file_path, 'w', encoding="utf-8") as md_file:
            md_file.writelines(markdown)

    # 解析md文件并将文件下载至本地保存起来
    def hande_md(self, image_parent_url, md_content, parent_dir):
        parent_uri = image_parent_url[:image_parent_url.rindex("/")]
        base_image_uri = base_url + parent_uri + "/"

        image_write_path = "./"+parent_dir+"/image"

        # 替换图片路径
        all_pic_path = get_all_pic_path(md_content)

        if len(all_pic_path) > 0:
            for pic_url in all_pic_path:
                download_pic_url = base_image_uri + pic_url
                new_pic_url = download_pic(download_pic_url, path=image_write_path)

                md_content = md_content.replace(pic_url, new_pic_url)

        return md_content

    # 获取目录索引
    def get_index_dir(self, md_content):
        md_render = misaka.Markdown(misaka.HtmlRenderer())
        html = md_render(md_content)
        soup = BeautifulSoup(html, features='html.parser')
        dir_name_list = []
        filter_name = ['/', '../']
        for dir_item in soup.find_all('a'):
            dir_url = dir_item.get('href')
            dir_name = unquote(dir_url)
            print(dir_name)
            if dir_name in filter_name:
                print('filter name', dir_name)
                continue
            dir_name_list.append(dir_name)

        return dir_name_list

    # 创建文件目录
    def mkdir(self, dir_name):
        folder = os.path.exists(dir_name)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(dir_name)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print("创建目录成功")
        else:
            print("---  There is this folder!  ---")

        self.mkimage(dir_name)

    def mkimage(self, dir_name):
        path = dir_name + "/image"
        folder = os.path.exists(path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print("创建目录成功")
        else:
            print("---  There is this folder!  ---")


if __name__ == '__main__':
    spider = Spider()
    url = "https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B7%B1%E5%85%A5%E6%8B%86%E8%A7%A3Java%E8%99%9A%E6%8B%9F%E6%9C%BA"
    filename = "深入拆解Java虚拟机"
    spider.exec(url, filename)
