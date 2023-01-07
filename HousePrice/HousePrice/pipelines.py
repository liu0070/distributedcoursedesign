# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class HousepricePipeline:
    def __init__(self):
        self.Data = {
            "title": list(),
            "address": list(),
            "huxing": list(),
            "BuildingArea": list(),
            "Position": list(),
            "Direction": list(),
            "BuildingTime": list(),
            "SubwayDistance": list(),
            "price_total": list(),
            "price_square": list(),
            "price_dy": list(),
            "labels": list()
        }

    def process_item(self, item, spider):
        value = dict(item)
        for key in self.Data.keys():
            if key in value.keys():
                self.Data[key].append(value[key])
            else:
                self.Data[key].append("")

    def open_spider(self, spider):
        print("开始爬取")

    def close_spider(self, spider):
        df = pd.DataFrame(self.Data)
        df.to_csv("data.csv")
        print("爬取结束")
