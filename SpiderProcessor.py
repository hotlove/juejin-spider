class SpiderProcessor:
    def __init__(self, aid, uuid, section_url, content_url):
        self.aid = aid
        self.uuid = uuid
        self.section_url = section_url
        self.content_url = content_url

    def run_proccessor(self):
        sections = self.get_sections()
    # 获取所有目录id
    def get_sections(self):
        pass

    # 获取内容
    def get_content(self, section_ids):
        pass