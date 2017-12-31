class CrawlingXpaths():

    def __init__(self):
        # XPATHS FOR AMAZON
        self.AMAZON_LIST_OF_PRODUCT_XPATH = "//ul[@id='s-results-list-atf']/li/div//h2/../@href"
        self.AMAZON_XPATH = {}
        self.AMAZON_XPATH['product_title'] = "//span[@id='productTitle']/text()"
        self.AMAZON_XPATH['image_url'] = "//span[@data-action='main-image-click']/div/img/@src"
        self.AMAZON_XPATH['product_description'] = "//div[@data-feature-name='featurebullets']//ul"
        self.AMAZON_XPATH['original_price'] = "//td/span[@class='a-text-strike']/text()"
        self.AMAZON_XPATH['discounted_price'] = "//span[@id='priceblock_saleprice']/text()"
        self.AMAZON_XPATH['seller_name'] = "//a[@id='brand']/text()"
        self.AMAZON_XPATH['seller_rating'] = "//span[@class='reviewCountTextLinkedHistogram noUnderline']/@title"
        self.AMAZON_XPATH['seller_review_count'] = "//span[@id='acrCustomerReviewText']/text()"



        # XPATH FOR FLIPKART
        self.FLIPKART_JSON_XPATH = "//script[@id='jsonLD']/text()"
        self.FLIPKART_LIST_OF_PRODUCT_XPATH = "//a[@rel='noopener noreferrer']/@href"

        self.FLIPKART_XPATH = {}
        self.FLIPKART_XPATH['product_title'] = "//h1/text()"
        self.FLIPKART_XPATH['image_url'] = "//img[@class='sfescn']/@src"
        self.FLIPKART_XPATH['product_description'] = "//span[text()='Product Description']/../..//text()"
        self.FLIPKART_XPATH['original_price'] = "//div[@class='_3auQ3N _16fZeb']/text()[2]"
        self.FLIPKART_XPATH['discounted_price'] = "//div[@class='_1vC4OE _37U4_g']/text()[2]"
        self.FLIPKART_XPATH['seller_name'] = "//script[@id='jsonLD']/text()"
        self.FLIPKART_XPATH['seller_rating'] = "//script[@id='jsonLD']/text()"
        self.FLIPKART_XPATH['seller_review_count'] = "//script[@id='jsonLD']/text()"



        # XPATH FOR SHOPCLUES
        self.SHOPCLUES_LIST_OF_PRODUCT_XPATH = "//div[@class='column col3 search_blocks']/a/@href"

        self.SHOPCLUES_XPATH = {}
        self.SHOPCLUES_XPATH['product_title'] = "//h1/text()"
        self.SHOPCLUES_XPATH['image_url'] = "//input[@name='mainImg']/@data-src"
        self.SHOPCLUES_XPATH['product_description'] = "//tr/td/span"
        self.SHOPCLUES_XPATH['original_price'] = "//span[@class='o_price1']/@content"
        self.SHOPCLUES_XPATH['discounted_price'] = "//span[@class='f_price']/@content"
        self.SHOPCLUES_XPATH['seller_name'] = "//div[@class='sllr_info']/h3/text()"
        self.SHOPCLUES_XPATH['seller_rating'] = "//div[@class='ratings']/span[@class='val']/text()"
        self.SHOPCLUES_XPATH['seller_review_count'] = "//div[@class='ratings']/span[@class='']/text()"
