from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p:first-child strong")
    BASKET_PRODUCT = (By.CSS_SELECTOR, "#messages :first-child div.alertinner strong")
    STORE_PRICE = (By.CSS_SELECTOR, "#content_inner p.price_color")
    STORE_PRODUCT = (By.CSS_SELECTOR, "#content_inner h1")