import scrapy
from cricinfo_digest.items import CricinfoDigestItem

__author__ = 'Abdullah_Rahman'


class digest(scrapy.Spider):
    name = "cric_digest"
    allowed_domains = ["espncricinfo.com"]
    start_urls = [
        "http://www.espncricinfo.com/"
    ]

    def parse(self, response):
        items=CricinfoDigestItem()

        items['link_name']=response.xpath("//li/p/*[contains(@class,'result-text')]/text()").extract()
        items['link']=response.xpath("//li/p/*[contains(@class,'result-text')]/@href").extract()



        yield items
