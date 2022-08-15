import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        section = response.xpath('//section[@id="numerical-index"]')
        all_peps = section.xpath('.//a[@class="pep reference internal"]/@href')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = (response.xpath(
                 '//h1[@class="page-title"]/text()'
                 ).get().split(' '))
        data = {
            'number': int(title[1]),
            'name': ' '.join(title[3:]),
            'status': response.xpath(
                '//dt[contains(., "Status")]/following-sibling::dd/text()'
            ).get(),
        }
        yield PepParseItem(data)
