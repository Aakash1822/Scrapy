import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import config
import start_scrapy

#--- Third-Party Libraries

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

import re

# 
class my_Spider(Spider):
    # spider name
    name = config.scrapy_name
    allowed_domains = config.domains_list 
    start_urls = config.urls_list

    def parse(self, response):
        sel = Selector(response) 

        domain_str = response.url.split(config.url_domain_split_start)[config.url_domain_split_start_num].split(config.url_domain_split_end)[config.url_domain_split_end_num]
        start_scrapy.check_current_product_tag_patterns(domain_str)
        if config.current_products_pattern != '' :
            products_all = sel.xpath(config.init_div+config.current_products_pattern)
            products_list = []

            for product_tag in products_all:
                product_name_with_price = {}
                product_name_with_price[config.web_name] = domain_str
                try:
                    product_name_with_price[config.product_name] = product_tag.xpath(config.in_div+config.current_product_name_pattern+config.extract_text).extract()[0].strip()
                except:
                    product_name_with_price[config.product_name] = config.none_value
                try:
                   product_name_with_price[config.price_name] = product_tag.xpath(config.in_div+config.current_product_price_pattern+config.extract_text).extract()[0].strip()
                except:
                    product_name_with_price[config.price_name] = config.none_value
                products_list.append(product_name_with_price)   
            config.total_products_list.append(products_list)