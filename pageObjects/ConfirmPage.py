from selenium.webdriver.common.by import By


class confirmpage:
    enter_country = (By.ID, "country")
    select_country = (By.LINK_TEXT, "India")
    click_Checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    click_purchase = (By.XPATH, "//input[@value='Purchase']")
    successMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def getCountry(self):
        return self.driver.find_element(*confirmpage.enter_country)

    def getSelectCountry(self):
        return self.driver.find_element(*confirmpage.select_country)

    def getClickCheckbox(self):
        return self.driver.find_element(*confirmpage.click_Checkbox)

    def getClick_purchase(self):
        return self.driver.find_element(*confirmpage.click_purchase)

    def getSucessMessage(self):
        return self.driver.find_element(*confirmpage.successMessage)

