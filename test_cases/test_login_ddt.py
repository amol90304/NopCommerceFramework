import time

import pytest
from PageObjects.LoginPage import LoginPage
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import ExcelUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "C:/Users/amols/PycharmProjects/pythonProject/FacebookPOM/TestData/LoginData.xlsx"

    logger = LogGen.loggen()



    def test_Login_ddt(self, Setup):
        self.logger.info("********Test_002_DDT_Login********")
        self.logger.info("***********Verifying login test ************")
        self.driver=Setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getrowcount(self.path, 'Sheet1')
        print("Numeber of rows in Excel", self.rows)


        # lst_status = []     # Empty list variable

        for r in range (2, self.rows+1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***Passed")
                    self.lp.clickLogout()
                    # lst_status.append("Pass")
            #     elif self.exp == "Fail":
            #         self.logger.info("****Failed****")
            #         self.lp.clickLogout()
            #         lst_status.append("Fail")
            #     elif act_title != exp_title:
            #         if self.exp == 'Pass':
            #             self.logger.info("***Failed***")
            #             lst_status.append("Fail")
            #         elif self.exp == 'Fail':
            #             self.logger.info("***Passed***")
            #             lst_status.append("Pass")
            #
            # if "Fail" not in lst_status:
            #     self.logger.info("Login DDT test passed...")
            #     self.driver.close()
            #     assert True
            # else:
            #     self.logger.info("Login DDT test failed...")
            #     self.driver.close()
            #     assert False
            #
            # self.logger.info("*****End of DDT test*****")
            # self.logger.info("*****Completed TC_Login DDT_002*********")
            #
            #
            #

















        # self.lp.setUserName(self.username)
        # self.lp.setPassword(self.password)
        # self.lp.clickLogin()
        # act_title = self.driver.title
        #
        # if act_title == "Dashboard / nopCommerce administration":
        #     assert True
        #     self.logger.info("***********login test is passed ************")
        #     self.driver.close()
        # else:
        #     self.driver.get_screenshot_as_file("C:/Users/amols/PycharmProjects/pythonProject/FacebookPOM/Screenshots/SS2.png")
        #     self.logger.error("***********login test is failed ************")
        #     self.driver.close()
        #     assert False

























Framewordk








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







