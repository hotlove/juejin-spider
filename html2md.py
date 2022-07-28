import os
import html2text

src_path = "./dist/html"
dir_path = "./dist/md"


# 获取所有文件路径
def get_all_md(file_path):
    src_path_list = []
    for file_name in os.listdir(file_path):
        if file_name == 'image':
            continue

        f_name = file_name[:file_name.rindex(".")]
        item = {
            'path': file_path + "/" + file_name,
            'file_name': f_name
        }

        src_path_list.append(item)

    return src_path_list


def html2md():
    html_file_list = get_all_md(src_path)

    for html_file in html_file_list:
        with open(html_file['path'], 'r', encoding='utf-8') as html_fp:
            html_content = html_fp.read()

        text_maker = html2text.HTML2Text()
        text_maker.body_width = 0
        markdown = text_maker.handle(html_content)

        md_file_name = "%s/%s.md" % (dir_path, html_file['file_name'])
        with open(md_file_name, 'a', encoding='utf-8') as md_fp:
            md_fp.write(markdown)


if __name__ == '__main__':
    html2md()
