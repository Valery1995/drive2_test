from pages.market_page import MarketPage
from time import sleep
import pytest


# @pytest.mark.parametrize('creds', all_subcategories_is_enabled())
def test_all_subcategories_is_enabled(driver):
    market = MarketPage(driver)
    market.open_page()
    assert market.all_subcategories_is_enabled()





