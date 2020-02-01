# -*- coding: utf-8 -*-
import scrapy
from kishidata.items import KishiWorkItem

class KishiSpider(scrapy.Spider):
    name = 'kishi'
    allowed_domains = ['shogi.or.jp']
    start_urls = ['https://www.shogi.or.jp/player/numerical_order.html']

    def parse(self, response):
        root_url = '/'.join(response.url.split('/')[:3])
        kishi_urls = response.xpath('//a[contains(@href,"player/pro")]/@href').extract()
        for path in kishi_urls:
            print(root_url + path)
            #yield scrapy.Request(root_url + path, callback=parse_kishi)

    def parse_kishi(self, response):
        kishi = ItemLoader(item=KishiWorkItem, response=response)
        kishi.add_xpath('id', '//table[@class="tableElements02"]//th[text()="棋士番号"]//following-sibling::td//text()')
        kishi.add_xpath('name', '//div[@class="nameArea"]//h1[@class="nameTtl"]//span[@class="jp"]/text()')
        kishi.add_xpath('name_en', '//div[@class="nameArea"]//h1[@class="nameTtl"]//span[@class="en"]/text()')
        kishi.add_xpath('birth_date', '//table[@class="tableElements02"]//th[text()="生年月日"]//following-sibling::td//text()')
        kishi.add_xpath('birth_place', '//table[@class="tableElements02"]//th[text()="出身地"]//following-sibling::td//text()')
        kishi.add_xpath('master', '//table[@class="tableElements02"]//th[text()="師匠"]//following-sibling::td//text()')
        kishi.add_xpath('ryuoh', '//table[@class="tableElements02"]//th[text()="竜王戦"]//following-sibling::td//text()')
        kishi.add_xpath('order', '//table[@class="tableElements02"]//th[text()="順位戦"]//following-sibling::td//text()')
        return kishi.load_item()