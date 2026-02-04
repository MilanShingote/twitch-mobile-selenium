from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class SearchResultsPage(BasePage):

    SEARCH_INPUT = (
        By.TAG_NAME,
        "input"
    )

    STREAMER_CARDS = (
        By.XPATH,
        "//a[contains(@href, '/')]"
    )

    def search_for(self, text):
        self.send_keys(self.SEARCH_INPUT, text)

    def scroll_down_times(self, times=2):
        for _ in range(times):
            self.scroll_down()
            time.sleep(1)

    def select_first_streamer(self):
        streamers = self.driver.find_elements(*self.STREAMER_CARDS)
        if not streamers:
            raise Exception("No streamers found")
        streamers[0].click()
