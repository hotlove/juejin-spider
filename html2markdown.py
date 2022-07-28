import os
import html2text

src_path = "./dist/html"
dir_path = "./dist/md"


def get_all_html(file_path):
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


def trasfer_html2markdown():
    html_file_list = get_all_html(src_path)

    for item in html_file_list:
        with open(item['path'], 'r', encoding='utf-8') as html_fp:
            html_content = html_fp.read()

        markdown = html2text.html2text(html_content)

        md_file_name = "%s/%s.md" % (dir_path, item['file_name'][:item['file_name'].rindex('.')])
        with open(md_file_name, 'a', encoding="utf-8") as md_file:
            md_file.writelines(markdown)


if __name__ == '__main__':
    trasfer_html2markdown()
