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
