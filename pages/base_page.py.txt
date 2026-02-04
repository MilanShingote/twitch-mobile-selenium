from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.popup_handler import PopupHandler


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def handle_popup(self):
        PopupHandler.close_if_present(self.driver)


    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def scroll_down(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
