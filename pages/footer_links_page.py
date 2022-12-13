from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

help_link = (By.CSS_SELECTOR, 'a[data-testid="footer-links.help"]')
support_link = (By.CSS_SELECTOR, 'a[data-testid="footer-links.support"]')
brand_link = (By.CSS_SELECTOR, 'a[data-testid="footer-links.brand"]')
vk_link = (By.CSS_SELECTOR, 'a[data-testid="footer-links.vk"]')
telegram_link = (By.CSS_SELECTOR, 'a[data-testid="footer-links.telegram"]')
app_link = (By.CSS_SELECTOR, 'a[data-testid="footer-links.apps"]')
all_footer_links = (By.CSS_SELECTOR, 'a[class="c-link c-link--current"]')

title = (By.CSS_SELECTOR, 'h1[class=x-title]')
request = (By.CSS_SELECTOR, 'div[class="wizard-header padding-top-0"]')
badge = (By.CSS_SELECTOR, 'h3[class="c-cp-header"]')
app_title = (By.CSS_SELECTOR, 'h1[class="mm-header"]')


class FooterLinksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(f'{self.base_url}/featured-topics')

    def help_link_is_correct(self):
        link_help = self.find_element(help_link)
        link_help_text = link_help.text
        link_help.click()
        title_test = self.find_element(title).text
        return link_help_text == title_test

    def support_link_is_correct(self):
        self.find_element(support_link).click()
        return self.find_element(request).text == 'Отправить запрос'

    def brand_link_is_correct(self):
        self.find_element(brand_link).click()
        return self.find_elements(badge)[1].text == 'Фото'

    @property
    def url(self):
        return self.driver.current_url

    def switch_to_window(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    def click_vk_link(self):
        self.find_element(vk_link).click()

    def click_telegram_link(self):
        self.find_element(telegram_link).click()

    def other_footer_link(self):
        for i in range(6, 13):
            link_name = self.find_elements(all_footer_links)[i].text
            self.find_elements(all_footer_links)[i].click()
            title_text = self.find_element(title).text
            if link_name == 'Правила сайта':
                if title_text != 'Основной закон DRIVE2':
                    return False
                continue
            if link_name == 'Реклама и сотрудничество':
                if title_text != 'Рекламa и сотрудничество':
                    return False
                continue
            if link_name != title_text:
                return False
            self.driver.back()
        return True


