import pytest
from pages.beaufortfairmont_launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestHamburgerMenu():
    def test_hamburger_Menu(self):
        hamburgerpage = LaunchPage(self.driver)
        hamburgerpage.clickMenuIcon()