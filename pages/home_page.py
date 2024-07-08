from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://www.demoblaze.com"

    def open(self):
        self.driver.get(self.base_url)

    def view_product_details(self, product_name):
        product_image_locator = (By.CSS_SELECTOR, "#tbodyid > div:nth-child(1) > div > a > img")
        product_image = self.wait_for_clickable_element(product_image_locator)
        product_image.click()
