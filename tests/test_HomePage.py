import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

from TestData.HomePageData import HomePageData
from tests.pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def testFormSubmission(self,getData):
        self.driver.get("http://www.clickngotravels.com/dubai.html?Name=&Last+Name=&Mobile=&Email=&message=")
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("First name is:" + getData["firstname"])
        homePage.getFirstName(getData["firstname"])
        homePage.getSecondName(getData["lastname"])
        homePage.getMobile(getData["Contact"])
        homePage.getEmail(getData["Email"])
        homePage.getMessage(getData["Message"])
        #homePage.clickSubmit()
        # message = homePage.getSuccessMsg()
        # print(message)
        # assert "submitted successfully!" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param

