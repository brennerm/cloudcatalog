import scrapy
from cloudcatalog_scraper.items import CloudServiceItem
import cloudcatalog_scraper.common as common

class DigitalOceanSpider(scrapy.Spider):
  name = 'digitalocean'
  start_urls = ['https://www.digitalocean.com/products/']

  def parse(self, response):
    for service in response.css('[data-testid="card"]'):
      name = service.css('h5::text').get()
      yield CloudServiceItem(
        f'{self.name}_{common.normalize(name)}',
        name,
        service.css('p::text').get(),
        response.urljoin(service.css('a::attr(href)').get())
      )