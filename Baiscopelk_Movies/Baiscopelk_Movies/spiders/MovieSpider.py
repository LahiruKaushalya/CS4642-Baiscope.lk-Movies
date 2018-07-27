# -*- coding: utf-8 -*-
import scrapy
from Baiscopelk_Movies.items import BaiscopelkMoviesItem

class MovieSpider(scrapy.Spider):
    name = 'MovieSpider'
    def start_requests(self):
        baseUrl = 'https://www.baiscopelk.com/category/%E0%B7%83%E0%B7%92%E0%B6%82%E0%B7%84%E0%B6%BD-%E0%B6%8B%E0%B6%B4%E0%B7%83%E0%B7%92%E0%B6%BB%E0%B7%90%E0%B7%83/%E0%B6%A0%E0%B7%92%E0%B6%AD%E0%B7%8A%E2%80%8D%E0%B6%BB%E0%B6%B4%E0%B6%A7%E0%B7%92/'
        urls = [
            baseUrl,
        ]
        for i in range(2,264):
            urls.append(baseUrl + 'page/' + str(i) + '/')
            
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        content = response.css('#main-content > div.content > div.post-listing.archive-box')
        for link in content.css('h2 > a::attr(href)').extract():
            yield scrapy.Request(url = link, callback = self.parse2)

    def parse2(self, response):
        movie = BaiscopelkMoviesItem()
        content = response.css('#main-content > div.content')
        
        movie['Title'] = content.css('#the-post > div > h1 > span::text').extract_first()
        movie['Date'] = content.css('#the-post > div > p > span.tie-date::text').extract_first()
        movie['Comments'] = content.css('#the-post > div > p > span.post-comments > a::text').extract_first()
        movie['Views'] = content.css('#the-post > div > p > span.post-views::text').extract_first()
        movie['Rating'] = content.css('#the-post > div > div > div > div > div.gdrts-rating-text > strong::text').extract_first()
        movie['Image'] = content.css('img.aligncenter ::attr(src)').extract_first()
        
        yield  movie  

        
        
