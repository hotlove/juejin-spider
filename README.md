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
> 主程序入口，主要负责爬取内容转换成`md`,`html`文件

### markdown2local
> 将爬取下来得`md` 内容种得图片 转换成本地图片，实现本地保存

### html2pdf
> 将`html`内容转化为`markdown`格式

### html2pdf
将`html`转化为`pdf`文件

### 使用建议
1. 使用`spider_processor`获取小册内容，注意，这里有些小册因为没有返回`markdown`文件格式内容，`md`目录会为空，这里推荐使用`html2md`脚本进行转化
2. 为了防止小册图片连接地址丢失建议使用`md2local`脚本将`markdown`文件保存一份本地文件，这里的本地是指将图片本地化