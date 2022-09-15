from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class InvoicePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    DELETE_INVOICE = "deleteButton"
    NUMBER_OF_INVOICES = "//tr[contains(@class,'invoice ng-scope')]"

    def getInvoice(self, invoiceNumber):
        stringInvNumber = str(invoiceNumber)
        return self.wait_for_presence_of_element_located(By.XPATH,"//tr[@class='invoice ng-scope'][" + stringInvNumber + "]/td[@class='invoice_number']/a")

    def deleteInvoice(self):
        return self.wait_for_presence_of_element_located(By.ID, self.DELETE_INVOICE).click()

    def getNumberOfInvoices(self):
        invoiceCounter = 0
        allInvoices = self.wait_for_presence_of_all_elements(By.XPATH, self.NUMBER_OF_INVOICES)
        for invoice in allInvoices:
            invoiceCounter += 1
        return invoiceCounter

    def deleteSelectedInvoice(self,invNumber):
        self.getNumberOfInvoices()
        self.getInvoice(invNumber).click()
        self.deleteInvoice()
        self.getNumberOfInvoices()