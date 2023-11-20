import selenium
from selenium.webdriver.common.by import By
from Git_repodemo.histories_project.POM.lib.helpers import Helpers


class HomePage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)

    christmas_start_page_button = (By.CLASS_NAME, 'block-table-of-contents__link')

    def click_on_christmas_start_page_button(self):
        self.find_and_click(self.christmas_start_page_button)

    def driver_back_button(self):
        self.driver_back()
