from urllib.request import urlopen
from junegrape.crawling import Crawler
from page import instagram


crawler = Crawler(instagram, ["image_url"], "chromedriver")

import time
time.sleep(25)

crawler.refresh_soup()
bodies = crawler.find_all("image_body")
for i, body in enumerate(bodies):
    image_url = body.div.div.img["src"]
    with urlopen(image_url) as f:
        with open('./image/' + "다독이챌린지" + str(i) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
crawler.exec()
