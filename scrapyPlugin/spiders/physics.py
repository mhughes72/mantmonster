from scrapy.spiders import Spider as BaseSpider
from scrapyPlugin.items import PhysicsSiteItem
import scrapy

class PhysicsSpider(scrapy.Spider):
    name = 'physics'
    allowed_domains = ['phys.org/physics-news']
    start_urls = ['https://phys.org/physics-news/']

    def parse(self, response):
        articles = response.xpath("//article[@class='sorted-article']/div[@class='d-flex']")
        for article in articles:
            item = PhysicsSiteItem()
            item["article_title"] = article.xpath(".//div[@class='sorted-article-content d-flex flex-column ie-flex-1']/h3[@class='mb-1 mb-lg-2']/a[@class='news-link']//text()").get()
            item["article_link"] = article.xpath(".//div[@class='sorted-article-content d-flex flex-column ie-flex-1']/h3[@class='mb-1 mb-lg-2']/a[@class='news-link']/@href").get()
            item["article_img"] = article.xpath(".//figure[@class='sorted-article-figure']/a/img/@data-src").get()
            item["article_summary"] = article.xpath(".//div[@class='sorted-article-content d-flex flex-column ie-flex-1']/p[@class='mb-1 pr-1'][1]//text()").get()
            yield item


