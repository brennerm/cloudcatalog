# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import dataclasses


@dataclasses.dataclass
class CloudServiceItem:
    key: str
    name: str
    short_description: str
    link: str
