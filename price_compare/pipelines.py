# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class PriceComparePipeline(object):

    def __init__(self):
        client = MongoClient()
        self.db = client.pritpal_xyz

    def process_item(self, item, spider):
        if spider.name == 'compare':
            data_dict = {
                'executable_id': item['executable_id'],
                'product_title': item['product_title'],
                'image_url': item['image_url'],
                'product_url': item['product_url'],
                'product_description': item['product_description'],
                'original_price': item['original_price'],
                'discounted_price': item['discounted_price'],
                'seller_name': item['seller_name'],
                'seller_rating': item['seller_rating'],
                'seller_review_count': item['seller_review_count'],
                'source': item['source'],
                'crawled_date': item['crawled_date']
            }
            self.db.crawled_data.insert_one(data_dict)
