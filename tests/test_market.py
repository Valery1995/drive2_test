from pages.market_page import MarketPage
from time import sleep
import pytest
from selenium.webdriver.support.ui import Select


def test_all_subcategories_is_enabled(driver):
    market = MarketPage(driver)
    market.open_page()
    assert market.all_subcategories_is_enabled()[0], market.all_subcategories_is_enabled()[1]


def test_location_filter(driver):
    market = MarketPage(driver)
    market.open_page()
    assert market.correct_location_filter()[0], market.correct_location_filter()[1]


def test_categories_is_enabled(driver):
    market = MarketPage(driver)
    market.open_page_filter()
    assert market.categories_details_is_enabled()[0], market.categories_details_is_enabled()[1]


def test_new_detail_filter(driver):
    condition = MarketPage(driver)
    condition.open_page_filter()
    assert condition.new_detail_filter_is_ok()


def test_old_detail_filter(driver):
    condition = MarketPage(driver)
    condition.open_page_filter()
    assert condition.old_detail_filter_is_ok()


def test_brand_car_filter(driver):
    market = MarketPage(driver)
    market.open_page_filter()
    assert market.brand_car_filter_is_ok()


def test_model_car_filter(driver):
    market = MarketPage(driver)
    market.open_page_filter()
    assert market.model_car_filter_is_ok()
