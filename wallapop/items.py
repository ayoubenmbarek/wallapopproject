# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WallapopItem(scrapy.Item):
     annonce_link = scrapy.Field()
     #annonce_date = scrapy.Field()
     id_annonce = scrapy.Field()
     contact_id = scrapy.Field()
     response_url = scrapy.Field()
     contact_nom = scrapy.Field()
     prix = scrapy.Field()
     price = scrapy.Field()
     contact_url = scrapy.Field()
     titre_annonce = scrapy.Field()
     gategorie_url = scrapy.Field()
     version = scrapy.Field()
     annee = scrapy.Field()
     modele = scrapy.Field()
     marque = scrapy.Field()
     km = scrapy.Field()
     boite = scrapy.Field()	
     carburant = scrapy.Field()
     couleur = scrapy.Field()
     puissance = scrapy.Field()		
     body_type = scrapy.Field()
     num_portes = scrapy.Field()
     num_places = scrapy.Field()
     image_url = scrapy.Field()
     vendu = scrapy.Field()
     reservee = scrapy.Field()
     code_postale = scrapy.Field()
     province = scrapy.Field()
     ville = scrapy.Field()
     adresse = scrapy.Field()
     longitude = scrapy.Field()
     latitude = scrapy.Field()
     contact_phone = scrapy.Field()
     description = scrapy.Field()
     date_publication = scrapy.Field()

    #pass
#["annonce_link","annonce_date","id_annonce","contact_id", "contact_nom", "contact_url", "titre_annonce", "gategorie_url", "version", "annee", "modele", "marque", "km", "boite", "carburant", "couleur", "puissance", "body_type", "num_portes", "num_places", "image_url", "vendu", "reservee", "code_postale", "province", "ville", "adresse", "longitude", "latitude", "contact_phone", "description"] 
