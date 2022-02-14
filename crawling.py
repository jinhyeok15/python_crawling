from publisher import Yes24
from bs4 import BeautifulSoup
from review import Review
import requests


class Crawler(Review):
    def __init__(self, url, publisher):
        super().__init__()
        self.url = url
        self.publisher = publisher
        self.review_count = 0

    def get_soup(self):
        req = requests.get(self.url, params=self.publisher.params)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
    def work(self):
        soup = self.get_soup()
        
        for i in range(self.publisher.contents_count):
            try:
                self.set_review('publisher_name', self.publisher.name)
                
                elem = self.publisher.getElem('date')
                res_list = soup.find_all(elem[0], {elem[1]: elem[2]})
                self.set_review('date', res_list[i].text)

                elem = self.publisher.getElem('book_name')
                res = soup.find(elem[0], {elem[1]: elem[2]})
                self.set_review('book_name', res.text)

                elem = self.publisher.getElem('rating')
                res_list = soup.find_all(elem[0], {elem[1], elem[2]})
                self.set_review('rating', res_list[i].text)

                elem = self.publisher.getElem('heart')
                res_list = soup.find_all(elem[0], {elem[1], elem[2]})
                self.set_review('heart', res_list[i].text)

                elem = self.publisher.getElem('content')
                res_list = soup.find_all(elem[0], {elem[1], elem[2]})
                self.set_review('content', res_list[i].text)

                self.commit()
                self.review_count += 1
            except IndexError:
                self.review_count += 1
                break
    
    def next(self):
        self.publisher.next()
    
    def get_total_num(self):
        soup = self.get_soup()
        elem = self.publisher.getElem('totalReviewNum')
        string = soup.find(elem[0], {elem[1]: elem[2]}).string
        import re
        string = re.sub(r'[^0-9]', '', string)
        return int(string)

    def exec(self):
        total_num = self.get_total_num()
        while self.review_count < total_num:
            self.work()
            self.next()
        return self

if __name__ == "__main__":
    yes24 = Yes24()
    crawler = Crawler("http://www.yes24.com/Product/Goods/1940233", yes24)
    review_data = crawler.exec()
    print(review_data.show())
