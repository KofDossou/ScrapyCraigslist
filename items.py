# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


#Items  we want from Job Add.
class CraiglistItem(Item):
    # define the fields for your item here like:
   desc = Field()
   title = Field()
   link = Field()
   compensation=Field()
   jobtype=Field()
