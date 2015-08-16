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
        l=[]
        l1=[]
        items['link_name']=response.xpath("//*[contains(@class,'featured-link')]/a/text()").extract()
        items['link']=response.xpath("//*[contains(@class,'featured-link')]/a/@href").extract()



        yield items
