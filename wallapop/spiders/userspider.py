import json
import scrapy

class CochesSpider(scrapy.Spider):
    name = 'userspider'
    quotes_base_url = 'https://es.wallapop.com/rest/useritems?statuses=published&userId=56953269&total=300&_p='  #published
    #quotes_base_url = 'https://es.wallapop.com/rest/useritems?statuses=published&userId=56953269&total=275&_p=3' #
    #quotes_base_url = 'https://es.wallapop.com/rest/useritems?_p=1&statuses=sold_outside&userId=56953269&total=969'  #outside try 2 urls
    #quotes_base_url = 'https://es.wallapop.com/rest/useritems?statuses=sold_outside&userId=56953269&total=1400&_p='  #outside
    #quotes_base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fcoches&total=94124&_p=' #try list coches
    #quotes_base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fmotor-y-accesorios&total=2828497&_p='#16&lastItemId=163981496'
    start_urls = [quotes_base_url + str(1)]
    download_delay = 1.5
    
    def parse(self, response):
        data = json.loads(response.body)
        for item in data.get('items', []):
            yield {
                'itemId': item.get('itemId'),
                #'author': item.get('author', {}).get('name'),
                'title': item.get('title'),
                #'description': item.get('description'),
                'nextPage': data.get('nextPage'),
            }
        if data['nextPage']:
            next_page = data['nextPage'] #+ 1
            yield scrapy.Request(self.quotes_base_url + str(next_page) )



