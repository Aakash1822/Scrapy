from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.utils.project import get_project_settings

from spiders.my_spider import my_Spider
    dispatcher.connect(stop_reactor, signal=signals.spider_closed) 
    spider = my_Spider()
    crawler = Crawler(Settings())
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
	 # scrapy instructions stored in log file
    log.start(logfile=config.log_file_name, loglevel=log.DEBUG, crawler=crawler, logstdout=False)   
    reactor.run()
    show_output()  

def stop_reactor():
    reactor.stop()