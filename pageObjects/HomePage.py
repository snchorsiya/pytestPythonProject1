from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    submit_btn = (By.XPATH, "//input[@class='btn btn-success']")
    success_text = (By.CLASS_NAME, "alert-success")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")

    def __init__(self, driver):
        self.driver = driver

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_clickOnSubmit_btn(self):
        return self.driver.find_element(*HomePage.submit_btn)

    def get_success_text(self):
        return self.driver.find_element(*HomePage.success_text)

    def get_click_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_select_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        chek_outpage = CheckOutPage(self.driver)
        return chek_outpage
