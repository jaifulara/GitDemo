from selenium.webdriver.common.by import By

from tests.pageObjects.ConfirmPage import ConfirmPage


#driver.find_elements(By.XPATH, "//div[@class='card h-100']")
class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//h4")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkOut2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardtTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def clickCheckoutBtn(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

    def clickFinalCheckout(self):
        self.driver.find_element(*CheckOutPage.checkOut2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
