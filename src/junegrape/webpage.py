from abc import *

class WebPage:
    def __init__(self, name="", elements={}) -> None:
        self.name = name
        self.page_number = 1
        self.elements = elements
    
    def next(self):
        self.page_number += 1

    def getElem(self, key):
        return self.elements[key]

    def setElem(self, key, value):
        self.elements[key] = value
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
