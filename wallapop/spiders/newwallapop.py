import scrapy
from scrapy import Request
from wallapop.items import WallapopItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
import ast
class wallapopSpider(scrapy.Spider):
        name = "newwallapop"
        handle_httpstatus_list = [301, 302, 500]#, 403]
	allowed_domains = ['wallapop.com']
	start_urls = ['https://es.wallapop.com/list/coches']
	download_delay = 0
	
	def parse(self, response):
	
                myItem = WallapopItem()        
                container = response.css('div.card-product-product-info')
                for link in container:
                      myItem["response_url"] = response.url  
                      url = link.css('a.product-info-title ::attr(href)').extract_first() 
                      full_url = response.urljoin(url)
                      request = Request(full_url, callback = self.second_page)#, dont_filter=True) 
                      request.meta['myItem'] = myItem
                      yield request   

	        next_page = response.css('a.more-products-btn.has-infinite ::attr(href)').extract_first()
                if next_page:
                    yield scrapy.Request(
                        response.urljoin(next_page))#,callback=self.parse)                      
                
        def second_page(self, response):
                hxs = Selector(response)
                myItem = response.meta["myItem"]  
                myItem["id_annonce"] = response.xpath('//a[@id="js-detail-add-item-favourite"]/@data-itemid').extract_first()
                myItem["annonce_link"] = response.url
                myItem["contact_nom"] = response.css('h2.card-user-detail-name ::text').extract_first()
                myItem["adresse"] = response.css('div.card-product-detail-location ::text').extract_first()
                
                yield myItem


