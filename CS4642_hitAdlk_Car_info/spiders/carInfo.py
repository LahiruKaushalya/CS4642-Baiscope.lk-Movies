# -*- coding: utf-8 -*-
import scrapy


class CarinfoSpider(scrapy.Spider):
    name = 'carInfo'
    def start_requests(self):
        urls = [
            'http://www.hitad.lk/EN/cars?page=0',
        ]
        for i in range(1,4):
            urls.append('http://www.hitad.lk/EN/cars?page=' + str(i*25))
            
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1][10:]
        filename = 'CarInfo-page-%s.html' % str(int(int(page)/25) + 1)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
