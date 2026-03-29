from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = MainPageLocators

    def click_modal_window(self):
        self.click(self.locators.MODAL_WINDOW)

    def open(self):
        self.driver.get(self.locators.URL)
        return self

    def click_stock(self):
        self.click(self.locators.STOCK)

    def click_delivery_terms(self):
        self.click(self.locators.DELIVERY_TERMS)

    def click_payment(self):
        self.click(self.locators.PAYMENT)

    def wait_our_promotions(self):
        return self.wait_element(self.locators.OUR_PROMOTIONS)

    def wait_delivery_header(self):
        return self.wait_element(self.locators.DELIVERY_HEADER)

    def wait_payment_header(self):
        return self.wait_element(self.locators.PAYMENT_HEADER)

    def click_pizza_button_navbar(self):
        self.click(self.locators.PIZZA_BUTTON_NAVBAR)

    def wait_pizza_header(self):
        return self.wait_element(self.locators.PIZZA_HEADER)

    def click_main_image(self):
        self.click(self.locators.MAIN_IMAGE)

    def wait_main_title(self):
        return self.wait_element(self.locators.MAIN_TITLE)

    def click_drinks_button_navbar(self):
        self.click(self.locators.DRINKS_BUTTON_NAVBAR)

    def wait_drinks_header(self):
        return self.wait_element(self.locators.DRINKS_HEADER)

    def click_hot_snacks_navbar(self):
        self.click(self.locators.HOT_SNACKS_NAVBAR)

    def wait_hot_snacks_header(self):
        return self.wait_element(self.locators.HOT_SNACKS_HEADER)

    def click_combo_navbar(self):
        self.click(self.locators.COMBO_NAVBAR)

    def wait_combo_header(self):
        return self.wait_element(self.locators.COMBO_HEADER)

    def click_pizza_sauces_navbar(self):
        self.click(self.locators.PIZZA_SAUCES_NAVBAR)

    def wait_pizza_sauces_header(self):
        return self.wait_element(self.locators.PIZZA_SAUCES_HEADER)

    def scroll_caption_product(self):
        self.scroll_element(self.locators.CAPTION_PRODUCT)

    def click_caption_product(self):
        self.click(self.locators.CAPTION_PRODUCT)

    def click_size_l_button(self):
        self.click(self.locators.SIZE_L_BUTTON)

    def scroll_cart_button(self):
        self.scroll_element(self.locators.CART_BUTTON)

    def click_cart_button(self):
        self.click(self.locators.CART_BUTTON)

    def click_place_order_button(self):
        self.click(self.locators.PLACE_ORDER_BUTTON)

    def wait_buyer_form_title(self):
        return self.wait_element(self.locators.BUYER_FORM_TITLE)

    def click_pizzeria_button(self):
        self.click(self.locators.PIZZERIA_BUTTON)

    def wait_pizzeria_header(self):
        return self.wait_element(self.locators.PIZZERIA_HEADER)

    def click_free_shipping_conditions_button(self):
        self.click(self.locators.FREE_SHIPPING_CONDITIONS_BUTTON)

    def click_payment_button_footer(self):
        self.click(self.locators.PAYMENT_BUTTON_FOOTER)

    def click_privacy_policy_button(self):
        self.click(self.locators.PRIVACY_POLICY_BUTTON)

    def wait_privacy_policy_header(self):
        return self.wait_element(self.locators.PRIVACY_POLICY_HEADER)

    def click_public_offer_button(self):
        self.click(self.locators.PUBLIC_OFFER_BUTTON)

    def wait_offer_header(self):
        return self.wait_element(self.locators.OFFER_HEADER)