from selenium.webdriver.common.by import By

class AdminCatalogPage:

    def __init__(self, driver):
        self.driver = driver
        admin_catalog_page = 'http://192.168.0.190:8081/admin/catalog/product'
        self.driver.get(admin_catalog_page)

    def add_new_product(self, product_name, model):
        self.driver.find_element(By.CSS_SELECTOR, '[data-original-title="Add New"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '#input_name1').send_keys(product_name)
        self.driver.find_element(By.CSS_SELECTOR, '#input-meta-title1').send_keys(product_name)
        self.driver.find_element(By.CSS_SELECTOR, '#input_model').send_keys(model)
        self.driver.find_element(By.CSS_SELECTOR, '[name="product_seo_url[0][1]"]').send_keys(product_name)
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        return product_name
    
    def delete_product(self, product_name):
        # Заполнить фильтр
        self.driver.find_element(By.CSS_SELECTOR, '[name="filter_name"]').send_keys(product_name)
        # Нажать кнопку фильтра
        self.driver.find_element(By.CSS_SELECTOR, '#button-filter').click()
        # Нажать на галочку в списке товаров
        self.driver.find_element(By.CSS_SELECTOR, '[name="selected[]"]').click()
        # Нажать delete button
        self.driver.find_element(By.CSS_SELECTOR, '.btn-danger').click()
        # В алерте нажать ок
        self.driver.switch_to.alert.accept()


