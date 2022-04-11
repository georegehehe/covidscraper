import pyppeteer.errors
import requests
import text_analyzer
from bs4 import BeautifulSoup
from pyppeteer import launcher
from pyppeteer import launch
from city_dict import *
import datetime
import asyncio

import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome import options

import requests.packages.urllib3.util.connection as urllib3_cn
from selenium.webdriver.common.by import By

launcher.DEFAULT_ARGS.remove("--enable-automation")
#starting url
url = "http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml"

# define an asynchronous function to the raw html data from a given url
async def fectchURL(url):
    browser = await launch({'headless':False,'dumpio':True, 'autoClose':True})
    page = await browser.newPage()
    await page.goto(url)
    await asyncio.wait([page.waitForNavigation()], timeout=10)
    str = await page.content()
    await browser.close()
    return str

# due to some unpredictable crashing error with chromium on MacOS, if any exception is detected, recursively call
# the function itslef again until error doesn't occur
def fetch(url):
    try:
        return asyncio.get_event_loop().run_until_complete(fectchURL(url))
    except:
        return fetch(url)

# main function
if  "__main__" == __name__:
    # utilized BeautifulSoup parser to parse the data from the raw html source
    page_soup = BeautifulSoup(fetch(url), 'html.parser')
    # locate all li elements in the html file under the class "list", which contains all relevant links and dates
    all_lis = page_soup.find('div', attrs={"class": "list"}).ul.find_all("li")
    link_list = list()
    date_list = list()
    city_list = list()
    out_list = list()
    # add all links and dates into their respective lists
    for element in all_lis:
        link = "http://www.nhc.gov.cn" + element.a["href"]
        link_list.append(link)
        dt = int(element.span.text.replace('-',''))
        yr = int(dt / 10000)
        mon = int((dt - yr * 10000)/100)
        d = dt - yr * 10000 - mon * 100
        dobj = datetime.datetime(yr, mon, d)
        yesterday = dobj - datetime.timedelta(days=1)
        date_list.append(yesterday.strftime("%Y%m%d"))
    # iterate through the link list and access html data from each respective link
    for i in range(len(link_list)):
        li = link_list[i]
        date = date_list[i]
        empty1 = True
        empty2 = True
        while empty1 or empty2:
            try:
                soup = BeautifulSoup(fetch(li), 'html.parser')
            except:
                soup = BeautifulSoup(fetch(li), 'html.parser')
            print(soup.prettify())
            # access all texts with id "xw_box"
            all_text = soup.find_all('div', attrs={"id":"xw_box"})
            str_list = []
            # put all the texts into a single string variable
            for element in all_text:
                if element.text not in str_list:
                    str_list.append(element.text)
            output = ""
            for text in str_list:
                output = text + output
            # use functions from other files to generate a dictionary which maps every city to its key attributes such as
            # its province and the number of cases (本土 and 无症状 respectively), then use the text analyzer to fill in the missing
            # fields (number of cases in this case)
            cities = create_dict()
            empty1 = text_analyzer.analyzer(output, cities, "本土")
            empty2 = text_analyzer.analyzer(output, cities, "无症状")
            print("EMPTY DATA%d: REATTEMPT", date)
        province_add(cities)
        print(cities)
        city_list.append((date, cities))
    # combine the data scraped from every url page into a standard format that can be read into an Excel file
    out_list = dict_out(city_list)
    out_excel(out_list)






