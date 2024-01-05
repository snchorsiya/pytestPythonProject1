import pytest
from selenium.webdriver.common.by import By

from Utilits.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    # @pytest.fixture(params=[("Ajit", "Patel@yopmail.com", "Abc@123", "Male"), ("Mona", "mona@yopmail.com", "Abc@123", "Female")])
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("name is" + getData["name"])
        homePage.get_name().send_keys(getData["name"])
        log.info("email is" + getData["email"])
        homePage.get_email().send_keys(getData["email"])
        log.info("password is" + getData["password"])
        homePage.get_password().send_keys(getData["password"])
        log.info("click on checkbox")
        homePage.get_click_checkbox().click()
        log.info("gender is" + getData["gender"])
        self.select_Option_By_Test(homePage.get_select_gender(), getData["gender"])
        log.info("Click on submit button")
        homePage.get_clickOnSubmit_btn().click()

        message = homePage.get_success_text().text
        log.info("Success Message is:" + message)

        assert "Success" in message
        self.driver.refresh()
