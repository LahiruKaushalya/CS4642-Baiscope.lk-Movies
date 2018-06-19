# -*- coding: utf-8 -*-
import scrapy


class CarcrawlerSpider(scrapy.Spider):
    name = 'carcrawler'
    start_urls = ['https://www.hitad.lk/EN/cars?page=0',]
    # for i in range(1,10):
    #     start_urls.append('https://www.hitad.lk/EN/cars?page=' + str(i*25) +'/')
        

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'cars-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body) 
        
