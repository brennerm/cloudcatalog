import scrapy
from cloudcatalog_scraper.items import CloudServiceItem
import cloudcatalog_scraper.common as common

class AlibabaSpider(scrapy.Spider):
  name = 'alibaba'
  start_urls = ['https://www.alibabacloud.com/product']

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