import pytest
from PageObjects.LoginPage import LoginPage
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_HomePageTitle(self, Setup):
        self.logger.info("***********Test_001_Login************")
        self.logger.info("***********Verifying homepage title************")
        self.driver = Setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.logger.info("***********Homepage title test is passed************")
            self.driver.close()

        else:
            self.driver.get_screenshot_as_file("C:/Users/amols/PycharmProjects/pythonProject/FacebookPOM/Screenshots/SS1.png")
            self.logger.error("***********Home page title test is failed************")
            self.driver.close()

            assert False

    @pytest.mark.regression
    def test_Login(self, Setup):
        self.logger.info("***********Verifying login test ************")
        self.driver=Setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***********login test is passed ************")
            self.driver.close()
        else:
            self.driver.get_screenshot_as_file("C:/Users/amols/PycharmProjects/pythonProject/FacebookPOM/Screenshots/SS2.png")
            self.logger.error("***********login test is failed ************")
            self.driver.close()
            assert False
































# class TC001:
#     baseURL = "https://www.facebook.com"
#     username = 'amol.dd2'
#     password = '8007777402'
#
#     def test_Homepage(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.baseURL)
#         act_title = self.driver.title
#         if act_title == "Facebook – log in or sign up":
#             assert True
#         else:
#             assert False







