from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hw5.MainPage import MainPage
from hw5.CatalogPage import CatalogPage
from hw5.ProductPage import ProductPage
from hw5.AdminPage import AdminPage
from hw5.RegisterPage import RegisterPage
from hw5.AdminCatalogPage import AdminCatalogPage
from hw5.LoginPage import LoginPage


def test_main_page(driver):
    MainPage(driver).verify_main_page()

def test_catalog_page(driver):
    CatalogPage(driver).verify_catalog_page()

def test_product_page(driver):
    ProductPage(driver).verify_product_page()

def test_admin_page(driver):
    AdminPage(driver).verify_admin_page()

def test_register_page(driver):
    RegisterPage(driver).verify_register_page()



def test_add_product(driver):
    AdminPage(driver).login_as_admin('user', 'bitnami')
    product_name = AdminCatalogPage(driver).add_new_product('new_laptop_1', 'new_model')
    CatalogPage(driver).verify_product(product_name)

def test_delete_product(driver):
    AdminPage(driver).login_as_admin('user', 'bitnami')
    AdminCatalogPage(driver).delete_product('new_laptop_1')
    assert not CatalogPage(driver).verify_product('new_laptop_1')

def test_register_new_user(driver):
    user = {'first_name': 'first_name', 
            'last_name': 'last_name', 
            'email': 'test@user.com', 
            'phone': '88005555555', 
            'password': 'test_password'}
    
    RegisterPage(driver).register_new_user(**user)
    LoginPage(driver).login_as(user['email'], user['password'])

def test_change_currency(driver):
    prev_currency = MainPage(driver).get_current_currency()
    MainPage(driver).change_currency()
    active_currency = MainPage(driver).get_current_currency()
    assert active_currency != prev_currency

