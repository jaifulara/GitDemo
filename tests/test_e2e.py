import pytest
from selenium import webdriver
from selenium.webdriver.firefox import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from tests.pageObjects.CheckoutPage import CheckOutPage
from tests.pageObjects.ConfirmPage import ConfirmPage
from tests.pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e_Indonesia(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("Getting all the card titles")
        cards = checkOutPage.getCardtTitles()
        i = -1
        for card in cards:
            cardText = card.text
            log.info(cardText)
            i = i + 1
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.clickCheckoutBtn().click()
        confirmPage = checkOutPage.clickFinalCheckout()
        confirmPage.countryInput().send_keys("Ind")
        log.info("Entering country name as Ind")

        self.verifyLinkPresence("Indonesia")
        confirmPage.countrySelectIndonesia().click()
        confirmPage.check().click()
        confirmPage.submit().click()
        SuccessText = confirmPage.success().text
        log.info("Text received from application is" + SuccessText)
        print(SuccessText)
        print("The received message from test is", SuccessText)

        assert ("Success!" in SuccessText)


    def test_e2e_India(self):
        log = self.getLogger()
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("Getting all the card titles")
        cards = checkOutPage.getCardtTitles()
        i = -1
        for card in cards:
            cardText = card.text
            log.info(cardText)
            i = i + 1
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.clickCheckoutBtn().click()
        confirmPage = checkOutPage.clickFinalCheckout()
        confirmPage.countryInput().send_keys("Ind")
        log.info("Entering country name as Ind")

        self.verifyLinkPresence("India")
        confirmPage.countrySelect().click()
        confirmPage.check().click()
        confirmPage.submit().click()
        SuccessText = confirmPage.success().text
        print(SuccessText)
        print("The received message from test is", SuccessText)

        assert ("Success!" in SuccessText)

