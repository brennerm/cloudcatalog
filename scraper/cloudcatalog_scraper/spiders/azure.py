import scrapy
from cloudcatalog_scraper.items import CloudServiceItem
import cloudcatalog_scraper.common as common

def normalize(name):
  return name.lower().replace(' ', '_').replace('(', '').replace(')', '')

class AzureSpider(scrapy.Spider):
  name = 'azure'
  start_urls = ['https://azure.microsoft.com/en-us/services/']

  def parse(self, response):
    for service in response.css('#products-list > .row > .column'):
      name = service.css('h3 > a > span::text').get()
      yield CloudServiceItem(
        f'{self.name}_{common.normalize(name)}',
        name,
        service.css('p::text').get(),
        response.urljoin(service.css('h3 > a::attr(href)').get())
      )