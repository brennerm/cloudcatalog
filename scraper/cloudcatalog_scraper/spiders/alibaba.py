import scrapy
from cloudcatalog_scraper.items import CloudServiceItem
import cloudcatalog_scraper.common as common

class AlibabaSpider(scrapy.Spider):
  name = 'alibaba'
  start_urls = ['https://www.alibabacloud.com/product']

  def parse(self, response):
    for service in response.css('.product-detail-item'):
      name = service.css('.product-tit::text').get()
      yield CloudServiceItem(
        f'{self.name}_{common.normalize(name)}',
        name,
        service.css('.product-desc::text').get(),
        response.urljoin(service.css('a::attr(href)').get())
      )