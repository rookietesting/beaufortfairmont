from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class InvoicePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def openInvoice(self, invoiceNumber):
        stringInvNumber = str(invoiceNumber)
        invoiceNumbers = self.wait_for_presence_of_element_located(By.XPATH,"//tr[@class='invoice ng-scope'][" + stringInvNumber + "]/td[@class='invoice_number']/a")
        invoiceNumbers.click()

    def deleteInvoice(self):
        deleteInvoice = self.wait_for_presence_of_element_located(By.ID, "deleteButton")
        deleteInvoice.click()

    def numberOfInvoices(self):
        invoiceCounter = 0
        allInvoices = self.wait_for_presence_of_all_elements(By.XPATH, "//tr[contains(@class,'invoice ng-scope')]")
        for invoice in allInvoices:
            invoiceCounter += 1

        return invoiceCounter
