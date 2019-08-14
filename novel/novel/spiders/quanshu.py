# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel.items import NovelItem

class QuanshuSpider(CrawlSpider):
    name = 'quanshu'
    allowed_domains = ['www.quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/']

    rules = (
        # http://www.quanshuwang.com/book_16621.html
        # http://www.quanshuwang.com/book_164429.html
        Rule(LinkExtractor(
            allow=r'.*/book_[\d]*\.html'), callback='parse_item', follow=True),
        # http://www.quanshuwang.com/book/135/135052/49203331.html
        Rule(LinkExtractor(
            allow=r'.*/book/[\d]*/[\d]*/[\d]*\.html'), callback='parse_page', follow=True),

    )

    def parse_item(self, response):

        #    name = response.xpath("//div[@class='b-info']/h1/text()").get()
        #    description = response.xpath("//div[@id='waa']/text()").get()

        page_url = response.xpath(
            "//li/a[@class='poptext']/@href").get()  # 获取第一页就可以
    #    author = response.xpath("//div[@class='bookDetail']/dl[2]/dd/text()").get()## 作者不一定能获取到

    #    print("作者："+ author)
    #    print("书名："+ name)

    #    print("介绍："+ description)
    #    print("第一页： "+ page_url)

        scrapy.Request(page_url)

    def parse_page(self, response):
        base_path='G:/novel/'

        name = response.xpath("//*[@id='direct']/a[3]/text()").get()
        chapter = response.xpath("//*[@id='direct']/text()[4]").get()
        content = response.xpath("//*[@id='content']/text()").getall()
        it = NovelItem(name=name,chapter=chapter,content=content)
        yield it
        # 干脆用管道
        # print(name, chapter)

        # //*[@id="content"]/text()[1]

        # print(content)
