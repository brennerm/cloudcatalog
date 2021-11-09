import scrapy
from cloudcatalog_scraper.items import CloudServiceItem
import cloudcatalog_scraper.common as common

class IbmSpider(scrapy.Spider):
  name = 'ibm'
  start_urls = ['https://cloud.ibm.com/catalog']

  def parse(self, response):
    for service in response.css('.pal--catalog-tile'):
      name = service.css('.pal--catalog-tile__header-name::text').get()
      yield CloudServiceItem(
        f'{self.name}_{common.normalize(name)}',
        name,
        service.css('.pal--catalog-tile__desc::text').get(),
        response.urljoin(service.css('a::attr(href)').get())
      )