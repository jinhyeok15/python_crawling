import pandas as pd

class Review():
    def __init__(self):
        self.columns = ["publisher_name", "date", "book_name", "rating", "heart", "content"]
        self.piece = dict()
        self.__reviews = pd.DataFrame(columns=self.columns)

    def commit(self):
        df = pd.DataFrame.from_dict(self.piece)
        self.__reviews.append(df, ignore_index=True)
    
    def set_review(self, colname, value):
        self.piece[colname] = value

    def show(self):
        return self.__reviews


if __name__=="__main__":
    review = Review()
    print(review.show())
