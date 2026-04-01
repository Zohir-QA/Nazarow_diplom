import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_element(self, locator): # Ждём видимость элемента и возвращаем его
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator): # Кликаем по элементу
        return self.wait_element(locator).click()

    def window(self, number): # Переключение между окнами
        handles = self.driver.window_handles
        return  self.driver.switch_to.window(handles[number])

    def scroll_element(self, locator): # Скролит до конкретного элемента
        element = self.wait_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", element)
        return element

    def scroll_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self

    def take_screenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=text, attachment_type=allure.attachment_type.PNG)

