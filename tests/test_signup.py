from pages.signup_page import SignupPage
from time import sleep
import pytest

INVALID_LOGIN = [
    {'email': 'mail@something', 'phone': '12345678901'},
    {'email': '@something.com', 'phone': '1234567890'},
    {'email': 'mailsomething.com', 'phone': '123456789'}
]

INVALID_PHONE = [
    {'phone': '123456', 'error': 'Телефон должен быть не менее 9 символов, а получено 7 символов.'},
    {'phone': '123456789012345', 'error': 'Телефон должен быть не более 15 символов, а получено 16 символов.'}
]


def test_vk_registration(driver):
    signup = SignupPage(driver)
    signup.open_page()
    signup.click_signup_button()
    signup.registration_vk_button()
    assert signup.url.find('vk.com') != -1


def test_yandex_registration(driver):
    signup = SignupPage(driver)
    signup.open_page()
    signup.click_signup_button()
    signup.registration_yandex_button()
    assert signup.url.find('passport.yandex.ru') != -1


def test_apple_registration(driver):
    signup = SignupPage(driver)
    signup.open_page()
    signup.click_signup_button()
    signup.registration_apple_button()
    assert signup.url.find('appleid.apple.com') != -1


def test_google_registration(driver):
    signup = SignupPage(driver)
    signup.open_page()
    signup.click_signup_button()
    signup.registration_google_button()
    assert signup.url.find('accounts.google.com') != -1


def test_home_button(driver):
    signup = SignupPage(driver)
    signup.open_page()
    signup.click_signup_button()
    signup.click_home_button()
    assert signup.url == 'https://www.drive2.ru/'


def test_only_login(driver):
    signup = SignupPage(driver)
    signup.open_page()
    signup.click_signup_button()
    signup.registration_by_mail_and_phone()
    assert signup.introduced_only_login(email='aniskevich@mail.ru') == 'Укажите телефон'


def test_only_phone(driver):
    signup = SignupPage(driver)
    signup.open_page()
    signup.click_signup_button()
    signup.registration_by_mail_and_phone()
    assert signup.introduced_only_phone(phone='375299631731') == 'Укажите адрес электронной почты'


@pytest.mark.parametrize('creds', INVALID_LOGIN)
def test_registration_invalid_email(driver, creds):
    signup = SignupPage(driver)
    signup.open_page()
    signup.click_signup_button()
    signup.registration_by_mail_and_phone()
    signup.enter_login_details(email=creds['email'], phone=creds['phone'])
    assert signup.check_field_error_text() == (f"Проверьте правильность написания email адреса. "
                                               f"Он может содержать только латинские буквы, цифры, "
                                               f"дефис, плюс, подчеркивание, точки и @.")


@pytest.mark.parametrize('creds', INVALID_PHONE)
def test_registration_invalid_phone(driver, creds):
    signup = SignupPage(driver)
    signup.open_page()
    signup.click_signup_button()
    signup.registration_by_mail_and_phone()
    signup.enter_login_details(email='something@mail.ru', phone=creds['phone'])
    assert signup.check_field_error_text() == creds['error']


def test_correct_login_details(driver):
    signup = SignupPage(driver)
    signup.open_page()
    signup.click_signup_button()
    signup.registration_by_mail_and_phone()
    signup.enter_login_details(email='correct@mail.ru', phone='+375229631731')
    assert signup.mobile_verification().is_displayed()

