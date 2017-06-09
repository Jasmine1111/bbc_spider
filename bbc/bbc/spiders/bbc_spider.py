#  _*_ coding: utf-8  _*_


from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy import log
import re

from bbc.items import BbcItem

class bbcSpider(CrawlSpider):
    name = "bbc"
    
    start_urls = ["http://www.bbc.com"]
    download_delay = 2
    handle_httpstatus_list = [301]
    

    rules = [
            Rule(
                SgmlLinkExtractor(allow=(r"http://www.bbc.com/.*?"),
              #  deny=("http:\/\/.*\.(gif|GIF|jpg|JPG|ico|ICO|css|sit|eps|wmf|zip|ppt|mpg|xls|gz|rpm|tgz|mov|MOV|exe).*",
              #          "http:\/\/.*#.*",
               #         "https:\/\/www\.bbc\.com\/w\/index\.php\?.*type=signup.*",
                #        "https:\/\/www\.bbc\.com\/w\/index\.php\?.*action=.*",
                  #       "https:\/\/www\.bbc\.com\/w\/index\.php\?.*title=Talk:.*",
             #           "https:\/\/www\.bbc\.com\/w\/index\.php\?.*title=Category:.*",
              #          "https:\/\/www\.bbc\.com\/w\/index\.php\?.*title=Special:.*",
              #          "https:\/\/www\.bbc\.com\/sport.*",
              #          "https:\/\/www\.bbc\.com\/weather.*",
              #          "http:\/\/www\.bbc\.com\/earth.*",
              #          "http:\/\/www.bbc.com\/travel.*",
              #          "https:\/\/www\.bbc\.com\/w\/index\.php\?.*title=Special%3AUserLogin.*",
              #          "https:\/\/www\.bbc\.com\/w\/index\.php\?.*title=Special.*",
              #          "https:\/\/www\.bbc\.com\/w\/index\.php\?.*title=User_talk:.*",
              #          "https:\/\/www\.bbc\.com\/w\/index\.php\?.*title=User:.*",
              #          "https:\/\/www\.bbc\.com\/w\/index\.php\?.*title=Template:.*",
              #          "https:\/\/www\.bbc\.com\/w\/index\.php\?.*title=Template_talk:.*"
           # ),
           allow_domains = ("www.bbc.com")
          ),
          callback='parse_item',
          follow='true'
       )
      ]

    def parse_item(self,response):
         item = BbcItem()
         title_tmp = response.xpath('//*[@id="page"]//h1//text()').extract_first()
         title = title_tmp
         if title:
             title = title.encode('utf8')
         item['title'] = title
         content_tmp = response.xpath('//*[@id="page"]/div[2]/div[2]/div/div[1]/div[1]//p//text() | //*[@id="page"]/div[2]/div[2]/div/div[1]/div[1]//h2//text()').extract()
         content = ''
         for con in content_tmp:
             if con[-1] == '.':
                 con = con+' '
             content = content + con.encode('utf-8')
         item['content'] = content
         link = str(response.url)
         item['url'] = link.encode('utf-8')
         return item
