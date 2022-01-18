from douban.items import DoubanItem
import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):

        movies_data = response.xpath("//ol[@class='grid_view']/li/div[@class='item']/div[@class='info']")

        for item in movies_data:

            ret = DoubanItem()
            ret['movie_link'] = item.xpath(".//a/@href").get()
            ret['movie_name'] = item.xpath(".//a/span[@class='title']/text()").get()
            ret['movie_rating'] = item.xpath(".//span[@class='rating_num']/text()").get()
            yield ret

        next_page = response.xpath("//div[@class='paginator']//link[@rel='next']/@href").get()
        next_page = response.urljoin(next_page)
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)

        print("Finished!")

    # a / @ href

