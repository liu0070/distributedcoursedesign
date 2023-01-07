# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousepriceItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  # 标题
    address = scrapy.Field()  # 地点
    huxing = scrapy.Field()  # 户型
    BuildingArea = scrapy.Field()  # 建筑面积
    Position = scrapy.Field()  # 所处位置
    Direction = scrapy.Field()  # 房屋朝向
    BuildingTime = scrapy.Field()  # 建造时间
    SubwayDistance = scrapy.Field()  # 与地铁口距离
    price_total = scrapy.Field()  # 房屋总价
    price_square = scrapy.Field()  # 每平方米价格
    price_dy = scrapy.Field()  # 低于市场价
    labels = scrapy.Field()  # 房屋标签

