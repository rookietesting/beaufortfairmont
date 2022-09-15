import pytest
from pages.beaufortfairmont_launch_page import LaunchPage
from utilities.util import Utils


@pytest.mark.usefixtures("setup")
class TestHamburgerMenu():
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.hamburgerpage = LaunchPage(self.driver)
        self.utils = Utils()

    def test_hamburger_Menu(self):
        self.hamburgerpage.clickMenuIcon()
        menuState = self.hamburgerpage.getMenuState()
        self.utils.asserMenuStateOpen(menuState)