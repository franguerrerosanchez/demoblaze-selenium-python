from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductDetailPage(BasePage):
    add_to_cart_button = (By.XPATH, "//a[contains(text(), 'Add to cart')]")

    def add_to_cart(self):
        add_to_cart_button = self.wait_for_clickable_element(self.add_to_cart_button)
        add_to_cart_button.click()
