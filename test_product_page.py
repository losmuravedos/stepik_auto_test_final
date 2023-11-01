import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link_end',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]
                         )
def test_guest_can_add_product_to_basket(browser, link_end):
    """
    Test if a guest can add a product to the basket.
    Args:
        browser: The browser object used for testing.
        link_end: The ending of the link to the product page.
    Returns:
        None
    """
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_end}"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_product_to_basket()
    page.product_should_be_in_basket()
    page.basket_price_should_equal_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Test case to verify that a guest user cannot see a success message after adding a product to the basket.
    Parameters:
        browser (WebDriver): The WebDriver instance to use for the test.
    Returns:
        None
    """
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    Test if a guest user cannot see the success message on the product page.
    Parameters:
    - browser: The browser object used for automated testing.
    Returns:
    None
    """
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Test if the success message disappears after adding a product to the basket.
    Parameters:
    - browser: The browser instance to use for testing.
    Returns:
    None
    """
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    """
    Test if a guest user can see the login link on a product page.
    :param browser: The browser object used for testing.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Test if a guest can go to the login page from the product page.
    Args:
        browser: The browser object used for testing.
    Returns:
        None
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
