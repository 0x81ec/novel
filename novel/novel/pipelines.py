# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

class NovelPipeline(object):

    def __init__(self):
        self.base_path="G:/novel/"
        self.count = 0
       
    def process_item(self, item, spider):
        # 对于每一个书名，创建一个文件夹
        # 对于每一页书，存一个文件
        # 判断文件夹是否存着，不存在创建，存着则直接保存
        path = self.base_path+item["name"].strip()
        print(path)
        # 创建目录
        if not os.path.exists(path):
            os.mkdir(path)
            self.count+=1
        # 写入文件
        with open(path+"/"+item['chapter'].strip().replace(">", "")+".txt",mode="w",encoding='utf-8') as tf:
            for c in item['content']:
                tf.writelines(c)
                # 自带换行符，咱就不加了
        print("第"+str(self.count)+"部小说")
        # return item
