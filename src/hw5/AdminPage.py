from selenium.webdriver.common.by import By

class AdminPage:
    NAVBAR_IMAGE = (By.CSS_SELECTOR, '[href*="common/login"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '[name="username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name="password"]')
    FORGOT_LINK = (By.CSS_SELECTOR, '[href$="forgotten"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    
    def __init__(self, driver):
        self.driver = driver
        admin_page = 'http://192.168.0.190:8081/admin'
        self.driver.get(admin_page)

    def verify_admin_page(self):
        self.driver.find_element(*AdminPage.NAVBAR_IMAGE)
        self.driver.find_element(*AdminPage.USERNAME_INPUT)
        self.driver.find_element(*AdminPage.PASSWORD_INPUT)
        self.driver.find_element(*AdminPage.FORGOT_LINK)
        self.driver.find_element(*AdminPage.LOGIN_BUTTON)


    def login_as_admin(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()


