# -*- coding: utf-8 -*-

import scrapy


class NewsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    user = scrapy.Field()
