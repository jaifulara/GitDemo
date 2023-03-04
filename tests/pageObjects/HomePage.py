from selenium.webdriver.common.by import By

from tests.pageObjects import CheckoutPage
from tests.pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")
    firstName = (By.NAME, "Name")
    lastName = (By.NAME, "Last Name")
    contact = (By.NAME, "Mobile")
    emailAddress = (By.NAME, "Email")
    message = (By.NAME, "message")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    success = (By.CLASS_NAME, "alert-success")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
        #driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()

    def getFirstName(self, first):
        return self.driver.find_element(*HomePage.firstName).send_keys(first)
    def getSecondName(self, last):
        return self.driver.find_element(*HomePage.lastName).send_keys(last)
    def getMobile(self, number):
        return self.driver.find_element(*HomePage.contact).send_keys(number)
    def getEmail(self,email):
        return self.driver.find_element(*HomePage.emailAddress).send_keys(email)
    def getMessage(self,text):
        return self.driver.find_element(*HomePage.message).send_keys(text)
    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submit).click()
    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.success).text

