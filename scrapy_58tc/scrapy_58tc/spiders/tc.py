import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://cz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify1_A']
    start_urls = ['https://cz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify1_A']

    def parse(self, response):
        # 字符串
        #content = response.text
        # 二进制数据
        #content = response.body

        #print("=====================")
        #print(content)

        span = response.xpath('//title')
        print("===================")
        print(span.extract())