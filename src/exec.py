from junegrape.crawling import Crawler
from page import instagram


crawler = Crawler(instagram, ["image_url"], "chromedriver")

import time
time.sleep(20)

crawler.refresh_soup()

print(crawler.find("test"))
crawler.exec()
