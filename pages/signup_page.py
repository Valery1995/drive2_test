from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

authentication_buttons = (By.CLASS_NAME, 'o-group')
registration_option_buttons = (By.CSS_SELECTOR, 'form[class="u-mobile-100 u-100"]')  # 4 варианта регистации
registration_field = (By.CSS_SELECTOR, 'input[type="email"]')
home_button = (By.CSS_SELECTOR, 'a[rel="home"]')
mail_and_phone_button = (By.CSS_SELECTOR, 'button[type="button"]')
email_field = (By.CSS_SELECTOR, 'input[autocomplete="email"]')
phone_field = (By.CSS_SELECTOR, ' input[autocomplete="tel"]')
register_button = (By.CSS_SELECTOR, 'button[data-type="yandex"]')
text_attention = (By.CSS_SELECTOR, 'div[class="c-bubble__content"]')
field_error = (By.CLASS_NAME, 'field-validation-error')
mobile_number_verification = (By.CSS_SELECTOR, 'h1[class="x-title"]')

user_agreement = (By.CSS_SELECTOR, 'a[href="/agreement/"]')
site_rules = (By.CSS_SELECTOR, 'a[href="/rules/"]')
data_use = (By.CSS_SELECTOR, 'a[href="/data-use/"]')
personal_agreement = (By.CSS_SELECTOR, 'a[href="/agreement/personal/"]')
business_account = (By.CSS_SELECTOR, 'a[href="/business/"]')

title_text = (By.CLASS_NAME, 'l-page-header')


class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_signup_button(self):
        self.find_element(authentication_buttons).click()

    def registration_vk_button(self):
        self.find_elements(registration_option_buttons)[0].click()

    def registration_yandex_button(self):
        self.find_elements(registration_option_buttons)[1].click()

    def registration_apple_button(self):
        self.find_elements(registration_option_buttons)[2].click()

    def registration_google_button(self):
        self.find_elements(registration_option_buttons)[3].click()

    def click_home_button(self):
        self.find_element(home_button).click()

    def registration_by_mail_and_phone(self):
        self.find_element(mail_and_phone_button).click()

    def enter_login_details(self, email, phone):
        self.find_element(email_field).send_keys(email)
        self.find_element(phone_field).send_keys(phone)
        self.find_element(register_button).click()

    def check_field_error_text(self):
        return self.find_elements(field_error)[0].text

    def introduced_only_login(self, email):
        self.find_element(email_field).send_keys(email)
        self.find_element(register_button).click()
        return self.find_element(text_attention).text

    def introduced_only_phone(self, phone):
        self.find_element(phone_field).send_keys(phone)
        self.find_element(register_button).click()
        return self.find_element(text_attention).text

    def mobile_verification(self):
        return self.find_element(mobile_number_verification)

    def click_user_agreement(self):
        self.find_element(user_agreement).click()

    def check_title_text(self):
        return self.find_element(title_text).text

    def switch_to_window(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])

    def click_site_rules(self):
        self.find_element(site_rules).click()

    def click_data_use(self):
        self.find_element(data_use).click()

    def click_personal_agreement(self):
        self.find_element(personal_agreement).click()

    def click_business_account(self):
        self.find_element(business_account).click()

    @property
    def url(self):
        return self.driver.current_url
