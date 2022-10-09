[**English**](https://github.com/georegehehe/covidscraper) | [**简体中文**](./README_ZH.md)
# COVID SCRAPER
# 1.功能
此程序使用了python的一些基本库以及模组，包括pyppeteer, beautiful soup, 以及 asyncio
实现了对中国卫健委新冠信息网站的摘取，并返回含有各省市确诊人数的excel表格
# 2.注意事项
请查看requirements.txt的模组要求，并在运行前执行pip install以确保程序能正常运行。 
请在python3.8/3.10环境下运行此程序。

此程序主要使用pyppeteer模组，通过访问chromium对网站发起http请求。因为chromium当前版本一些
不稳定因素，程序有时候会报错，因此使用了try except方法拦截错误并重新发起请求。
请根据您电脑的情况可以对源代码做出调整（例如删除try except），以避免程序卡死

# 3.组件介绍
main.py为主程序，负责执行http请求以及调用其他python文件的函数以创建，修改，和输出数据

city_dict.py实现了excel文件与程序数据结构之间的转换；程序的数据结构主要用到了python的dictionary
用hash table的形式保证程序能够快速修改和摘取相应的数据 （python 文件内有对数据结构的详细介绍）

text_analyzer.py为核心文字分析模件；得利于卫健委发布数据的有规律性，可以通过搜索关键词、字、标点符号以筛选
重要段落，再通过搜索城市关键词以获取相对应的新冠确诊数字。

# 4.其他
此程序目前仅支持对卫健委网站第一页的搜索。由于该网站网址的规律性，理论上来说是可以轻松的对多页进行分析
不过因为chromium的不稳定因素以及过去数据的格式不统一性，在作者本机上运行程序时难以调试/debug，所以
此功能可以作为未来延展

# 5.Sources
处理卫健委网站的反爬虫机制时参考了以下网站：
https://juejin.cn/post/6996985734854869000

卫健委网站：
http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml
