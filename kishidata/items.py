# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KishiWorkItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    name_en = scrapy.Field()
    birth_date = scrapy.Field()
    birth_place = scrapy.Field()
    master = scrapy.Field()
    ryuoh = scrapy.Field()
    order = scrapy.Field()
