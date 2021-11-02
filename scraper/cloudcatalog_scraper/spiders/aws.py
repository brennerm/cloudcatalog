import scrapy
from cloudcatalog_scraper.items import CloudServiceItem
import cloudcatalog_scraper.common as common

def normalize(name):
  return name.lower().replace(' ', '_').replace('(', '').replace(')', '')

class AwsSpider(scrapy.Spider):
  name = 'aws'
  start_urls = ['https://aws.amazon.com/products/']

  def parse(self, response):
    for service in response.css('.lb-content-item'):
      name = service.css('a > span::text').get()
      yield CloudServiceItem(
        f'{self.name}_{common.normalize(name)}',
        name,
        service.css('a > cite::text').get(),
        service.css('a::attr(href)').get()
      )