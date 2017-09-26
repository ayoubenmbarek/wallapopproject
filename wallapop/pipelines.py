# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#from scrapy.conf import settings
from scrapy.exceptions import DropItem
from wallapop.items import WallapopItem
#from scrapy import log

class WallapopPipeline(object):
    def process_item(self, item, spider):
        return item

from scrapy.exceptions import DropItem

class SpecificWordsPipeline(object):
        def process_item(self, item, spider): 
                #item = WallapopItem()
                specific_words = ["remolque", "remolques", "moto", "motos", "bicicleta", "bicicletas", "busco", "bike", "bikes", "caja de cambios", "herramientas", "llanta", "llantas", "kart", "buggi", "buggis", "buggy", "buggys", "bultaco", "burgman",  "conac", "puente", "quad", "quads", "bombilla", "bombillas", "vespa", "scoopy", "yamaha", "piagio", "piaggio", "kawasaki", "kawazaki", "MBK", "kymco", "scooter", "scooters", "velo solex", "velosolex", "bici", "bicis", "gilera" "buell", "daelim", "motobecane", "KTM", "voxan", "malaguti", "ducatti", "ducati", "cagiva", "husqvarna", "laverda", "barco", "barcos", "barca", "barcas", "embarcacion", "reloj", "se busca", "busco", "compro", "se compra", "culata", "culatas", "sortija", "sortijas", "varilla", "varillas", "asiento", "asientos", "patinete", "patinetes", "elevador", "elevadores", "maleta", "maletas", "maquina", "maquinas", "IMR 160", "IMR 140", "polini", "caravana", "caravanas", "actualizamos", "cochesss", "Por SOLO 97 EUR", "licencia", "taxi", "taxis"]
                for word in specific_words:
                    if word in item["titre_annonce"]:
                        raise DropItem("Unauthorized word %s" % item)
                    else:
                         return item
        
        
                
class PricePipeline(object):

    #vat_factor = 1.15

    def process_item(self, item, spider):
        #item = WallapopItem()
        item["price"] = []
        if  item["price"] < 800:
            #if item['price_excludes_vat']:
             #   item['prix'] = item['prix'] * self.vat_factor
            raise DropItem("Price is less then 800 euro %s" % item)
        else:
            return item
            

# Let say that our items have an unique id, but our spider returns multiples items with the same id: this function will dropthe duplicates
class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        #item = WallapopItem()#test with this item if default won't work
        if item["id_annonce"] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item["id_annonce"])
            return item
