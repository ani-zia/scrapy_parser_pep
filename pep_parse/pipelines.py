import csv
import datetime as dt

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

from .settings import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_statuses_count = {}

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('status'):
            pep_status = adapter['status']
            self.pep_statuses_count[pep_status] = (
                self.pep_statuses_count.get(pep_status, 0) + 1)
            return item
        else:
            raise DropItem(f'Missing status in {item}')

    def close_spider(self, spider):
        total = spider.crawler.stats.get_stats()['item_scraped_count']
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        special_format_for_writing = ([['Статус', 'Количество']] + [[k, v]
                                      for k, v
                                      in self.pep_statuses_count.items()] + [
                                      ['Total', total]])
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(special_format_for_writing)
