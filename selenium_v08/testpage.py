"""
Файл с локаторами
"""
from BassApp import BassPage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    """Класс с локаторами."""

    # Локатор поля ввода Username
    LOCATOR_INPUT_USERNAME = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")

    # Локатор поля ввода Password
    LOCATOR_INPUT_PASSWORD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")

    # Локатор кода ошибки 401
    LOCATOR_ERR_LABEL = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")

    # Локатор кнопки Login
    LOCATOR_BTN_LOGIN = (By.CSS_SELECTOR, "button")

    # Локатор текста приветствия
    LOCATOR_GREETING_TEXT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")

    # Локатор кнопки создания поста
    LOCATOR_CREATE_BTN = (By.CSS_SELECTOR, "#create-btn")

    # Локатор поля Title
    LOCATOR_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")

    # Локатор поля Description
    LOCATOR_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")

    # Локатор поля Content
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")

    # Локатор кнопки SAVE
    LOCATOR_BTN_SAVE = (By.CSS_SELECTOR, ".button")

    # Локатор заголовка нового поста на странице поста
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")

    # Локатор кнопки Home
    LOCATOR_BTN_HOME = (By.CSS_SELECTOR, "span")

    # Локатор заголовка первого поста на главной странице
    LOCATOR_FIRST_POST = (By.XPATH, """//*[@id="app"]/main/div/div[3]/div[1]/a[1]/h2""")

    # Локатор кнопки Contact
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")

    # Локатор поля Your name формы Contact us
    LOCATOR_INPUT_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")

    # Локатор поля Your email формы Contact us
    LOCATOR_INPUT_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")

    # Локатор поля Content формы Contact us
    LOCATOR_INPUT_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")

    # Локатор кнопки CONTACT US
    LOCATOR_CONTACT_US_BTN = (By.CSS_SELECTOR, "button[type='submit']")


class OperationsHelper(BassPage):
    """
    Класс с методами
    """

    def fill_login_field(self, word):
        """Ввод данных в поле Username"""
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_INPUT_USERNAME[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_USERNAME)  # ищем элемент Username
        login_field.clear()  # отчищаем поле
        login_field.send_keys(word)  # вписываем текст в поле

    def fill_pass_field(self, word):
        """Ввод данных в поле Password"""
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_INPUT_PASSWORD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_PASSWORD)   # ищем элемент Password
        pass_field.clear()  # отчищаем поле
        pass_field.send_keys(word)  # вписываем текст в поле

    def click_login_button(self):
        """Клик по кнопке Login"""
        logging.info(f"Click login button")
        self.find_element(TestSearchLocators.LOCATOR_BTN_LOGIN).click()

    def get_error_text(self):
        """Метод получения и возврата текста сообщения об ошибке"""
        # ищем элемент, но перед этим ждем для того, чтобы элемент успел появиться
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERR_LABEL, time=2)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERR_LABEL[1]}")
        return text     # возвращаем только текст ошибки

    def get_greeting_text(self):
        """Метод получения и возврата текста приветствия при успешной аутентификации"""
        # ищем элемент, но перед этим ждем для того, чтобы элемент успел появиться
        greeting_text = self.find_element(TestSearchLocators.LOCATOR_GREETING_TEXT, time=10)
        text = greeting_text.text
        logging.info(f"We find text {text} in greeting field {TestSearchLocators.LOCATOR_GREETING_TEXT[1]}")
        return text     # возвращаем только текст приветствия

    def click_create_new_post_icon(self):
        """Клик по иконке Create new post"""
        logging.info(f"Click on the Create new post icon")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_BTN, time=10).click()

    def fill_title_field(self, word):
        """Ввод данных в поле Title"""
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_TITLE[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)  # ищем элемент Title
        title_field.clear()  # отчищаем поле
        title_field.send_keys(word)  # вписываем текст в поле

    def fill_description_field(self, word):
        """Ввод данных в поле Description"""
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION[1]}")
        description_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)  # ищем элемент Description
        description_field.clear()  # отчищаем поле
        description_field.send_keys(word)  # вписываем текст в поле

    def fill_content_field(self, word):
        """Ввод данных в поле Content"""
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)  # ищем элемент Content
        content_field.clear()  # отчищаем поле
        content_field.send_keys(word)  # вписываем текст в поле

    def click_save_button(self):
        """Клик по кнопке SAVE"""
        logging.info(f"Click on the SAVE button")
        self.find_element(TestSearchLocators.LOCATOR_BTN_SAVE, time=10).click()

    def get_post_title(self):
        """Метод получения и возврата заголовка поста на странице поста"""
        # ищем элемент, но перед этим ждем для того, чтобы элемент успел появиться
        post_title = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE, time=10)
        text = post_title.text
        logging.info(f"We find text {text} in greeting field {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        return text  # возвращаем только текст заголовка поста

    def click_home_button(self):
        """Клик по кнопке Home"""
        logging.info(f"Click on the Home button")
        self.find_element(TestSearchLocators.LOCATOR_BTN_HOME, time=10).click()

    def get_title_of_first_post(self):
        """Метод получения и возврата заголовка первого поста на главной странице"""
        post_title = self.find_element(TestSearchLocators.LOCATOR_FIRST_POST, time=10)
        text = post_title.text
        logging.info(f"We find text {text} in greeting field {TestSearchLocators.LOCATOR_FIRST_POST[1]}")
        return text  # возвращаем только текст заголовка поста

    def click_contact_button(self):
        """Клик по кнопке Contact"""
        logging.info(f"Click on the Contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN, time=10).click()

    def fill_your_name_field(self, word):
        """Ввод данных в поле Your name формы Contact us"""
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_INPUT_YOUR_NAME[1]}")
        your_name_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_YOUR_NAME)  # ищем элемент Your name
        your_name_field.clear()  # отчищаем поле
        your_name_field.send_keys(word)  # вписываем текст в поле

    def fill_your_email_field(self, word):
        """Ввод данных в поле Your email формы Contact us"""
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_INPUT_YOUR_EMAIL[1]}")
        your_email_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_YOUR_EMAIL)  # ищем элемент Your email
        your_email_field.clear()  # отчищаем поле
        your_email_field.send_keys(word)  # вписываем текст в поле

    def fill_your_content_field(self, word):
        """Ввод данных в поле Content формы Contact us"""
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_INPUT_CONTENT[1]}")
        your_content_field = self.find_element(TestSearchLocators.LOCATOR_INPUT_CONTENT)  # ищем элемент Content
        your_content_field.clear()  # отчищаем поле
        your_content_field.send_keys(word)  # вписываем текст в поле

    def click_contact_us_button(self):
        """Клик по кнопке CONTACT US"""
        logging.info(f"Click on the CONTACT US button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN, time=10).click()

    def get_alert(self):
        """Метод получения и возврата текста alert после успешной отправки формы"""
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f"We find text {text} in field alert")
        return text
