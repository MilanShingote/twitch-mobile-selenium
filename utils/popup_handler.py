from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopupHandler:

    CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@aria-label, 'Close')]"
    )

    @staticmethod
    def close_if_present(driver, timeout=5):
        try:
            WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(PopupHandler.CLOSE_BUTTON)
            ).click()
        except TimeoutException:
            pass
