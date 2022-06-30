from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    CURRENCY_SWITCH = (By.ID, 'form-currency')
    SLIDE_PANNEL = (By.ID, 'slideshow0')
    SUPPORT_PHONE = (By.CSS_SELECTOR, 'ul.list-inline > li')
    CART_BUTTON = (By.CSS_SELECTOR, '#cart button')
    FEATURED_LIST = (By.CSS_SELECTOR, '.product-thumb')

    def __init__(self, driver):
        self.driver = driver
        main_page = 'http://192.168.0.190:8081/'
        self.driver.get(main_page)

    def verify_main_page(self):

        self.driver.find_element(*MainPage.CURRENCY_SWITCH)

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(MainPage.SLIDE_PANNEL))

        self.driver.find_element(*MainPage.SUPPORT_PHONE)
        self.driver.find_element(*MainPage.CART_BUTTON)
        self.driver.find_element(*MainPage.FEATURED_LIST)

    
    def find_product(self, product_name):
        self.driver.find_element(By.CSS_SELECTOR, '[name="search"]').send_keys(product_name)
        self.driver.find_element(By.CSS_SELECTOR, '#search > span > button').click()
    
    def change_currency(self):
        self.driver.find_element(By.CSS_SELECTOR, '#form-currency').click()

        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="EUR"]')))
        self.driver.find_element(By.CSS_SELECTOR, '[name="EUR"]').click()

    def get_current_currency(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#form-currency > div > button > strong').text[-1]

