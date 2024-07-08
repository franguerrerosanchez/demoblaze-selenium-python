from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.demoblaze.com/cart.html"
        self.product_name_locator = (By.XPATH, "//td[@class='cart_product']/a[contains(@href, 'prod=')]")
        self.product_quantity_locator = (By.XPATH, "//td[@class='cart_quantity']/input[@name='quantity']")

    def open(self):
        self.driver.get(self.base_url)

    def is_product_in_cart(self, product_name):
        product_locator = (By.XPATH, f"//td[@class='cart_product']/a[contains(@href, 'prod=') and contains(text(), '{product_name}')]")
        try:
            product_element = self.driver.find_element(*product_locator)
            return product_element.is_displayed()
        except NoSuchElementException:
            return False

    def get_product_quantity(self, product_name):
        product_locator = (By.XPATH, f"//td[@class='cart_product']/a[contains(@href, 'prod=') and contains(text(), '{product_name}')]/../../td[@class='cart_quantity']/input[@name='quantity']")
        try:
            quantity_element = self.driver.find_element(*product_locator)
            return int(quantity_element.get_attribute('value'))
        except NoSuchElementException:
            return 0
