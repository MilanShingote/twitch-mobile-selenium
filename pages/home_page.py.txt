from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.twitch.tv"

    SEARCH_ICON = (
        By.XPATH,
        "//a[contains(@href,'/search')]"
    )

    def open(self):
        self.driver.get(self.URL)

    def tap_search(self):
        self.click(self.SEARCH_ICON)
