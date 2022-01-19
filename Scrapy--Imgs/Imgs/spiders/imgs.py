import scrapy
from Imgs.items import ImgsItem

class ImgsSpider(scrapy.Spider):
    name = 'imgs'
    start_urls = ['https://www.tukuppt.com/soback/liujinwenli1203/__time_0_0_0_0_0_0_1.html/']

    def parse(self, response):

        print("Process Begin!")
        imgs_list = response.xpath("//a[@class='img']/img")

        for item in imgs_list:
            ret = ImgsItem()
            ret['src'] = item.xpath("./@data-original").get()
            ret['src'] = "https:" + ret['src']
            yield ret

        print("Accessed Finished!")
