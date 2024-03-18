import pytest

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.CheckoutPage import CheckoutPage
from pageObject.HomePage import HomePage
from utilities.baseclass import BaseClass

print("Hello")
print("Hello My name is")
print("Hello Brave Lee")

#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        #checkoutpage = CheckoutPage(self.driver)
        products = checkoutpage.getCardTitle()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmpage = checkoutpage.checkOutItems()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifyLinkPresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in successText



















