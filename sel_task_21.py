from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.saucedemo.com/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

# cookie1 created before login
my_cookie1 = {'name': 'before_login', 'value': 'b_login'}
driver.add_cookie(my_cookie1)
m = driver.get_cookies()

# before login cookie display on a console
print("Before login cookies", m)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
sleep(3)
driver.find_element(By.ID, "login-button").click()
sleep(2)

# cookie1 created after login
my_cookie2 = {'name': 'after_login', 'value': 'a_login'}
driver.add_cookie(my_cookie2)
k= driver.get_cookies()

# after login cookie display on a console
print("After login cookies",k)
