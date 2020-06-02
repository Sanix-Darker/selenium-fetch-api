from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from os import environ

import urllib.parse as urlparse
from urllib.parse import parse_qs
from app.settings import GECKO_PATH

class SeleniumScrap():
    def __init__(self, results_box):
        self.results_box = results_box
        self.option = Options()
        self.option.headless = True
        self.driver = webdriver.Firefox(options=self.option, executable_path=GECKO_PATH)

    def get(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(1)  # in seconds

        element = self.driver.find_element_by_xpath(self.results_box)
        html_content = element.get_attribute('outerHTML')

        self.driver.quit()

        return html_content
