from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    PRICE = (By.CSS_SELECTOR, '.list-unstyled h2')
    WISHLIST_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')
    THUMBNAIL = (By.CSS_SELECTOR, '.thumbnail')
    ADD_CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')
    RATING_STARS = (By.CSS_SELECTOR, '.rating')

    def __init__(self, driver):
        self.driver = driver
        product_page = 'http://192.168.0.190:8081/laptop-notebook/hp-lp3065'
        self.driver.get(product_page)

    def verify_product_page(self):

        self.driver.find_element(*ProductPage.PRICE)
        self.driver.find_element(*ProductPage.WISHLIST_BUTTON)
        self.driver.find_element(*ProductPage.THUMBNAIL)
        self.driver.find_element(*ProductPage.ADD_CART_BUTTON)
        
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.visibility_of_element_located(ProductPage.RATING_STARS))


