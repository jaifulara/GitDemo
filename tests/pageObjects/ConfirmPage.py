from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryName = (By.ID, "country")
    countryIndia = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitBtn = (By.CSS_SELECTOR, "input[type='submit']")
    successMsg = (By.CLASS_NAME, "alert-success")

    def countryInput(self):
        return self.driver.find_element(*ConfirmPage.countryName)


    def countrySelect(self):
        return self.driver.find_element(*ConfirmPage.countryIndia)

    def check(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def submit(self):
        return self.driver.find_element(*ConfirmPage.submitBtn)

    def success(self):
        return self.driver.find_element(*ConfirmPage.successMsg)
