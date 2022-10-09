[**English**](https://github.com/georegehehe/covidscraper) | [**简体中文**](./README_ZH.md)
# COVID SCRAPER
# 1.Utilities
This python-based program can be used to collect data regarding new Covid Cases in 450+ major Chinese cities from the Chinese National Health Commission Website with an excel output. Packages used includes pyppeteer, beautiful soup, and asyncio

# 2.Requirements
Please refer to requirements.txt for required modules. Make sure to pip install before running.
Please run under python3.8/3.10 environment

The scraping function is mostly based on pyppeteer api and chromium. Due to the volatile nature of the latest Chromium version, try except is extensively used throughout the program to intercept errors and resend http requests. Please adjust based on specific circumstances faced by your computer/chromium.

# 3.Components
main.py executes http requests and utilizes functions from other scripts to collect, modify, and output the data. 
 
city_dict.py converts excel data into the hashmap-based data structure used in the program 

text_analyzer.py performs key textual analysis texts; it reads the textual data from the CHHC website into numerical data by recognizing the pattern among the texts.

# 4.Others
The program only supports collecting data from a single page. But due to the patterns observed among the url of different pages, feel free to manually change the url variable into that of your desird page. 

The program only works for cases before May, as the CNHC website soon changed their reporting structure, and individual numbers for each city is no longer availalbe.

# 5.Sources
https://juejin.cn/post/6996985734854869000

http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml

