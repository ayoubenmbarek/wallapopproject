# -*- coding: utf-8 -*-

# Scrapy settings for wallapop project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wallapop'

SPIDER_MODULES = ['wallapop.spiders']
NEWSPIDER_MODULE = 'wallapop.spiders'

COOKIES_ENABLED = False #added 13/07
#AJAXCRAWL_ENABLED = True #added 13/07

RETRY_ENABLED = True #added 14/07
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wallapop (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

RANDOM_UA_PER_PROXY = True
USER_AGENT_LIST = "/home/databiz41/useragents.txt"  
HTTPPROXY_ENABLED = True  
HTTP_PROXY = 'http://127.0.0.1:8128'
RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
PROXY_LIST = '/home/databiz41/proxy_list.txt'
DOWNLOAD_HANDLERS = {
  's3': None,
}
RANDOMIZE_DOWNLOAD_DELAY = True
FEED_EXPORT_FIELDS = ["response_url", "annonce_link", "id_annonce", "contact_id", "contact_nom", "contact_url", "titre_annonce", "date_publication", "gategorie_url", "version", "annee","modele","marque", "km", "prix", "boite", "carburant", "couleur", "puissance", "body_type", "num_portes", "num_places", "image_url", "vendu", "reservee", "code_postale", "province", "ville", "adresse", "longitude", "latitude", "contact_phone", "description"] 
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False #uncommented 14/07 commented 19/07
REDIRECT_ENABLED = False #added 14/07
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wallapop.middlewares.WallapopSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'wallapop.middlewares.MyCustomDownloaderMiddleware': 543,
     #'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware', #added 13/07 # Whether the AjaxCrawlMiddleware will be enabled. You may want to enable it for broad crawls.
     #'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware', #added 13/07 #To make sure Scrapy respects robots.txt make sure the middleware is enabled and the ROBOTSTXT_OBEY setting is enabled.
     #'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
     #'scrapy_proxies.RandomProxy': 100,
     #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1, 
     #'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    #'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
     #'wallapop.middlewares.ProxyMiddleware': 410,
     #'wallapop.middlewares.RandomUserAgentMiddleware': 400,
     #'wallapop.middlewares.RetryChangeProxyMiddleware': 600, 



}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
    # 'scrapy.extensions.httpcache.FilesystemCacheStorage', #added 14/07
#}
HTTPCACHE_STORAGE = True

#The directory to use for storing the (low-level) HTTP cache. If empty, the HTTP cache will be disabled. If a relative path is given, is taken relative to the project data dir.
HTTPCACHE_DIR = "/home/databiz41/wallapop/wallapop/cache_dir"


# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'wallapop.pipelines.WallapopPipeline': 300,
    #'wallapop.pipelines.PricePipeline': 300,
    #'wallapop.pipelines.DuplicatesPipeline': 300, 
    #'wallapop.pipelines.SpecificWordsPipeline': 300,
}
#LOG_FILE = "wallapoplogs5.log"
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True #added13/07
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
