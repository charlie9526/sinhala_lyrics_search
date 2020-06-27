# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SinhalaSongsLyricsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    songName = scrapy.Field()
    songNameSinglish = scrapy.Field()
    artists = scrapy.Field()
    genre = scrapy.Field()
    lyricsCreater = scrapy.Field()
    music = scrapy.Field()
    movie = scrapy.Field()
    key = scrapy.Field()
    beat = scrapy.Field()
    lyrics = scrapy.Field()
    views = scrapy.Field()
