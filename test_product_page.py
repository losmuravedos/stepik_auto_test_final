import pytest
from faker import Faker
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.go_to_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        fake_person = Faker()
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email=fake_person.email(), password=fake_person.password())
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.add_product_to_basket()
        page.product_should_be_in_basket()
        page.basket_price_should_equal_product_price()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.parametrize('link_end',
                         ["0", "1", "2", "3", "4", "5", "6",
                          pytest.param("7", marks=pytest.mark.xfail),
                          "8", "9"]
                         )
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link_end):
    url_link = f"{link}?promo=offer{link_end}"
    page = ProductPage(browser=browser, url=url_link)
    page.open()
    page.add_product_to_basket()
    page.product_should_be_in_basket()
    page.basket_price_should_equal_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message_disappear()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.should_be_empty_basket_message()
