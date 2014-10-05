import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class HotelItem(scrapy.Item):
	name = scrapy.Field()
	url = scrapy.Field()
	expedia_price = scrapy.Field()

class ExpediaSpider(CrawlSpider):

	name = "expedia"
	allowed_domains = ['expedia.com']
	start_urls = ['http://www.expedia.com']
	rules = [Rule(LinkExtractor(allow=['/Hotel-Search?#endDate=10/15/2014&startDate=10/12/2014&destination=Berlin+(and+vicinity),+Germany&adults=2&regionId=179892&sort=mostPopular&page=\d']), 'parse_hotel')]

    def parse_hotel(self, response):
        hotel = HotelItem()
        hotel['url'] = response.url
        hotel['name'] = response.xpath("//*[contains(@id,'hotel')]/a/div[2]/ul/li[3]/span/strong/text()").extract()
        hotel['expedia_price'] = response.xpath("//span[@class='price']/span[contains(@class,'actualPrice')]/text()").extract()
        return hotel
