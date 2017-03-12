# _*_ coding:utf-8 _*_

from scrapy.spiders import Rule
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy import log
import re

