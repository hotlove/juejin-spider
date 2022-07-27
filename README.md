### conf.ini
```editorconfig
[juejin]
aid = 
uuid = 
booklet_id = 
book_name = test
get_section_dir_url = https://api.juejin.cn/booklet_api/v1/booklet/get?aid=${juejin:aid}&uuid=${juejin:uuid}
get_section_content_url = https://api.juejin.cn/booklet_api/v1/section/get?aid=${juejin:aid}&uuid=${juejin:uuid}
cookie =
```
- aid 打开f12 -> 查看接口获取
- uuid 打开f12 -> 查看接口获取
- booklet_id 书本id打开小册地址栏中有 类似`https://juejin.cn/book/xxxxxxx`
- get_secition_dir_url 获取左侧目录url
- get_section_content_url 获取实际内容接口
- cookie 请求cookie
### spider_processor
主程序入口，主要负责爬取内容转换成`md`,`html`文件

### markdown2local
将爬取下来得`md` 内容种得图片 转换成本地图片，实现本地保存