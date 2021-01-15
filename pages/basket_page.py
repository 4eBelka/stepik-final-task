from .base_page import BasePage
from .locators import BasketPageLocators
import pytest

class BasketPage(BasePage):
    def checking_no_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_BUY), \
        "Button buy is presented, but should not be"
        
    def checking_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE_EMPTY), \
        "No message indicating that the basket is empty"