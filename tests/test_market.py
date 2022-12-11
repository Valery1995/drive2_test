from pages.market_page import MarketPage
from time import sleep
import pytest


# @pytest.mark.parametrize('creds', all_subcategories_is_enabled())
def test_all_subcategories_is_enabled(driver):
    market = MarketPage(driver)
    market.open_page()
    assert market.all_subcategories_is_enabled()[0], market.all_subcategories_is_enabled()[1]


def test_location_filter(driver):
    market = MarketPage(driver)
    market.open_page()
    assert market.correct_location_filter()[0], market.correct_location_filter()[1]

