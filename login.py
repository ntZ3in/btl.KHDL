from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login(driver, username, password):
    driver.get("http://facebook.com")

    txtUser = driver.find_element("id", "email")
    txtUser.send_keys(username)

    txtPass = driver.find_element("id", "pass")
    txtPass.send_keys(password)

    txtPass.send_keys(Keys.ENTER)