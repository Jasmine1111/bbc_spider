# -*- coding: utf-8 -*-

# Define your item pipelines here
#

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from sqlalchemy import Column, Integer,Text, String, DateTime, Numeric, create_engine, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
import json

BaseModel = declarative_base()

class Message(BaseModel):
    __tablename__ = 'message'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    question_id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(VARCHAR(955),nullable=False)
    title = Column(VARCHAR(255))
    language = Column(VARCHAR(255))
    content = Column(Text)

class Mysql(object):
    def __init__(self,host,username,passwd,schema):
        self.message=Message()
        self.host=host
        self.username = username
        self.passwd=passwd
        self.schema = schema
        self.engine = create_engine("mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8&use_unicode=0".format(self.username,self.passwd,self.host,self.schema))
        self.DB_Session = sessionmaker(bind = self.engine,autocommit=True)
        self.session = self.DB_Session()
        BaseModel.metadata.create_all(self.engine)
    def insert_message(self,item):
        message = Message(url=item['url'],title=item['title'],content=item['content'],language=item['country'])
        self.session.add(message)
        try:
            self.session.flush()
        except:
            time.sleep(0.01)

class BbcPipeline(object):
    def __init__(self,settings):
        self.host = settings.get('MYSQL_HOST')
        self.username = settings.get('MYSQL_USER')
        self.passwd = settings.get('MYSQL_PASSWD')
        self.schema = settings.get('MYSQL_DB')
        self.mysql = Mysql(self.host,self.username,self.passwd,self.schema)
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_item(self, item, spider):
        if item['title'] and item['content']:
            links = item['url'].split('/')
            print links
            if len(links)>=5:
                if links[3]== 'arabic':
                    item['country']='arabic'
                elif links[3]=='zhongwen':
                    item['country']='chinese'
                elif links[3]=='indonesia':
                    item['country']='indonesian'
                elif links[3]=='kyrgyz':
                    item['country']='kyrgyz'
                elif links[3]=='portuguese':
                    item['country']='portuguese'
                elif links[3]=='mundo':
                    item['country']='mundo'
                elif links[3]=='ukrainian':
                    item['country']='ukrainian'
                elif links[3]=='azeri':
                    item['country']='azeri'
                elif links[3]=='afrique':
                    item['country']='french'
                elif links[3]=='japanese':
                    item['country']='japanese'
                elif links[3]=='nepali':
                    item['country']='nepali'
                elif links[3]=='russian':
                    item['country']='russian'
                elif links[3]=='swahili':
                    item['country']='swahili'
                elif links[3]=='urdo':
                    item['country']='urdo'
                elif links[3]=='bengali':
                    item['country']='bengali'
                elif links[3]=='hausa':
                    item['country']='hausa'
                elif links[3]=='gahuza':
                    item['country']='kinyarwanda'
                elif links[3]=='pashto':
                    item['country']='pashto'
                elif links[3]=='sinhala':
                    item['country']='sinhala'
                elif links[3]=='tamil':
                    item['country']='tamil'
                elif links[3]=='uzbek':
                    item['country']='uzbek'
                elif links[3]=='burmese':
                    item['country']='burmese'
                elif links[3]=='hindi':
                    item['country']='hindi'
                elif links[3]=='gahuza':
                    item['country']='kirundi'
                elif links[3]=='persian':
                    item['country']='persian'
                elif links[3]=='somali':
                    item['country']='somali'
                elif links[3]=='turkce':
                    item['country']='turkish'
                elif links[3]=='vietnamese':
                    item['country']='vietnamese'
                elif links[3] == 'news':
                    item['country']='english'
                else:
                    item['country']=None
                if item['country']:
                    self.mysql.insert_message(item)
        return item
'''
        else:
            raise DropItem("empty title in %s" %item["link"])
'''
