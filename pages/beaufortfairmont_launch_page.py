from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def hamburgerMenuOpen(self):
        hamburger_state = self.wait_for_presence_of_element_located(By.XPATH,"//*[contains(@class,'glyphicon-transfer')]/ancestor::div[@id='page-wrapper']")
        classValue = hamburger_state.get_attribute("class")
        hamburger_menu = self.wait_for_element_to_be_clickable(By.XPATH, "//*[contains(@class,'glyphicon-transfer')]")

        if "open" not in classValue:
            hamburger_menu.click()
