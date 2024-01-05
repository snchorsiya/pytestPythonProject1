from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import confirmpage


class CheckOutPage:
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    clickCard = (By.CSS_SELECTOR, ".card-footer button")
    clickCheckOut = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    clickCheckoutBtnConfirm = (By.XPATH, "//button[normalize-space()='Checkout']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getclickBtn(self):
        return self.driver.find_element(*CheckOutPage.clickCard)

    def getclickCheckoutBtn(self):
        return self.driver.find_element(*CheckOutPage.clickCheckOut)

    def getClickConfirmCheckout(self):
        self.driver.find_element(*CheckOutPage.clickCheckoutBtnConfirm).click()
        confirm_page = confirmpage(self.driver)
        return confirm_page
