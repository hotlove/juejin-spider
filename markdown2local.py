'''
此脚本 主要是将md文件中的图片改为本地
'''
import os
import shutil
import uuid

import chardet
import misaka
import requests
from bs4 import BeautifulSoup

src_path = "./dist/md"
dir_path = "./dist/md_local"

dir_path_img = dir_path + "/image"


def get_files_list(dir):
    """
    获取一个目录下所有文件列表，包括子目录
    :param dir:
    :return:
    """
    files_list = []
    for root, dirs, files in os.walk(dir, topdown=False):
        for file in files:
            files_list.append(os.path.join(root, file))

    return files_list


# 获取所有文件路径
def get_all_md(file_path):
    src_path_list = []
    for file_name in os.listdir(file_path):
        if file_name == 'image':
            continue

        item = {
            'path': file_path + "/" + file_name,
            'file_name': file_name
        }

        src_path_list.append(item)

    return src_path_list


def get_all_pic_path(md_content):
    """
       获取一个markdown文档里的所有图片链接
       :param md_content:
       :return:
    """
    md_render = misaka.Markdown(misaka.HtmlRenderer())
    html = md_render(md_content)
    soup = BeautifulSoup(html, features='html.parser')
    pics_list = []
    for img in soup.find_all('img'):
        image_path = img.get('src')
        c = image_path.encode("utf8")
        d = str(c, encoding='utf-8')
        print(type(d))
        print(chardet.detect(bytes(d, 'utf-8')))
        pics_list.append(d)

    return pics_list


# 下载图片
def download_pic(url):
    img_data = requests.get(url).content
    new_img_path = os.path.join(dir_path_img, f'{uuid.uuid4().hex}.jpg')
    with open(new_img_path, 'w+') as f:
        f.buffer.write(img_data)

    return new_img_path


# 复制文件到新目录下
def copy_file2local(src_path, dir_path):
    for file_name in os.listdir(src_path):
        new_path = dir_path + "/" + file_name
        shutil.copyfile(src_path + "/" + file_name, new_path)


def execute_markdow2local():
    # 1.复制文件
    copy_file2local(src_path, dir_path)
    print("copy 完成")

    # 2.获取文件名
    real_src_path = get_all_md(dir_path)
    print("获取文件数量:", len(real_src_path))

    # 3.加载文件并处理
    for file_item in real_src_path:
        with open(file_item['path'], 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()

            # 替换图片路径
            all_pic_path = get_all_pic_path(md_content)
            print(all_pic_path)
            if len(all_pic_path) > 0:
                for pic_url in all_pic_path:
                    s = "颤三"
                    encode = chardet.detect(bytes(pic_url, 'utf-8'))
                    print(encode)
                    if pic_url in md_content:
                        print('old image', True)
                    new_pic_url = download_pic(pic_url)
                    md_content = md_content.replace(pic_url, new_pic_url)
                    if new_pic_url in md_content:
                        print("new image", True)

            # 重新写入文件
            with open(file_item['path'], 'w', encoding='utf-8') as new_md_file:
                new_md_file.write(md_content)

            print(file_item['path'], '处理完毕')


if __name__ == '__main__':
    execute_markdow2local()
