# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from techstars.items import TechstarsItem
import json


class TechstarsSpider(scrapy.Spider):
    name = "techstars"
    allowed_domains = ["techstars.com"]
    start_urls = ['https://connect.techstars.com/widgets/portfolio-statistics.js']

    def parse(self, response):

        base_text = response.text.replace('\\v', '')

        html_list = json.loads(base_text[base_text.find(
                        'var html = ')+11: base_text.find(".join(")])
        html_text = '\n'.join(html_list)

        sel = Selector(text=html_text)

        for t in sel.xpath('//div[@class="batch"]/table'):
            tclass = t.xpath('tr/th[@class="batch_class"]/text()').extract_first(default='').strip()
            for i in t.xpath('tr[@class="parent"]'):
                item = TechstarsItem()
                company_list = i.xpath('td//text()').extract() + ['']*6
                company_info = company_list[2:6]
                item['Class'] = tclass
                item['Company'] = company_info[0]
                item['Funding'] = company_info[1]
                item['Status'] = company_info[2]
                item['Nexus'] = company_info[3]
                item['Website'] = i.xpath(
                    'following-sibling::tr[contains(@class,"child-")]/'
                    'td/a/img/../@href').extract_first(default='').strip()
                item['Crunchbase_Url'] = i.xpath(
                    'following-sibling::tr[contains(@class,"child-")]/'
                    'td/a[contains(@href,"crunchbase.com")]/@href').extract_first(default='').strip()
                item['Description'] = i.xpath(
                    'following-sibling::tr[contains(@class,"child-")]/'
                    'td/p/text()').extract_first(default='').strip()
                item['Logo'] = i.xpath(
                    'following-sibling::tr[contains(@class,"child-")]/'
                    'td/a/img/@src').extract_first(default='').strip()
                yield item
