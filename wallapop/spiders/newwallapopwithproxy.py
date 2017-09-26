import scrapy
from scrapy import Request
from wallapop.items import WallapopItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
import ast
class wallapopSpider(scrapy.Spider):
        name = "newwallapopwithproxy"
        handle_httpstatus_list = [301, 302, 500]#, 403]
	allowed_domains = ['wallapop.com']
	#start_urls = ['https://es.wallapop.com/list/coches']
	start_urls = ['https://es.wallapop.com/list/coches?_p=0&lastItemId=0']
	download_delay = 1.5
	
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
		hrefs = response.css('a.product-info-title ::attr(href)').extract()
		last_href = hrefs[-1]
		last_id = last_href.split('-')
		last_item_id = last_id[-1]

                current_page = response.url  #example https://es.wallapop.com/list/coches?_p=5&lastItemId=1675618585
                current_page1 = current_page.split('&')
                current_page2 = current_page1[0]
                current_page3 = current_page2.split('=')
                number_current_page = int(current_page3[-1])
                number_next_page = number_current_page + 1
                while number_current_page != 3223:
                        next_page = 'https://es.wallapop.com/list/coches?_p='+str(number_next_page)+'&lastItemId='+str(last_item_id)
                        yield scrapy.Request(next_page)
                           
                #or try to set p=0 and lastitemid=0 for the start_url
                #for i in range(1,3224):
                        #next_page = 'https://es.wallapop.com/list/coches?_p='+str(i)+'&lastItemId='+str(last_item_id)
                        #yield scrapy.Request(next_page)   
                        
	        #next_page = response.css('a.more-products-btn.has-infinite ::attr(href)').extract_first()
                #if next_page:
                    #yield scrapy.Request(
                        #response.urljoin(next_page))#,callback=self.parse)                      
                
        def second_page(self, response):
                hxs = Selector(response)
                myItem = response.meta["myItem"]  
                myItem["id_annonce"] = response.xpath('//a[@id="js-detail-add-item-favourite"]/@data-itemid').extract_first()
                myItem["annonce_link"] = response.url
                myItem["contact_nom"] = response.css('h2.card-user-detail-name ::text').extract_first()
                myItem["adresse"] = response.css('div.card-product-detail-location ::text').extract_first()
                
                yield myItem


