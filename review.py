import pandas as pd

class Review():
    def __init__(self, columns):
        self.columns = columns
        self.piece = dict()
        self.__reviews = pd.DataFrame(columns=self.columns)
        self.size = 0
        self.row_count = 0

    def commit(self):
        df = pd.DataFrame.from_dict(self.piece)
        self.__reviews = pd.concat([self.__reviews, df], ignore_index=True)
        self.row_count += 1
    
    def set_review(self, colname, value):
        self.piece[colname] = [value]
    
    def get_row_count(self):
        return self.row_count

    def show(self):
        return self.__reviews

    def save(self):
        self.__reviews.to_excel('review.xlsx')
