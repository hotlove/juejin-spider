import configparser
from configparser import ExtendedInterpolation

def load_config():
    # 获取配置文件
    cf = configparser.ConfigParser(interpolation=ExtendedInterpolation(), inline_comment_prefixes=['#', ';'], allow_no_value=True)
    cf.read('conf.ini')
    aid = cf.get("juejin", "aid")
    uuid = cf.get("juejin", "uuid")
    get_section_url = cf.get("juejin", "get_section_dir_url")
    get_section_content_url = cf.get("juejin", "get_section_content_url")
    print(aid, uuid, get_section_url, get_section_content_url)


if __name__ == '__main__':
    load_config()
