import pytest
from pages.beaufortfairmont_manage_invoice_page import InvoicePage
from utilities.util import Utils

@pytest.mark.usefixtures("setup")
class TestExistingInvoices():
    def test_Existing_Invoices(self):
        utils = Utils()
        invoicepage = InvoicePage(self.driver)

        numberOfInvoicesStart = invoicepage.numberOfInvoices()
        invoicepage.openInvoice(1)
        invoicepage.deleteInvoice()
        numberOfInvoicesEnd = invoicepage.numberOfInvoices()

        utils.assertAfterDelete(numberOfInvoicesStart,numberOfInvoicesEnd)