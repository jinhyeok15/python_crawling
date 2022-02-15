from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By  # for find_element_by_xpath
from .bascket import Bascket


class Crawler(Bascket):
    def __init__(self, url, webpage, columns):
        super().__init__(columns)
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
    
    def find_all(self, elem_name):
        elem = self.webpage.getElem(elem_name)
        return self.soup.select(elem)
    
    def find(self, elem_name):
        elem = self.webpage.getElem(elem_name)
        return self.soup.select_one(elem)

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
        return super()
