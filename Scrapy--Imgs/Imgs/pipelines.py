import scrapy
from scrapy.pipelines.images import ImagesPipeline
class ImgsPipeline(ImagesPipeline):

    # 根据图片的src返回图片的数据
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['src'])

    # 存储路径
    def file_path(self, request, response=None, info=None):
        img_name = request.url.split('/')[-3].replace('!', '')
        return img_name

    # 返回给下一个被执行的管道类
    def item_completed(self, results, item, info):
        return item
