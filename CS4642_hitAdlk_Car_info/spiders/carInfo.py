# -*- coding: utf-8 -*-
import scrapy


class CarinfoSpider(scrapy.Spider):
    name = 'carInfo'
    def start_requests(self):
        urls = [
            'http://www.hitad.lk/EN/cars?page=0',
        ]
        for i in range(1,239):
            urls.append('http://www.hitad.lk/EN/cars?page=' + str(i*25))
            
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        for car in response.css('ul.cat-ads'):
            link = car.css('div.clearfix a::attr(href)').extract()[0]
            yield scrapy.Request(url = link, callback = self.parse2)


    def parse2(self, response):
        for line in response.css('div.fw_b'):
            data = line.css('div.col-lg-12::text').extract()
            yield{
                'Published By' : data[0],
                'Sale Type': data[1],
                'Location': data[2],
                'Sub Category' : data[3],
                'Brand': data[4],
                'Model': data[5],
                'Transmission Type' : data[6],
                'Year': data[7],
                'Fuel Type': data[8],
            }

        
        
