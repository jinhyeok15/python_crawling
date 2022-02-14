from abc import *

class Publisher(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.name = ""
        self.params = dict()
        self.elements = dict()
        self.contents_count = 0
    
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def getElem(self, key):
        pass

    @staticmethod
    def get_instance(name):
        if name=='yes24':
            return Yes24()


class Yes24(Publisher):
    def __init__(self) -> None:
        self.name = "yes24"
        self.params = {
                    'Sort': 1,
                    'PageNumber': 1,
                    'Type': 'ALL'
                }
        self.elements = {
                    "book_name": ('h2', 'class', 'gd_name'),
                    "date": ('em', 'class', 'txt_date'),
                    "rating": ('span', 'class', 'review_rating'),
                    "heart": ('em', 'class', 'yes_b txt'),
                    "content": ('div', 'class', 'review_cont'),
                    "totalReviewNum": ('em', 'id', 'emReviewCountText')
            }
        self.contents_count = 5
    
    def next(self):
        self.params['PageNumber'] += 1
        return self
    
    def getElem(self, key):
        return self.elements[key]
    

if __name__ == "__main__":
    yes24 = Publisher.get_instance('yes24')
    yes24.next().next().next()
    print(yes24.params['PageNumber'])
