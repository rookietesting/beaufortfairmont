import pytest
from pages.beaufortfairmont_manage_invoice_page import InvoicePage
from pages.beaufortfairmont_launch_page import LaunchPage
from utilities.util import Utils

@pytest.mark.usefixtures("setup")
class TestExistingInvoices():
    def test_Existing_Invoices(self):
        utils = Utils()
        invoicepage = InvoicePage(self.driver)
        launchpage = LaunchPage(self.driver)

        launchpage.getInvoices()
        numberOfInvoicesStart = invoicepage.getNumberOfInvoices()
        invoicepage.deleteSelectedInvoice(1)
        numberOfInvoicesEnd = invoicepage.getNumberOfInvoices()

        utils.assertAfterDelete(numberOfInvoicesStart,numberOfInvoicesEnd)