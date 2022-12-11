from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select

all_subcategories = (By.CSS_SELECTOR, 'a[class="market-categories__subcategory c-link c-link--text"]')
city_list = (By.CSS_SELECTOR, 'a[class="c-side-nav__link c-link c-link--text js-side-link"]')
car_details = (By.CSS_SELECTOR, 'a[class="u-link-area"]')
location_information = (By.TAG_NAME, 'td')
condition_details = (By.CSS_SELECTOR, 'label[class="c-side-nav__item "]')

select_brand = (By.CSS_SELECTOR, 'select[name="brand"]')
select_model = (By.CSS_SELECTOR, 'select[name="model"]')
categories_details = (By.CSS_SELECTOR, 'label[class="c-side-nav__item"]')
information = (By.TAG_NAME, 'tbody')


class MarketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(f'{self.base_url}/market')

    def open_page_filter(self):
        self.driver.get(f'{self.base_url}/market?location=2191')

    def all_subcategories_is_enabled(self):
        subcategories = self.find_elements(all_subcategories)
        for i in subcategories:
            result = bool(i.is_enabled())
            if result == False:
                return [False, f'link "{i.text}" not enabled']
        return True, ''

    def correct_location_filter(self):
        cites = self.find_elements(city_list)
        for i in range(len(cites)):
            self.driver.get(f'{self.base_url}/market')
            cites = self.find_elements(city_list)
            name_city = cites[i].text
            cites[i].click()
            for num in range(1):
                details = self.find_elements(car_details)
                details[num].click()
                location = self.find_elements(location_information)[0].text.split(' (')[0]
                result = bool(name_city == location)
                if result == False:
                    return [False, f'В фильтре "{name_city}" деталь из города {location}']
                self.driver.back()
        return True, ''

    def categories_details_is_enabled(self):
        categories = self.find_elements(categories_details)
        for i in categories:
            result = bool(i.is_enabled())
            if result == False:
                return [False, f'category "{i.text}" not enabled']
        return True, ''

    def new_detail_filter_is_ok(self):
        self.find_elements(condition_details)[0].click()
        sleep(1)  # нужен слип потому что не успевает кликнуть фильтр состояние
        for i in range(10):
            details = self.find_elements(car_details)
            details[i].click()
            condition = self.find_elements(information)[0].text.find('Состояние новое')
            if condition == -1:
                return False
            self.driver.back()
        return True

    def old_detail_filter_is_ok(self):
        self.find_elements(condition_details)[1].click()
        sleep(1)  # нужен слип потому что не успевает кликнуть фильтр состояние
        for i in range(10):
            details = self.find_elements(car_details)
            details[i].click()
            condition = self.find_elements(information)[0].text.find('Состояние б/у')
            if condition == -1:
                return False
            self.driver.back()
        return True
