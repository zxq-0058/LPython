# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanPipeline:
    def process_item(self, item, spider):
        # print(item['movie_link'], item['movie_name'], item['movie_rating'])
        return item
