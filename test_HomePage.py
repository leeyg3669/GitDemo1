import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.baseclass import BaseClass

print("Hello")
print("Hello, my name is")
print("Hello, Brave Lee")

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

            homepage = HomePage(self.driver)
            homepage.getName().send_keys(getData["firstname"])
            homepage.getEmail().send_keys(getData["lastname"])
            homepage.getCheckBox().click()
            self.selectOptionByText(homepage.getGender(), getData["gender"])
            homepage.submitForm().click()

            alertText = homepage.getSuccessMessage().text

            assert ("Success" in alertText)
            self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self,request):
     return request.param