from abc import *

class Publisher(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.name = ""
        self.page_number = 1
        self.elements = dict()
        self.contents_count = 0
        self.columns = []
    
    @abstractmethod
    def next(self):
        self.page_number += 1

    @abstractmethod
    def getElem(self, key):
        return self.elements[key]

    @abstractmethod
    def setElem(self, key, value):
        self.elements[key] = value

    @staticmethod
    def get_instance(name):
        if name=='yes24':
            return Yes24()
        elif name=='kyobo':
            return Kyobo()


class Yes24(Publisher):
    def __init__(self) -> None:
        self.name = "yes24"
        self.page_number = 1
        self.elements = {
                    "book_name": 'h2.gd_name',
                    "date": 'div.review_etc > em.txt_date',
                    "rating": 'span.review_rating > span:nth-of-type(1)',
                    "heart": 'span.bWrap > em.yes_b.txt',
                    "content": 'div.review_cont',
                    "totalReviewNum": '#emReviewCountText',
                    "review_more": [
                        '//*[@id="infoset_reviewContentList"]/div[2]/div[2]/a',
                        '//*[@id="infoset_reviewContentList"]/div[3]/div[2]/a',
                        '//*[@id="infoset_reviewContentList"]/div[4]/div[2]/a',
                        '//*[@id="infoset_reviewContentList"]/div[5]/div[2]/a',
                        '//*[@id="infoset_reviewContentList"]/div[6]/div[2]/a',
                    ],
                    "next_button": '/html/body/div/div[8]/div/div[2]/div[13]/div[5]/div[1]/div[1]/div/a[3]',
                    "next_end_button": '//*[@id="infoset_reviewContentList"]/div[7]/div[1]/div/a[12]'
            }
        self.contents_count = 5
        self.columns = ["publisher_name", "date", "book_name", "rating", "heart", "content"]
    
    def next(self):
        super().next()
        self._refresh_next_cursor()
        return self
    
    def _refresh_next_cursor(self):
        self.setElem("next_button", f'/html/body/div/div[8]/div/div[2]/div[13]/div[5]/div[1]/div[1]/div/a[{self.page_number%10+2}]')

    def getElem(self, key):
        return super().getElem(key)
    
    def setElem(self, key, value):
        return super().setElem(key, value)


class Kyobo(Publisher):
    def __init__(self) -> None:
        self.name = "kyobo"
        self.page_number = 1
        self.elements = {
            "book_name": 'div.box_detail_point > h1.title > strong',
            "card_date": 'div.card_news > h4 > em > span',
            "card_id": 'div.card_news > h4 > em > a',
            "card_heart": 'div.area_kp > div.card_news > div.option > a > span',
            "card_content": 'p.part',
            "date": '#list_killngpart ul > li > div.comment_wrap > dl > dd.date',
            "id": '#list_killngpart ul > li > div.comment_wrap > dl > dt.id > a',
            "heart": '#list_killngpart ul > li > div.comment_wrap > div > ul > li > span',
            "content": '#list_killngpart ul > li > div.comment_wrap > dl > dd.comment',
            "review_nav_button": '//*[@id="detailFixedTab"]/div/div[1]/ul/li[3]/a',
            "next_button": '//*[@id="list_killngpart"]/div/div/a[1]',
            "next_end_button": '//*[@id="list_killngpart"]/div/div/a[10]',
            "total": '#killingTotal.total'
        }
        self.contents_count = 5
        self.columns = ['publisher_name', 'date', 'book_name', 'id', 'heart', 'content']
    
    def next(self):
        super().next()
        self._refresh_next_cursor()
    
    def _refresh_next_cursor(self):
        self.setElem('next_button', f'//*[@id="list_killngpart"]/div/div/a[{self.page_number%10}]')

    def getElem(self, key):
        return super().getElem(key)
    
    def setElem(self, key, value):
        return super().setElem(key, value)

if __name__ == "__main__":
    yes24 = Publisher.get_instance('yes24')
    yes24.next().next().next()
    print(yes24.elements['next_button'])
