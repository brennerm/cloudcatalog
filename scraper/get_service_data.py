import argparse
import json
import os

import scrapy
import scrapy.spiderloader
import scrapy.crawler
import scrapy.utils.project

argparser = argparse.ArgumentParser()
argparser.add_argument("output")
args = argparser.parse_args()

settings = scrapy.utils.project.get_project_settings()
process = scrapy.crawler.CrawlerProcess(settings)
spider_loader = scrapy.spiderloader.SpiderLoader.from_settings(settings)
spider_cls = [spider_loader.load(name) for name in spider_loader.list()]

for spider in spider_cls:
  process.crawl(scrapy.crawler.Crawler(spider, settings={
    "ITEM_PIPELINES": {
      'cloudcatalog_scraper.pipelines.DuplicatesPipeline': 300,
      'cloudcatalog_scraper.pipelines.NullDescriptionPipeline': 400
    },
    "FEEDS": {
        f"{spider.name}.json": {
            "encoding": "utf8",
            "format": "json",
            "overwrite": True
        }
    }
  }))
process.start()


# assert that all result files are at least 1 KB big
for spider in spider_cls:
  assert os.path.getsize(f"{spider.name}.json") > 1024

# merge results into single file
merged_results = []

for spider in spider_cls:
  with open(f"{spider.name}.json", 'r') as f:
    merged_results.extend(
      json.load(f)
    )

with open(args.output, 'w') as f:
  json.dump(merged_results, f)
