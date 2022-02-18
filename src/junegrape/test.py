import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from crawling import _get_driver_name_from_path

URL = "http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9788932474427&orderClick=s1a"
driver = webdriver.Chrome()


class CrawlerTest(unittest.TestCase):

    def setUp(self) -> None:
        driver.get(URL)
        return super().setUp()
    def tearDown(self) -> None:
        driver.close()
        return super().tearDown()
    
    def test_get_driver_page_source(self):
        page_source = driver.page_source
        self.assertEqual(page_source[0], '<')

    def test_get_driver_name_from_path(self):
        self.assertEqual(_get_driver_name_from_path('C:/python_study/chromedriver/chromedriver.exe'), 'chromedriver')
    
    # frame을 trace해서 driver가 원하는 xpath에 접근 가능 하도록 하기 test
    # def test_trace_xpath(self):


def make_suite(testcase: unittest.TestCase, tests: list) -> unittest.TestSuite:
    return unittest.TestSuite(map(testcase, tests))


if __name__=="__main__":
    crawler_test_suite = make_suite(CrawlerTest, ['test_get_driver_name_from_path'])
    suites = unittest.TestSuite([crawler_test_suite])
    unittest.TextTestRunner(verbosity=1).run(suites)
