"""
Файл с базовыми классами страницы
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# базовый класс страницы
class BassPage:

    def __init__(self, driver):
        """Конструктор"""
        self.driver = driver
        self.base_url = "http://test-stand.gb.ru"

    def find_element(self, locator, time=10):
        """Поиск элемента"""
        # ищем элементы по locator и устанавливаем ожидание time для их появления
        # так же задаем сообщение message, которое выведется в случае, если элемент не найден
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def get_element_property(self, locator, property):
        """Получение свойств элемента"""
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        """Метод открытия станицы сайта"""
        return self.driver.get(self.base_url)  # возвращаем открытую страницу
