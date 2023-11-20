from Git_repodemo.histories_project.POM.lib import helpers
from Git_repodemo.histories_project.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By
from Git_repodemo.histories_project.POM.lib.assertions import assert_that


class ChristmasStartPageHeader(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    christmas_page_header = (By.LINK_TEXT, 'How Did Christmas Start?')

    def assert_christmas_page_button(self, christmas_page_header_text='How Did Christmas Start?'):
        expected_text = self.find(self.christmas_page_header, get_text=True)
        assert_that(expected_text, christmas_page_header_text)
