# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TechstarsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	Class = scrapy.Field()
	Company = scrapy.Field()
	Funding = scrapy.Field()
	Status = scrapy.Field()
	Nexus = scrapy.Field()
	Website = scrapy.Field()
	Crunchbase_Url = scrapy.Field()
	Description = scrapy.Field()
	Logo = scrapy.Field()
