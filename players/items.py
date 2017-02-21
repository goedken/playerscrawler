# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Player(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    team = scrapy.Field()
    number = scrapy.Field()
    position = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    age = scrapy.Field()
    college = scrapy.Field()
    experience = scrapy.Field()
    ppg = scrapy.Field()
    apg = scrapy.Field()
    rpg = scrapy.Field()
    per = scrapy.Field()
    image_name = scrapy.Field()
