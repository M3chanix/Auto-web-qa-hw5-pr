from selenium.webdriver.common.by import By

class RegisterPage:
    FIRST_NAME_INPUT = (By.XPATH, '//*[@id="input-firstname"]')
    LOGIN_PAGE_LINK = (By.XPATH, '//*[@id="content"]/p/a')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="input-password"]')
    SUBSCRIBE_YES_CHECKBOX = (By.CSS_SELECTOR, '.radio-inline')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

    def __init__(self, driver):
        self.driver = driver
        register_page = 'http://192.168.0.190:8081/index.php?route=account/register'
        self.driver.get(register_page)

    def verify_register_page(self):
        self.driver.find_element(*RegisterPage.FIRST_NAME_INPUT)
        self.driver.find_element(*RegisterPage.LOGIN_PAGE_LINK)
        self.driver.find_element(*RegisterPage.PASSWORD_INPUT)
        self.driver.find_element(*RegisterPage.SUBSCRIBE_YES_CHECKBOX)
        self.driver.find_element(*RegisterPage.CONTINUE_BUTTON)

    def register_new_user(self, first_name, last_name, email, phone, password):
        self.driver.find_element(*RegisterPage.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '#input-lastname').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '#input-email').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, '#input-telephone').send_keys(phone)
        self.driver.find_element(*RegisterPage.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#input-confirm').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '[name="agree"]').click()
        self.driver.find_element(*RegisterPage.CONTINUE_BUTTON).click()



