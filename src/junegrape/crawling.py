from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By  # for find_element_xxx
from .bascket import Bascket

# _get_driver_name_from_path, Crawler.findnum
import re


__driver_names = [
    'chromedriver',
    'geckodriver',
]


def _get_driver_name_from_path(path):
    for name in __driver_names:
        p = re.compile(rf'({name})')
        if p.search(path):
            return name
    return None


class Scanner:
    def __init__(self, url, driver_path=None):
        driver_name = _get_driver_name_from_path(driver_path)
        if driver_name=='chromedriver':
            self.driver = webdriver.Chrome(driver_name)
        elif driver_name=='geckodriver':
            self.driver = webdriver.Firefox(driver_name)
        else:
            raise Exception('Unvalid driver name')
        
        self.driver.get(url)
    
    def get_driver(self):
        return self.driver
        
    def get_soup(self):
        html = self.driver.page_source
        return BeautifulSoup(html, 'html.parser')


class SeleniumMixin:
    def click(self, elem_name, idx=None):
        pass
    
    def click_all(self, elem_name):
        pass


class Bs4Mixin:
    def findtxt(self, elem_name, idx=None):
        pass
    
    def findnum(self, elem_name, idx=None):
        pass
    
    def find_all(self, elem_name):
        pass
    
    def find(self, elem_name):
        pass


class Crawler(Bascket, SeleniumMixin, Bs4Mixin):
    def __init__(self, webpage, columns, driver_path=None) -> None:
        Bascket(columns).__init__(columns)
        self.webpage = webpage
        scanner = Scanner(webpage.url, driver_path)
        self.driver = scanner.get_driver()
        self.soup = scanner.get_soup()

    def refresh_soup(self):
        html = self.driver.page_source
        self.soup = BeautifulSoup(html, 'html.parser')
        return self

    def next(self):
        self.webpage.next()
        return self
    
    # Bs4Mixin implementation
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
        string = re.sub(r'[^0-9]', '', string)
        return int(string)
    
    def find_all(self, elem_name):
        elem = self.webpage.getElem(elem_name)
        return self.soup.select(elem)
    
    def find(self, elem_name):
        elem = self.webpage.getElem(elem_name)
        return self.soup.select_one(elem)
    
    # SeleniumMixin implementation
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

    # method by using mixin
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

    def exec(self):
        self.driver.close()
        return self
