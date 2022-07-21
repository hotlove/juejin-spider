import configparser
from configparser import ExtendedInterpolation

from spider_processor import SpiderProcessor


def load_config():
    # 获取配置文件
    cf = configparser.ConfigParser(interpolation=ExtendedInterpolation(),
                                   inline_comment_prefixes=['#', ';'],
                                   allow_no_value=True)
    cf.read('conf.ini')
    aid = cf.get("juejin", "aid")
    uuid = cf.get("juejin", "uuid")
    section_url = cf.get("juejin", "get_section_dir_url")
    content_url = cf.get("juejin", "get_section_content_url")
    booklet_id = cf.get("juejin", "booklet_id")
    book_name = cf.get("juejin", "book_name")
    return aid, uuid, booklet_id, book_name, section_url, content_url


if __name__ == '__main__':
    aid, uuid, booklet_id, book_name, section_url, content_url = load_config()
    spider_proccessor = SpiderProcessor(aid, uuid, booklet_id, book_name, section_url, content_url)
    spider_proccessor.run_proccessor()
