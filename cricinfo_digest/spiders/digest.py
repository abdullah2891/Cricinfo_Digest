import scrapy
from cricinfo_digest.items import CricinfoDigestItem

__author__ = 'Abdullah_Rahman'


class digest(scrapy.Spider):
    name = "cric_digest"
    allowed_domains = ["cricbuzz.com"]
    start_urls = [
        "http://www.cricbuzz.com/cricket-match/live-scores"
    ]

    def parse(self, response):
        items=CricinfoDigestItem()

        items['series']= response.xpath("//h3/text()").extract()
        items['scores']=response.xpath("//*[contains(@class,'teams_scores')]/text()").extract()
        items['teams']=response.xpath("//*[contains(@class,'team_name_completed')]/text()").extract()



        yield items
