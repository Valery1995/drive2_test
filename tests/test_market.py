from pages.market_page import MarketPage
from time import sleep
import pytest


def test_asdas(driver):
    market = MarketPage(driver)
    market.open_page()
    for i in market.all_subcategories_is_enabled():
        print(i)
        assert i

