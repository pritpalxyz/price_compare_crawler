# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PriceCompareItem(scrapy.Item):
    executable_id = scrapy.Field()
    product_title = scrapy.Field()
    image_url = scrapy.Field()
    product_url = scrapy.Field()
    product_description = scrapy.Field()
    original_price = scrapy.Field()
    discounted_price = scrapy.Field()
    seller_name = scrapy.Field()
    seller_rating = scrapy.Field()
    seller_review_count = scrapy.Field()
    source = scrapy.Field()
    crawled_date = scrapy.Field()
