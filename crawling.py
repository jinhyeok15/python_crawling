from publisher import Publisher
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from review import Review


class Crawler(Review):
    def __init__(self, url, webpage):
        super().__init__(webpage.columns)
        self.url = url
        self.webpage = webpage
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get(self.url)
        html = self.driver.page_source
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_soup(self):
        html = self.driver.page_source
        self.soup = BeautifulSoup(html, 'html.parser')
        return self

    def next(self):
        self.webpage.next()
        return self
    
    def findtxt(self, elem_name, idx=None):
        elem = self.webpage.getElem(elem_name)
        res_list = self.soup.select(elem)
        if idx:
            string = res_list[idx].text
        else:
            string = res_list[0].text
        return string
    
    def findnum(self, elem_name, idx=None):
        elem = self.webpage.getElem(elem_name)
        res_list = self.soup.select(elem)
        if idx:
            string = res_list[idx].text
        else:
            string = res_list[0].text
        import re
        string = re.sub(r'[^0-9]', '', string)
        return int(string)
    
    def findtxt_and_put(self, elem_name, idx=None):
        txt = self.findtxt(elem_name, idx)
        self.set_review(elem_name, txt)
        return self
    
    def findnum_and_put(self, elem_name, idx=None):
        num = self.findnum(elem_name, idx)
        self.set_review(elem_name, num)
        return self

    def put(self, elem_name, value):
        self.set_review(elem_name, value)
        return self
    
    def click(self, elem_name, idx=None):
        elem = self.webpage.getElem(elem_name)
        if idx:
            button = self.driver.find_element(By.XPATH, elem[idx])
        elif type(elem)==type([]):
            button = self.driver.find_element(By.XPATH, elem[0])
        else:
            button = self.driver.find_element(By.XPATH, elem)
        self.driver.execute_script("arguments[0].click();", button)
        return self

    def click_all(self, elem_name):
        elem = self.webpage.getElem(elem_name)
        for e in elem:
            button = self.driver.find_element(By.XPATH, e)
            self.driver.execute_script("arguments[0].click();", button)
            self.driver.implicitly_wait(1)
        return self

    def exec(self):
        self.driver.close()
        return self

if __name__ == "__main__":
    # yes24 = Publisher.get_instance('yes24')
    # crawler = Crawler("http://www.yes24.com/Product/Goods/1940233", yes24)
    # total_num = crawler.findnum('totalReviewNum')

    # while crawler.row_count < total_num:
    #     for c in range(yes24.contents_count):
    #         try:
    #             crawler\
    #             .click_all('review_more')\
    #             .get_soup()\
    #             .put('publisher_name', yes24.name)\
    #             .findtxt_and_put('date', c)\
    #             .findtxt_and_put('book_name')\
    #             .findtxt_and_put('rating', c)\
    #             .findtxt_and_put('heart', c)\
    #             .findtxt_and_put('content', c)\
    #             .commit()
    #         except IndexError:
    #             crawler.row_count += 1
    #             break
    #     if yes24.page_number%10==0:
    #         crawler.click('next_end_button').next()
    #     else: crawler.click('next_button').next()
    # review_data = crawler.exec()
    # review_data.save()
    from selenium.webdriver.common.keys import Keys
    kyobo = Publisher.get_instance('kyobo')
    crawler = Crawler("http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9788932474427&orderClick=s1a", kyobo)

    total_num = 100
    body = crawler.driver.find_element_by_css_selector('body')
    for i in range(15):
        body.send_keys(Keys.PAGE_DOWN)
        crawler.driver.implicitly_wait(3)
    while crawler.row_count < total_num:
        for c in range(kyobo.contents_count):
            try:
                crawler.get_soup()\
                .put('publisher_name', kyobo.name)\
                .findtxt_and_put('date', c)\
                .findtxt_and_put('book_name')\
                .findtxt_and_put('id', c)\
                .findtxt_and_put('heart', c)\
                .findtxt_and_put('content', c)\
                .commit()
                # print(crawler.show())
            except IndexError:
                crawler.row_count += 1
                break
        if kyobo.page_number%10==0:
            crawler.click('next_end_button').next()
        else: crawler.click('next_button').next()
    comment_data = crawler.exec()
    comment_data.save()
