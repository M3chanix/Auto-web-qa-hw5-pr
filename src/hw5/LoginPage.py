from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        login_page = 'http://192.168.0.190:8081/index.php?route=account/login'
        self.driver.get(login_page)

    def login_as(self, email, password):
        self.driver.find_element(By.CSS_SELECTOR, '#input-email').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, '#input-password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

