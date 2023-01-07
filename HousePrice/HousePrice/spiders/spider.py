import scrapy
from scrapy.spiders import Spider
from bs4 import BeautifulSoup
from .items import *
import re


class MySpider(Spider):
    allowed_domains = ['hf.fang.anjuke.com']
    name = "myspider"

    def start_requests(self):
        start_urls = []
        for i in range(1, 30):
            url = "https://hf.esf.fang.com/house/i3{0}?rfss=1-9714ba262b20953b2f-79".format(i)
            start_urls.append(url)
        for url in start_urls:
            print(url)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        house_data = BeautifulSoup(response.text, 'lxml')
        print("开始解析页面")
        for info in house_data.select("dl", attrs={"class": "clearfix"}):
            item = HousepriceItem()
            item['title'] = info.select("span[class='tit_shop']")[0].text.strip()
            tel_shop = [j for j in [i.strip() for i in info.select("p[class='tel_shop']")[0].text.split('\n')] if
                        j != "" and j != '|']
            item['huxing'] = tel_shop[0]
            item['BuildingArea'] = re.findall("\d+", tel_shop[1])[0]
            item['xiaoqu'] = tel_shop[2]
            item['Position'] = tel_shop[3]
            item['Direction'] = tel_shop[4]
            item['BuildingTime'] = tel_shop[5] if tel_shop[5].isdigit() else None
            item['address'] = " ".join(info.select("p[class='add_shop']")[0].text.strip().split())
            try:
                labels = info.select("p[class='clearfix label']")[0]
                if info.find("span", attrs={"class": "bg_none icon_dt"}):
                    item['SubwayDistance'] = re.findall("\d+",
                                                        info.find("span", attrs={"class": "bg_none icon_dt"}).text)[0]
                    if len(labels.text.split()) > 1:
                        item['labels'] = ','.join(labels.text.split()[:-1])
                else:
                    if len(labels.text.split()) > 0:
                        item['labels'] = ','.join(labels.text.split())
            except:
                item['labels'] = ''
                item['SubwayDistance'] = ''
            prices = info.select("dd[class='price_right']")[0].text.split()
            item['price_total'] = re.findall("\d+", prices[0])[0]
            item['price_square'] = re.findall("\d+", prices[1])[0]
            if len(prices) > 2:
                item['price_dy'] = re.findall("\d+", prices[2])[0]
            else:
                item['price_dy'] = ''
            yield item
        print("页面解析结束")
