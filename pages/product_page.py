from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import pytest

class ProductPage(BasePage): 
    def add_product_to_basket(self):
        self.click_on_the_add_to_basket_button()
        self.checking_message()
        self.checking_product_in_basket_and_store()
        self.checking_price_in_basket_and_store()
    
    def click_on_the_add_to_basket_button(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()
        self.solve_quiz_and_get_code()
    
    def checking_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_MESSAGE), "Product not added to basket"
     
    def checking_product_in_basket_and_store(self):
        store_product = self.browser.find_element(*ProductPageLocators.STORE_PRODUCT)
        basket_product = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT)
        assert store_product.text == basket_product.text, "Products do not match"

    def checking_price_in_basket_and_store(self):
        store_price = self.browser.find_element(*ProductPageLocators.STORE_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert store_price.text == basket_price.text, "Prices do not match"