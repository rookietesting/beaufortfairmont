from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    INITIAL_MENU_STATE = "//*[contains(@class,'glyphicon-transfer')]/ancestor::div[@id='page-wrapper']"
    MENU_BUTTON = "//*[contains(@class,'glyphicon-transfer')]"
    INVOICES = "Invoices"
    ADD_INVOICE = "Add Invoice"

    def getMenuState(self):
        return self.wait_for_presence_of_element_located(By.XPATH, self.INITIAL_MENU_STATE).get_attribute("class")

    def getMenuButton(self):
        return self.wait_for_presence_of_element_located(By.XPATH, self.MENU_BUTTON)

    def getInvoices(self):
        return self.wait_for_presence_of_element_located(By.LINK_TEXT, self.INVOICES).click()

    def getAddInvoices(self):
        return self.wait_for_presence_of_element_located(By.LINK_TEXT, self.ADD_INVOICE).click()

    def clickMenuIcon(self):
        classValue = self.getMenuState()
        if "open" not in classValue:
            self.getMenuButton().click()
