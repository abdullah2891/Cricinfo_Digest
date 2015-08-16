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

        items['teams']=response.xpath("//*[contains(@class,'team-name')]/text()").extract()
        items['scores']=response.xpath("//*[contains(@class,'team-score')]/text()").extract()



        yield items
