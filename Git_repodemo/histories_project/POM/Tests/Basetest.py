import pytest


@pytest.mark.usefixtures('get_driver')
class BaseTest:
    def navigate_christmas_page_and_check_header(self):
        self.homepage.click_on_christmas_start_page_button()
        self.christmasstartpage.assert_christmas_page_button()
        self.homepage.driver_back()
        self.saturnaliapage.assert_saturnalia_page_button()



