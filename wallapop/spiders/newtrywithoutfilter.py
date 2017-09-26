#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import scrapy
from wallapop.items import WallapopItem
import re
from scrapy import Request

class CochesSpider(scrapy.Spider):
    handle_httpstatus_list = [301, 302]
    name = 'newtrywithoutfilter'
    download_delay = 0
    #quotes_base_url = 'https://es.wallapop.com/rest/useritems?_p=3&statuses=published&userId=56953269&total=275'  #published
    #quotes_base_url = 'https://es.wallapop.com/rest/useritems?statuses=published&userId=56953269&total=275&_p=3' #
    #quotes_base_url = 'https://es.wallapop.com/rest/useritems?_p=1&statuses=sold_outside&userId=56953269&total=969'  #outside try 2 urls
    #quotes_base_url = 'https://es.wallapop.com/rest/useritems?statuses=sold_outside&userId=56953269&total=969&_p='  #outside
    #quotes_base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fcoches&total=94124&_p=' #try list coches
    #quotes_base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fprovincia-madrid%2Fcoches&total=21000&_p='#try madrid coches
    #quotes_base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fcoches&total=98609&_p='
    #quotes_base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fprovincia-barcelona%2Fcoches&total=21136&_p=' #barcelone list coches
    #quotes_base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fcoches&total=98609&_p=' #all list coches 14//07
  #quotes_base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fprovincia-madrid%2Fcoches&total=21499&_p=' #madrid coches
    #quotes_base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fmotor-y-accesorios&total=2828497&_p='#16&lastItemId=163981496'
    #start_urls = [quotes_base_url + str(1) + '&lastItemId=164586835'] #list coches all
    #start_urls = [quotes_base_url + str(1) + '&lastItemId=164586835'] #barcelone list coches
    #start_urls = [quotes_base_url + str(1) + '&lastItemId=164586816'] #madrid coches
    
    #try to get users from regions madrid barcelone etc and use their url to extract the dataand do not let scrapy crawl duplicated url
    #verify last item id from json and url
    download_delay = 1.5
    #list_spain_province = ['a-coruna', 'Alacant-Alicante', 'Alava', 'Albacete', 'Almeria', 'Asturias', 'Avila', 'Badajoz', 'Barcelona', 'Burgos', 'Caceres', 
#'Cadiz', 'Cantabria', 'Castello-Castellon', 'Ceuta', 'Cordoba', 'Cuenca', 'Girona', 'Granada', 'Guadalajara', 'Guipuzcoa', 'Huelva', 'Huesca', 'Islas-Baleares', 'Jaen', 'La-Rioja', 'Las-Palmas', 'Leon', 'Lleida', 'Lugo', 'Madrid', 'Malaga', 'Murcia', 'Navarra', 'Ourense', 'Palencia', 'Pontevedra', 'Salamanca', 'Santa-Cruz-de-Tenerife', 'Segovia', 'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia', 'Valladolid', 'Vizcaya', 'Zamora', 'Zaragoza']
    #for province in list_spain_province:
               #total = 21499 #total for first url
               #base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fprovincia-'+province+'%2Fcoches&total='+str(total)+'&_p='  
               #base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fprovincia-'+province+'%2Fcoches&total=21499&_p=' 
                
    
    def start_requests(self):
         #'Ceuta', deleted dont contain coches
        list_spain_province = ['a-coruna', 'Alacant-Alicante', 'Alava', 'Albacete', 'Almeria', 'Asturias', 'Avila', 'Badajoz', 'Barcelona', 'Burgos', 'Caceres', 
'Cadiz', 'Cantabria', 'Castello-Castellon', 'Cordoba', 'Cuenca', 'Girona', 'Granada', 'Guadalajara', 'Guipuzcoa', 'Huelva', 'Huesca', 'Islas-Baleares', 'Jaen', 'La-Rioja', 'Las-Palmas', 'Leon', 'Lleida', 'Lugo', 'Madrid', 'Malaga', 'Murcia', 'Navarra', 'Ourense', 'Palencia', 'Pontevedra', 'Salamanca', 'Santa-Cruz-de-Tenerife', 'Segovia', 'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo', 'Valencia', 'Valladolid', 'Vizcaya', 'Zamora', 'Zaragoza']
        for province in list_spain_province:
               #total = 21499 #total for first url
               #a-coruna dropped 10386 and saved 1613 try to recrawl it later it contains 31000..
               #base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fprovincia-'+province+'%2Fcoches&total=102609245&_p='  #finished province one by one
               self.base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fprovincia-'+province+'%2Fcoches&total=595266545&lastItemId=165179565&_p='
               #base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fcoches&total=102609245&_p='# try the hole list 18/07
               #base_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fprovincia-Burgos%2Fmotor-y-accesorios&total=595266545&_p='#&lastItemId=165179565
               url = self.base_url + str(0)
               #yield Request(url, self.parse) #try callback = self.parse
               yield Request(url, callback = self.parse)
    
    def parse(self, response):
        data = json.loads(response.body)
        for jsonresponse in data.get('items', []):
                item = WallapopItem()
                item["id_annonce"] = jsonresponse.get('itemId')
                item_url = jsonresponse.get('url')
                item["annonce_link"] = 'https://es.wallapop.com/item/' + item_url
                #item["annonce_date"] = jsonresponse.get('itemId')
                #'author': jsonresponse.get('author', {}).get('name'),
                item["contact_id"] = jsonresponse.get('sellerUser', {}).get('userId') 
                item["contact_nom"] = jsonresponse.get('sellerUser', {}).get('microName')
                user_url = jsonresponse.get('sellerUser', {}).get('url')
                item["contact_url"] = 'https://es.wallapop.com' + user_url
                item["titre_annonce"] = jsonresponse.get('title')
                item["gategorie_url"] = jsonresponse.get('categoryUrl') 
                try:
                        item["version"] = jsonresponse.get('itemCar', {}).get('version')
                        item["annee"] = jsonresponse.get('itemCar', {}).get('year') 
                        item["modele"] = jsonresponse.get('itemCar', {}).get('model') 
                        item["marque"] = jsonresponse.get('itemCar', {}).get('brand') 
                        item["km"] = jsonresponse.get('itemCar', {}).get('km') 
                        item["boite"] = jsonresponse.get('itemCar', {}).get('gearbox')  
                        item["carburant"] = jsonresponse.get('itemCar', {}).get('engine')
                        item["couleur"] = jsonresponse.get('itemCar', {}).get('color') 
                        item["puissance"] = jsonresponse.get('itemCar', {}).get('horsepower') 
                        item["body_type"] = jsonresponse.get('itemCar', {}).get('body_type') 
                        item["num_portes"] = jsonresponse.get('itemCar', {}).get('num_doors') 
                        item["num_places"] = jsonresponse.get('itemCar', {}).get('num_seats')  
                        
		        item["image_url"] = jsonresponse.get('pictureURL')
		        item["vendu"] = jsonresponse.get('sold')#boolean 
		        item["reservee"] = jsonresponse.get('reserved')#boolean 
		        item["price"] = jsonresponse.get('salePrice') #without euro symbol
		        item["prix"] = jsonresponse.get('price') #with euro symbol
		        item["code_postale"] = jsonresponse.get('itemLocation', {}).get('zip') 
		        item["province"] = jsonresponse.get('itemLocation', {}).get('regionName')
		        item["ville"] = jsonresponse.get('itemLocation', {}).get('city') 
		        item["adresse"] = jsonresponse.get('itemLocation', {}).get('fullAddress')
		        item["longitude"] = jsonresponse.get('itemLocation', {}).get('approximatedMapLongitude')
		        item["latitude"] = jsonresponse.get('itemLocation', {}).get('approximatedMapLatitude')
		        bb = jsonresponse.get('description') 
		        item["date_publication"] = jsonresponse.get('publishDateStr') #exist on coches per province response_url
			item["response_url"] = response.url
		        #description = jsonresponse.get('description')
		        #item["contact_phone"] = jsonresponse.get('itemId')
		except:
                       pass
                try: 
                        cc = bb.replace('-','')
	             	item["contact_phone"] = re.findall(r"\D(\d{9})\D", cc)  
	             	#myItem["agence_cp"] = re.search(r'.*(\d{5}(\-\d{4})?)$', myItem["agence_adresse"])
	        except:
	              pass
                
                yield item 
                
		    #yield {
		      #  itemId = item.get('itemId'), 
		        #'author': item.get('author', {}).get('name'),
		       # 'title': item.get('title'),
		        #'description': item.get('description'),
		        #'nextPage': data.get('nextPage'),
		       # 'lastItemId': data.get('lastItemId'),
		    #}
		#if data['nextPage'] > 0:
		next_page = data['nextPage'] 
		#if data['nextPage'] != -2:
		last_item_id = data['lastItemId']
		total = data['total']
		#new_url = 'https://es.wallapop.com/rest/seoitems?path=%2Flist%2Fprovincia-'+self.province+'%2Fcoches&total=21499&_p='+str(next_page)
		#response = response.url
		response = self.base_url
		cc = response.split('&')
		#try:#added 04/08 because it raised an exception
		cc[-1] = str('_p='+str(next_page))
		cc[-2] = str('lastItemId='+str(last_item_id))
		cc[-3] = str('total='+str(total))
		cc = '&'.join(cc)
		yield scrapy.Request(cc)
		#except:
		#	pass
	    



