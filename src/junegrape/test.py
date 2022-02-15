import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class ReviewTest(unittest.TestCase):
    
    def test_get_frame(self):
        driver = webdriver.Chrome('chromedriver')
        driver.get("http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9788932474427&orderClick=s1a")
        iframes = driver.find_elements_by_css_selector('iframe')
        for iframe in iframes:
            print(iframe.get_attribute('name'))
        self.assertEqual("8", "")

if __name__=="__main__":
    unittest.main()
