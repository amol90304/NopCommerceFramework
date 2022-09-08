from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    btn_Login_xpath = '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button'
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_Login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()
































































# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class LoginPage:
#     textbox_username_id = "email"
#     textbox_username_password = "pass"
#     btn_login_name = "login"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def setUserName(self, username):
#         self.driver.find_element(By.ID, self.textbox_username_id).clear()
#         self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)
#
#     def setPassword(self, password):
#         self.driver.find_element(By.ID, self.textbox_username_password).clear()
#         self.driver.find_element(By.ID, self.textbox_username_password).send_keys(password)
#
#     def clickLoginBtn(self):
#         self.driver.find_element(By.NAME, self.btn_login_name).click()
#
