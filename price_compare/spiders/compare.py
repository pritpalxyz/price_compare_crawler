# -*- coding: utf-8 -*-
import scrapy, datetime, re, json
from bs4 import BeautifulSoup
from price_compare.items import PriceCompareItem
from price_compare.xpaths import CrawlingXpaths
from pprint import pprint

class CompareSpider(scrapy.Spider):
    name = "compare"
    # allowed_domains = ["amazon.in", "flipkart.com", "shopclues.com"]
    start_urls = []

    def __init__(self, search_word=None, executable_id=None, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.executable_id = executable_id
        self.XPATH_OBJECT = CrawlingXpaths()
        self.DeclareVariables()
        self.UpdateSearchUrl(search_word)

    def DeclareVariables(self):
        self.AMAZON_PRE_URL = "https://www.amazon.in/s/field-keywords="
        self.FLIPKART_PRE_URL = "https://www.flipkart.com/search?q="
        self.SHOPCLUES_PRE_URL = "http://www.shopclues.com/search?q="

        self.FLIPKART_URL = "https://www.flipkart.com"

    def UpdateSearchUrl(self, search_word):
        self.AMAZON_SEARCH_URL = "{0}{1}".format(self.AMAZON_PRE_URL,
                                                            search_word)
        self.FLIPKART_SEARCH_URL = "{0}{1}".format(self.FLIPKART_PRE_URL,
                                                            search_word)
        self.SHOPCLUES_SEARCH_URL = "{0}{1}".format(self.SHOPCLUES_PRE_URL,
                                                            search_word)

        self.start_urls.append(self.AMAZON_SEARCH_URL)
        self.start_urls.append(self.FLIPKART_SEARCH_URL)
        self.start_urls.append(self.SHOPCLUES_SEARCH_URL)

    def FilterString(self, crawled_string):
        filterd_string = self.listToStr(crawled_string)
        soup = BeautifulSoup(filterd_string, 'html.parser')
        return re.sub(" +|\n|\r|\t|\0|\x0b|\xa0",' ',soup.get_text()).strip()

    def listToStr(self, data_list):
        return " ".join(unicode(content) for content in data_list)

    def parse(self, response):
        if "www.amazon" in response.url:
            source = 'amazon'
            LIST_OF_PRODUCT_XPATH = self.XPATH_OBJECT.AMAZON_LIST_OF_PRODUCT_XPATH
        if "www.flipkart" in response.url:
            LIST_OF_PRODUCT_XPATH = self.XPATH_OBJECT.FLIPKART_LIST_OF_PRODUCT_XPATH
            source = 'flipkart'
        if "www.shopclues" in response.url:
            LIST_OF_PRODUCT_XPATH = self.XPATH_OBJECT.SHOPCLUES_LIST_OF_PRODUCT_XPATH
            source = 'shopclues'

        for href in response.xpath(LIST_OF_PRODUCT_XPATH).extract():
            if source == "flipkart":
                if "/p/" not in href:continue
                href = "{0}{1}".format(self.FLIPKART_URL,href)
            if source == 'shopclues':
                href = "http:{0}".format(href)
            req = scrapy.Request(href, callback=self.ParseSubProductInformation)
            req.meta['source'] = source
            yield req

    def ParseSubProductInformation(self, response):
        source  = response.meta['source']
        if source =='amazon':
            XPATH_SOURCE = self.XPATH_OBJECT.AMAZON_XPATH
            rating = self.FilterString(response.xpath(XPATH_SOURCE['seller_rating']).extract())
            title = self.FilterString(response.xpath(XPATH_SOURCE['product_title']).extract())
            imageurl = self.listToStr(response.xpath(XPATH_SOURCE['image_url']).extract())
            review_count = self.FilterString(response.xpath(XPATH_SOURCE['seller_review_count']).extract())
            seller_name = self.FilterString(response.xpath(XPATH_SOURCE['seller_name']).extract())
            description = self.FilterString(response.xpath(XPATH_SOURCE['product_description']).extract())
        if source == 'flipkart':
            XPATH_SOURCE = self.XPATH_OBJECT.FLIPKART_XPATH
            json_content = json.loads(self.FilterString(response.xpath(self.XPATH_OBJECT.FLIPKART_JSON_XPATH).extract()))
            json_content = json_content[0]
            try:
                rating = json_content['aggregateRating']['ratingValue']
            except:
                rating = ""
            title = json_content['name']
            imageurl = json_content['image']
            try:
                review_count = json_content['aggregateRating']['reviewCount']
            except:
                review_count = ""
            try:
                seller_name = json_content['brand']['name']
            except:
                seller_name = ""
            try:
                description = json_content['description']
            except:
                description = self.FilterString(response.xpath(XPATH_SOURCE['product_description']).extract())

        if source == 'shopclues':
            XPATH_SOURCE = self.XPATH_OBJECT.SHOPCLUES_XPATH
            rating = self.FilterString(response.xpath(XPATH_SOURCE['seller_rating']).extract())
            title = self.FilterString(response.xpath(XPATH_SOURCE['product_title']).extract())
            imageurl = self.listToStr(response.xpath(XPATH_SOURCE['image_url']).extract())
            review_count = self.FilterString(response.xpath(XPATH_SOURCE['seller_review_count']).extract())
            seller_name = self.FilterString(response.xpath(XPATH_SOURCE['seller_name']).extract())
            description = self.FilterString(response.xpath(XPATH_SOURCE['product_description']).extract())

        item = PriceCompareItem()
        item['executable_id'] = self.executable_id
        item['product_title'] = title
        item['image_url'] = imageurl
        item['product_url'] = response.url
        item['product_description'] = description
        item['original_price'] = self.FilterString(response.xpath(XPATH_SOURCE['original_price']).extract())
        item['discounted_price'] = self.FilterString(response.xpath(XPATH_SOURCE['discounted_price']).extract())
        item['seller_name'] = seller_name
        item['seller_rating'] = rating
        item['seller_review_count'] = review_count
        item['source'] = source
        item['crawled_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        yield item
