import pytest
from pages.beaufortfairmont_manage_invoice_page import InvoicePage
from pages.beaufortfairmont_launch_page import LaunchPage
from utilities.util import Utils

@pytest.mark.usefixtures("setup")
class TestExistingInvoices():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.invoicepage = InvoicePage(self.driver)
        self.launchpage = LaunchPage(self.driver)
        self.utils = Utils()

    def test_Delete_Existing_Invoices(self):
        self.launchpage.getInvoices()
        numberOfInvoicesStart = self.invoicepage.getNumberOfInvoices()
        self.invoicepage.deleteSelectedInvoice(1)
        numberOfInvoicesEnd = self.invoicepage.getNumberOfInvoices()
        self.utils.assertInvoicesAfterDelete(numberOfInvoicesStart,numberOfInvoicesEnd)