import time

import pytest
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from Utilits.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import confirmpage


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        print(self.driver.title)
        chek_outpage = homePage.shopItems()
        log.info("getting all the card titles")
        title = self.driver.title
        print("Click on After Shop link:-", title)
        # chek_outpage = CheckOutPage(self.driver)
        all_phone = chek_outpage.getCardTitles()
        time.sleep(5)
        for phone in all_phone:
            product_name = phone.text
            log.info(product_name)
            if product_name == "Blackberry":
                chek_outpage.getclickBtn().click()
        chek_outpage.getclickCheckoutBtn().click()
        confirm_page = chek_outpage.getClickConfirmCheckout()
        log.info("Entering country name as India")
        # confirm_page = confirmpage(self.driver)
        confirm_page.getCountry().send_keys("Ind")
        self.verifyLinkPresence("India")
        # self.driver.find_element(By.ID, "country").send_keys("Ind")
        confirm_page.getSelectCountry().click()
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        confirm_page.getClickCheckbox().click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirm_page.getClick_purchase().click()
        # self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        sueess_Text = confirm_page.getSucessMessage().text
        # sueessText = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        log.info("Text received from application" + sueess_Text)
        self.driver.save_screenshot(f".//ScreenShots//")
        assert "Succweess! Thank you!" in sueess_Text


