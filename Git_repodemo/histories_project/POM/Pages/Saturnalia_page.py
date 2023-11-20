from Git_repodemo.histories_project.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By
from Git_repodemo.histories_project.POM.lib.assertions import assert_that


class SaturnaliaPage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    saturnalia_page_header = (By.ID, 'saturnalia-and-christmas')

    def assert_saturnalia_page_button(self, saturnalia_page_header_text='Saturnalia and Christmas'):
        expected_text = self.find(self.saturnalia_page_header, get_text=True)
        assert_that(expected_text, saturnalia_page_header_text)
