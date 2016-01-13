# -*- coding: utf-8 -*-
import scrapy
from reddit_spidermon_demo.items import NewsItem


class RedditSpider(scrapy.Spider):
    name = "reddit"
    allowed_domains = ["reddit.com"]
    start_urls = (
        'http://www.reddit.com/r/programming',
    )

    def parse(self, response):
        for submission_sel in response.css("div.entry"):
            item = NewsItem()
            item['url'] = submission_sel.css("a.title ::attr(href)").extract_first()
            item['title'] = submission_sel.css("a.title ::text").extract_first()
            item['user'] = submission_sel.css("a.author ::text").extract_first()
            yield item
