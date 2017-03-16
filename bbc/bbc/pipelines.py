# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

import json

class BbcPipeline(object):
    def process_item(self, item, spider):
'''
        if item['title'] and item['content']:
            links = item['link'].split('/')
            country = ''
            if len(links)>=3:
                if links[1] == 'news':
                    country = 'english'
                else:
                    country = links[1]
                temps=links[2].split('-')
                style=temps[0]
                self.file = open('%s_%s.txt'%country%style,'wa+')
            else:
                self.file = open('otherlinks.txt','a')
                self.file.write(item['link'])
            temp = item['content']
            content = ''
            content = 'title:\n' + item['title']
            content = content + '\n'
            content = content + 'content:\n'
            content = content + temp
            content = content + '\n'
            self.file.write(content)
            self.file.close()
'''
        return item
'''
        else:
            raise DropItem("empty title in %s" %item["link"])
'''
