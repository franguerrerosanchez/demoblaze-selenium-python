from behave import given, when, then
from selenium import webdriver
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage

@given('I am on the demoblaze.com homepage')
def go_to_homepage(context):
    context.driver = webdriver.Chrome()
    context.home_page = HomePage(context.driver)
    context.home_page.open()

@when('I view the {product_name} details')
def view_product_details(context, product_name):
    context.product_name = product_name
    context.home_page.view_product_details(product_name)
    context.product_detail_page = ProductDetailPage(context.driver)

@when('I add the product to the cart')
def add_product_to_cart(context):
    context.product_detail_page.add_to_cart()

@when('I navigate to the cart')
def navigate_to_cart(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.open()

@then('I should see the product "{product_name}" in the cart')
def step_impl(context, product_name):
    assert context.cart_page.is_product_in_cart(product_name), f"Product '{product_name}' not found in cart"

@then('I should see exactly 1 unit of the product "{product_name}" in the cart')
def step_impl(context, product_name):
    expected_quantity = 1
    actual_quantity = context.cart_page.get_product_quantity(product_name)
    assert actual_quantity == expected_quantity, f"Expected {expected_quantity} unit of product '{product_name}' in cart, but found {actual_quantity}"

@then('I close the browser')
def step_impl(context):
    context.driver.quit()