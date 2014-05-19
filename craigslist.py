#craiglist.py
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from craiglist.items import CraiglistItem

class craig(CrawlSpider):
    name = "craig"
    allowed_domains = ["chicago.craigslist.org"]
    start_urls = ["https://chicago.craigslist.org/sof"]


#Extracts software engineering jobs from index page     
    rules = [
    Rule(SgmlLinkExtractor(allow=("http://chicago.craigslist.org/sof/index200.html")), follow=True),
    Rule(SgmlLinkExtractor(allow=()), callback='parse_item')
]
   

#Parse function for extracting the Title,Link,Description,Compensation and Job Type from Add.
    def parse_item(self,response):
        self.log('Hi, this is an item page! %s' % response.url)
        sel=Selector(response)
        item=CraiglistItem()
        item['title'] = sel.xpath('//h2[@class="postingtitle"]/text()').extract()
        item['link'] = sel.xpath('//span[@class="pl"]/@href').extract()
        item['desc'] = sel.xpath('//section[@id="postingbody"]/text()').extract()
        item['compensation'] = sel.xpath('//div[@class="bigattr"]/text()').extract()
        item['jobtype'] =sel.xpath ('//p[@class="attrgroup"]/span/text()').extract()
        return item
