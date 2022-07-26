import os
import pdfkit
html_path = './dist/html'
pdf_path = './dist/pdf'

# 需要更换个人wkhtmltopdf路径
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

src_path_list = []
for html in os.listdir(html_path):
    print(html)
    src_path_list.append(html_path + "/" + html)

pdf_option = {
            'page-size': 'A4',
            'page-width': '1400px',
            'footer-center': '[page]',
            'margin-top': '0.5in',
            'margin-right': '0.5in',
            'margin-bottom': '0.5in',
            'margin-left': '0.5in',
            'encoding': "UTF-8",
            'custom-header': [('Accept-Encoding', 'gzip')],
            'cookie': [('cookie-name1', 'cookie-value1'), ('cookie-name2', 'cookie-value2')],
            'minimum-font-size': 38,
            'outline-depth': 10,
            # 'animation': False,
            # 'page-size': 'Letter',
        }

pdfkit.from_file(src_path_list, pdf_path + "/b.pdf", options=pdf_option, configuration=config)