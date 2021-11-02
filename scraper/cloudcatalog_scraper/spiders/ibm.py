import scrapy
from cloudcatalog_scraper.items import CloudServiceItem
import cloudcatalog_scraper.common as common

class IbmSpider(scrapy.Spider):
  name = 'ibm'
  start_urls = ['https://www.ibm.com/cloud/products']

  def parse(self, response):
    pass
    for service in response.css('.cws-card'):
      name = service.css('.cws-headline::text').get()
      yield CloudServiceItem(
        f'{self.name}_{common.normalize(name)}',
        name,
        service.css('.cws-body::text').get(),
        response.urljoin(service.css('.cws-card::attr(href)').get())
      )