from selenium.webdriver.common.by import By

class CatalogPage:
    BREADCRUMB = (By.CSS_SELECTOR, '.breadcrumb')
    PRODUCT_LIST = (By.CSS_SELECTOR, '.list-group')
    FIRST_PRODUCT = (By.CSS_SELECTOR, '.product-layout')
    LIMIT_INPUT = (By.CSS_SELECTOR, '#input-limit')
    SORT_INPUT = (By.CSS_SELECTOR, '#input-sort')

    def __init__(self, driver):
        self.driver = driver
        catalog_page = 'http://192.168.0.190:8081/laptop-notebook'
        self.driver.get(catalog_page)

    def verify_catalog_page(self):
        self.driver.find_element(*CatalogPage.BREADCRUMB)
        self.driver.find_element(*CatalogPage.PRODUCT_LIST)
        self.driver.find_element(*CatalogPage.FIRST_PRODUCT)
        self.driver.find_element(*CatalogPage.LIMIT_INPUT)
        self.driver.find_element(*CatalogPage.SORT_INPUT)


    def verify_product(self, product_name):
        return self.driver.find_element(By.CSS_SELECTOR, f'[href*="{product_name}"]')


