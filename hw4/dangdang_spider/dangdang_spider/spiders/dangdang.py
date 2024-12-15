import scrapy

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=example']  # 请替换 "example" 为实际的搜索关键词

    def parse(self, response):
        # 提取商品名称和价格
        products = response.xpath('//p[@class="name" and @name="title"]/a/text()').getall()
        prices = response.xpath('//span[@class="search_now_price"]/text()').getall()
        print("Products:", products)
        print("Prices:", prices)

        for product, price in zip(products, prices):
            # 打印结果到终端
            print({'name': product.strip(), 'price': price.strip()})


