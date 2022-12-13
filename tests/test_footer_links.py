from pages.footer_links_page import FooterLinksPage
from time import sleep
import pytest


def test_help_link(driver):
    footer = FooterLinksPage(driver)
    footer.open_page()
    assert footer.help_link_is_correct()


def test_support_link(driver):
    footer = FooterLinksPage(driver)
    footer.open_page()
    assert footer.support_link_is_correct()


def test_brand_link(driver):
    footer = FooterLinksPage(driver)
    footer.open_page()
    assert footer.brand_link_is_correct()


def test_vk_link_is_correct(driver):
    footer = FooterLinksPage(driver)
    footer.open_page()
    footer.click_vk_link()
    footer.switch_to_window()
    assert footer.url == 'https://vk.com/drive2'


def test_telegram_is_correct(driver):
    footer = FooterLinksPage(driver)
    footer.open_page()
    footer.click_telegram_link()
    footer.switch_to_window()
    assert footer.url == 'https://t.me/drive2russia'


def test_footer_links_is_correct(driver):
    footer = FooterLinksPage(driver)
    footer.open_page()
    assert footer.other_footer_link()


def test_cars_button(driver):
    menu = FooterLinksPage(driver)
    menu.open_page()
    menu.click_cars_button()
    assert menu.title_name == 'Машины'


def test_experience_button(driver):
    menu = FooterLinksPage(driver)
    menu.open_page()
    menu.click_experience_button()
    assert menu.title_name == 'Бортжурналы'


def test_communities_button(driver):
    menu = FooterLinksPage(driver)
    menu.open_page()
    menu.click_communities_button()
    assert menu.title_name == 'Сообщества'


def test_shops_button(driver):
    menu = FooterLinksPage(driver)
    menu.open_page()
    menu.click_shops_button()
    assert menu.title_name == 'Автосервисы и магазины'


def test_market_button(driver):
    menu = FooterLinksPage(driver)
    menu.open_page()
    menu.click_market_button()
    assert menu.title_name == 'Барахолка'


def test_new_featured(driver):
    menu = FooterLinksPage(driver)
    menu.open_page()
    menu.click_new_featured()
    assert menu.title_name == 'Самое интересное'


def test_cars_for_sale_button(driver):
    menu = FooterLinksPage(driver)
    menu.open_page()
    menu.click_cars_for_sale_button()
    assert menu.title_name == 'Продажа машин с историей'
