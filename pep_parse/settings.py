from pathlib import Path


BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
