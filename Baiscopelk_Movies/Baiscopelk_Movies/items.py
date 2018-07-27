# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiscopelkMoviesItem(scrapy.Item):
   
    Title = scrapy.Field()
    Date = scrapy.Field()
    Comments = scrapy.Field()
    Views = scrapy.Field()
    Rating = scrapy.Field()
    Image = scrapy.Field()
