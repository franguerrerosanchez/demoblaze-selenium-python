from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

def before_scenario(context, scenario):
    chrome_service = ChromeService(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=chrome_service)

def after_scenario(context, scenario):
    context.driver.quit()
