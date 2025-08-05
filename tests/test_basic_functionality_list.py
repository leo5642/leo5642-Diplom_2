from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.page_home import HomePage
from locators.locators1 import LocatorsCollector
from locators.url import UrlCollector
from pages.page_order_scooter import PageOrder
import allure

class Testbookscollector1:
    def test_use_burron_(self, browser, setup_classes):
        home_page = HomePage
        home_page.click_button_kom()
        current_url = driver.current_url
        assert current_url == UrlCollector.url_home