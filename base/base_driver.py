from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def wait_for_presence_of_all_elements(self,locator_type, locator):
        wait = WebDriverWait(self.driver,10)
        list_of_elemets = wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elemets

    def wait_for_presence_of_element_located(self,locator_type, locator):
        wait = WebDriverWait(self.driver,10)
        elemet = wait.until(EC.presence_of_element_located((locator_type,locator)))
        return elemet

    def wait_for_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver,10)
        elemets = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return elemets
