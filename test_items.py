# import time


def test_add_to_cart_button_existance(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # time.sleep(30)
    assert bool(browser.find_element_by_css_selector('#add_to_basket_form button'))
