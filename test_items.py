
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_shop_has_add_to_basket_button(browser):
    browser.get(link)

    # time.sleep(15)

    # изначально полагаем, что кнопки нет
    button_found = False

    try:
        # пытаемся найти кнопку, если селектор выдаст исключение NoSuchElementException
        # то button_found останется false, иначе ставим button_found в True
        button = browser.find_element_by_css_selector("button.btn-add-to-basket")
        button_found = True
    except:
        pass

    assert button_found == True, "shop page doesn't have 'Add to basket' button!"


