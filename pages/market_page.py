from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

all_subcategories = (By.CSS_SELECTOR, 'a[class="market-categories__subcategory c-link c-link--text"]')


class MarketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(f'{self.base_url}/market')
        sleep(2)

    def all_subcategories_is_enabled(self):
        subcategories = self.find_elements(all_subcategories)
        for i in range(len(subcategories)):
            result = bool(subcategories[i].is_enabled())
            if result == False:
                print(f'link №{i+1} not enabled')
                return False
        return True



